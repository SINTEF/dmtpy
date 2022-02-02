"""
{"name": "x", "type": "float", "description": "point, x coordinates"},
"""
from .dimension import Dimension

class Attribute:
    """ A property"""

    def __init__(self,name:str ,property_type:str,description:str, *dimensions: Dimension,
                 optional=True, default=None) -> None:
        self.name = name
        self.property_type = property_type
        self.description = description
        self.dimensions = dimensions
        self.optional = optional
        self.default = default

        primitive_types =  ['boolean', 'number', 'string', 'integer']
        self.__is_primitive = property_type in primitive_types

    def has_dimensions(self):
        """Has dimensions"""
        return self.dimensions and len(self.dimensions)>0

    def is_boolean(self):
        """Is this a boolean primitive?"""
        return self.property_type == 'boolean'

    def is_string(self):
        """Is this a String primitive?"""
        return self.property_type == 'string' or self.property_type == 'char'

    @property
    def contained(self) -> bool:
        """Is this attribute contained"""
        return True

    @property
    def is_primitive(self) -> bool:
        """Is this a primitive attribute"""
        return self.__is_primitive

    @property
    def is_enum(self) -> bool:
        """Is this an enum primitive?"""
        return False
