# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Fish(Model):
    """Fish.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Salmon, Shark

    :param species:
    :type species: str
    :param length:
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param fishtype: Constant filled by server.
    :type fishtype: str
    """

    _validation = {
        'length': {'required': True},
        'fishtype': {'required': True},
    }

    _attribute_map = {
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'fishtype': {'key': 'fishtype', 'type': 'str'},
    }

    _subtype_map = {
        'fishtype': {'salmon': 'Salmon', 'shark': 'Shark'}
    }

    def __init__(self, length, species=None, siblings=None):
        super(Fish, self).__init__()
        self.species = species
        self.length = length
        self.siblings = siblings
        self.fishtype = None