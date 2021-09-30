"""
{"name": "x", "type": "float", "description": "point, x coordinates"},
"""
from .dimension import Dimension

class Attribute:
    """ A property"""

    def __init__(self,name:str ,property_type:str,description:str, *dimensions: Dimension) -> None:
        self.name = name
        self.property_type = property_type
        self.description = description
        self.dimensions = dimensions
        primitive_types =  ['boolean', 'number', 'string', 'integer']
        self.__is_primitive = property_type in primitive_types

    def has_dimensions(self):
        return self.dimensions and len(self.dimensions)>0

    def is_boolean(self):
        return self.property_type == 'boolean'

    def is_string(self):
        return self.property_type == 'string' or self.property_type == 'char'

    @property
    def contained(self) -> bool:
        return True

    @property
    def is_primitive(self) -> bool:
        """Is this a primitive attribute"""
        return self.__is_primitive

    @property
    def is_enum(self) -> bool:
        return False
