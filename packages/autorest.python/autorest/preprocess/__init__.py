# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The preprocessing autorest plugin.
"""
import copy
from typing import Callable, Dict, Any, List, Optional

from .._utils import to_snake_case
from .helpers import pad_reserved_words, add_redefined_builtin_info
from .python_mappings import PadType

from .. import YamlUpdatePlugin, YamlUpdatePluginAutorest
from .._utils import parse_args, get_body_type_for_description, JSON_REGEXP, KNOWN_TYPES


def add_body_param_type(code_model: Dict[str, Any], body_parameter: Dict[str, Any]):
    if (
        body_parameter
        and body_parameter["type"]["type"] in ("model", "dict", "list")
        and any(
            ct for ct in body_parameter.get("contentTypes", []) if JSON_REGEXP.match(ct)
        )
        and not body_parameter["type"].get("xmlMetadata")
        and not any(t for t in ["flattened", "groupedBy"] if body_parameter.get(t))
    ):
        body_parameter["type"] = {
            "type": "combined",
            "types": [body_parameter["type"], KNOWN_TYPES["binary"]],
        }
        code_model["types"].append(body_parameter["type"])


def update_overload_section(
    overload: Dict[str, Any],
    yaml_data: Dict[str, Any],
    section: str,
):
    for overload_s, original_s in zip(overload[section], yaml_data[section]):
        if overload_s.get("type"):
            overload_s["type"] = original_s["type"]
        if overload_s.get("headers"):
            for overload_h, original_h in zip(
                overload_s["headers"], original_s["headers"]
            ):
                if overload_h.get("type"):
                    overload_h["type"] = original_h["type"]


def add_overload(yaml_data: Dict[str, Any], body_type: Dict[str, Any]):
    overload = copy.deepcopy(yaml_data)
    overload["isOverload"] = True
    overload["bodyParameter"]["type"] = body_type

    overload["overloads"] = []

    # for yaml sync, we need to make sure all of the responses, parameters, and exceptions' types have the same yaml id
    for overload_p, original_p in zip(overload["parameters"], yaml_data["parameters"]):
        overload_p["type"] = original_p["type"]
    update_overload_section(overload, yaml_data, "responses")
    update_overload_section(overload, yaml_data, "exceptions")

    # update content type to be an overloads content type
    content_type_param = next(
        p for p in overload["parameters"] if p["restApiName"].lower() == "content-type"
    )
    content_type_param["inOverload"] = True
    content_type_param["inDocstring"] = True
    body_type_description = get_body_type_for_description(overload["bodyParameter"])
    content_type_param[
        "description"
    ] = f"Body Parameter content-type. Content type parameter for {body_type_description} body."
    content_types = yaml_data["bodyParameter"]["contentTypes"]
    if body_type["type"] == "binary" and len(content_types) > 1:
        content_types = "'" + "', '".join(content_types) + "'"
        content_type_param["description"] += f" Known values are: {content_types}."
    return overload


def add_overloads_for_body_param(yaml_data: Dict[str, Any]) -> None:
    """If we added a body parameter type, add overloads for that type"""
    body_parameter = yaml_data["bodyParameter"]
    if not (
        body_parameter["type"]["type"] == "combined"
        and len(yaml_data["bodyParameter"]["type"]["types"])
        > len(yaml_data["overloads"])
    ):
        return
    for body_type in body_parameter["type"]["types"]:
        if any(
            o
            for o in yaml_data["overloads"]
            if id(o["bodyParameter"]["type"]) == id(body_type)
        ):
            continue
        yaml_data["overloads"].append(add_overload(yaml_data, body_type))
    content_type_param = next(
        p for p in yaml_data["parameters"] if p["restApiName"].lower() == "content-type"
    )
    content_type_param["inOverload"] = False
    content_type_param["inOverriden"] = True
    content_type_param["inDocstring"] = True
    content_type_param[
        "clientDefaultValue"
    ] = None  # make it none bc it will be overriden, we depend on default of overloads
    content_type_param["optional"] = True


def _remove_paging_maxpagesize(yaml_data: Dict[str, Any]) -> None:
    # we don't expose maxpagesize for version tolerant generation
    # users should be passing this into `by_page`
    yaml_data["parameters"] = [
        p
        for p in yaml_data.get("parameters", [])
        if p["restApiName"].lower() not in ["maxpagesize", "$maxpagesize"]
    ]


def update_description(
    description: Optional[str], default_description: str = ""
) -> str:
    if not description:
        description = default_description
    description.rstrip(" ")
    if description and description[-1] != ".":
        description += "."
    return description


def update_operation_group_class_name(
    yaml_data: Dict[str, Any], class_name: str
) -> str:
    if class_name == "":
        return yaml_data["client"]["name"] + "OperationsMixin"
    if class_name == "Operations":
        return "Operations"
    return class_name + "Operations"


def update_parameter(yaml_data: Dict[str, Any]) -> None:
    yaml_data["description"] = update_description(yaml_data["description"])
    if not (
        yaml_data["location"] == "header"
        and yaml_data["clientName"] in ("content_type", "accept")
    ):
        yaml_data["clientName"] = pad_reserved_words(
            yaml_data["clientName"].lower(), PadType.PARAMETER
        )
    if yaml_data.get("propertyToParameterName"):
        # need to create a new one with padded keys and values
        yaml_data["propertyToParameterName"] = {
            pad_reserved_words(prop, PadType.PROPERTY)
            .lower(): pad_reserved_words(param_name, PadType.PARAMETER)
            .lower()
            for prop, param_name in yaml_data["propertyToParameterName"].items()
        }


def update_types(yaml_data: List[Dict[str, Any]]) -> None:
    for type in yaml_data:
        for property in type.get("properties", []):
            property["description"] = update_description(property["description"])
            property["clientName"] = pad_reserved_words(
                property["clientName"].lower(), PadType.PROPERTY
            )
            add_redefined_builtin_info(property["clientName"], property)
        if type.get("name"):
            type["description"] = update_description(type["description"], type["name"])
            type["snakeCaseName"] = to_snake_case(type["name"])


def update_client(yaml_data: Dict[str, Any]) -> None:
    yaml_data["description"] = update_description(
        yaml_data["description"], default_description=yaml_data["name"]
    )
    yaml_data["moduleName"] = to_snake_case(yaml_data["name"].replace(" ", "_"))
    for parameter in yaml_data["parameters"]:
        update_parameter(parameter)


def update_paging_response(yaml_data: Dict[str, Any]) -> None:
    yaml_data["discriminator"] = "paging"
    yaml_data["pagerSync"] = yaml_data.get("pagerSync") or "azure.core.paging.ItemPaged"
    yaml_data["pagerAsync"] = (
        yaml_data.get("pagerAsync") or "azure.core.async_paging.AsyncItemPaged"
    )


class PreProcessPlugin(YamlUpdatePlugin):  # pylint: disable=abstract-method
    """Add Python naming information."""

    @property
    def version_tolerant(self) -> bool:
        return self.options.get("version-tolerant", True)

    def get_operation_updater(
        self, yaml_data: Dict[str, Any]
    ) -> Callable[[Dict[str, Any], Dict[str, Any]], None]:
        if yaml_data["discriminator"] == "lropaging":
            return self.update_lro_paging_operation
        if yaml_data["discriminator"] == "lro":
            return self.update_lro_operation
        if yaml_data["discriminator"] == "paging":
            return self.update_paging_operation
        return self.update_operation

    def update_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
        *,
        is_overload: bool = False,
    ) -> None:
        yaml_data["groupName"] = pad_reserved_words(
            yaml_data["groupName"], PadType.OPERATION_GROUP
        )
        yaml_data["groupName"] = to_snake_case(yaml_data["groupName"])
        yaml_data["name"] = yaml_data["name"].lower()
        yaml_data["name"] = pad_reserved_words(yaml_data["name"], PadType.METHOD)
        yaml_data["description"] = update_description(
            yaml_data["description"], yaml_data["name"]
        )
        yaml_data["summary"] = update_description(yaml_data.get("summary", ""))
        body_parameter = yaml_data.get("bodyParameter")
        for parameter in yaml_data["parameters"]:
            update_parameter(parameter)
        if yaml_data.get("bodyParameter"):
            update_parameter(yaml_data["bodyParameter"])
            for entry in yaml_data["bodyParameter"].get("entries", []):
                update_parameter(entry)
        for overload in yaml_data.get("overloads", []):
            self.update_operation(code_model, overload, is_overload=True)
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "operation"
        if body_parameter and not is_overload:
            # if we have a JSON body, we add a binary overload
            add_body_param_type(code_model, body_parameter)
            add_overloads_for_body_param(yaml_data)

    def _update_lro_operation_helper(self, yaml_data: Dict[str, Any]) -> None:
        azure_arm = self.options.get("azure-arm", False)
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "lro"
            response["pollerSync"] = (
                response.get("pollerSync") or "azure.core.polling.LROPoller"
            )
            response["pollerAsync"] = (
                response.get("pollerAsync") or "azure.core.polling.AsyncLROPoller"
            )
            if not response.get("pollingMethodSync"):
                response["pollingMethodSync"] = (
                    "azure.mgmt.core.polling.arm_polling.ARMPolling"
                    if azure_arm
                    else "azure.core.polling.base_polling.LROBasePolling"
                )
            if not response.get("pollingMethodAsync"):
                response["pollingMethodAsync"] = (
                    "azure.mgmt.core.polling.async_arm_polling.AsyncARMPolling"
                    if azure_arm
                    else "azure.core.polling.async_base_polling.AsyncLROBasePolling"
                )

    def update_lro_paging_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
        is_overload: bool = False,
    ) -> None:
        self.update_lro_operation(code_model, yaml_data, is_overload=is_overload)
        self.update_paging_operation(code_model, yaml_data, is_overload=is_overload)
        yaml_data["discriminator"] = "lropaging"
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "lropaging"
        for overload in yaml_data.get("overloads", []):
            self.update_lro_paging_operation(code_model, overload, is_overload=True)

    def update_lro_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
        is_overload: bool = False,
    ) -> None:
        self.update_operation(code_model, yaml_data, is_overload=is_overload)
        self._update_lro_operation_helper(yaml_data)
        for overload in yaml_data.get("overloads", []):
            self._update_lro_operation_helper(overload)

    def update_paging_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
        is_overload: bool = False,
    ) -> None:
        self.update_operation(code_model, yaml_data, is_overload=is_overload)
        if not yaml_data.get("pagerSync"):
            yaml_data["pagerSync"] = "azure.core.paging.ItemPaged"
        if not yaml_data.get("pagerAsync"):
            yaml_data["pagerAsync"] = "azure.core.async_paging.AsyncItemPaged"
        returned_response_object = (
            yaml_data["nextOperation"]["responses"][0]
            if yaml_data.get("nextOperation")
            else yaml_data["responses"][0]
        )
        if self.version_tolerant:
            # if we're in version tolerant, hide the paging model
            returned_response_object["type"]["isPublic"] = False
            _remove_paging_maxpagesize(yaml_data)
        item_type = next(
            p["type"]["elementType"]
            for p in returned_response_object["type"]["properties"]
            if p["restApiName"] == (yaml_data.get("itemName") or "value")
        )
        if yaml_data.get("nextOperation"):
            if self.version_tolerant:
                _remove_paging_maxpagesize(yaml_data["nextOperation"])
            yaml_data["nextOperation"]["groupName"] = pad_reserved_words(
                yaml_data["nextOperation"]["groupName"], PadType.OPERATION_GROUP
            )
            yaml_data["nextOperation"]["groupName"] = to_snake_case(
                yaml_data["nextOperation"]["groupName"]
            )
            for response in yaml_data["nextOperation"].get("responses", []):
                update_paging_response(response)
                response["itemType"] = item_type
        for response in yaml_data.get("responses", []):
            update_paging_response(response)
            response["itemType"] = item_type
        for overload in yaml_data.get("overloads", []):
            self.update_paging_operation(code_model, overload, is_overload=True)

    def update_operation_groups(self, yaml_data: Dict[str, Any]) -> None:
        operation_groups_yaml_data = yaml_data["operationGroups"]
        for operation_group in operation_groups_yaml_data:
            operation_group["propertyName"] = pad_reserved_words(
                operation_group["propertyName"], PadType.OPERATION_GROUP
            )
            operation_group["propertyName"] = to_snake_case(
                operation_group["propertyName"]
            )
            operation_group["className"] = update_operation_group_class_name(
                yaml_data, operation_group["className"]
            )
            for operation in operation_group["operations"]:
                self.get_operation_updater(operation)(yaml_data, operation)

    def update_yaml(self, yaml_data: Dict[str, Any]) -> None:
        """Convert in place the YAML str."""
        update_client(yaml_data["client"])
        self.update_operation_groups(yaml_data)
        update_types(yaml_data["types"])


class PreProcessPluginAutorest(YamlUpdatePluginAutorest, PreProcessPlugin):
    def get_options(self) -> Dict[str, Any]:
        options = {
            "version-tolerant": self._autorestapi.get_boolean_value("version-tolerant"),
            "azure-arm": self._autorestapi.get_boolean_value("azure-arm"),
        }
        return {k: v for k, v in options.items() if v is not None}


if __name__ == "__main__":
    # CADL pipeline will call this
    args, unknown_args = parse_args()
    PreProcessPlugin(
        output_folder=args.output_folder, cadl_file=args.cadl_file, **unknown_args
    ).process()