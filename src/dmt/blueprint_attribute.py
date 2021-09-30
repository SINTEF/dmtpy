"""
{"name": "x", "type": "float", "description": "point, x coordinates"},
"""
from .attribute import Attribute
from .dimension import Dimension

class BlueprintAttribute(Attribute):
    """ A property"""

    def __init__(self,name:str ,property_type:str,description:str, contained: bool, *dimensions: Dimension) -> None:
        super().__init__(name,property_type,description,*dimensions)
        self.__contained = contained

    @property
    def contained(self) -> bool:
        return self.__contained


    @contained.setter
    def contained(self, value: bool):
        """Set uid"""
        self.__contained = value
