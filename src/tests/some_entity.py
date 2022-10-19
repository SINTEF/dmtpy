from dmt.blueprint import Blueprint
from dmt.attribute import Attribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.enum_attribute import EnumAttribute
from dmt.entity import Entity
from dmt.dimension import Dimension
class SomeEntityBlueprint(Blueprint):

    """Blueprint used for testing"""

    def __init__(self):

        super().__init__(name="SomeEntity", package_path="tests")
        self.add_attribute(Attribute("name", "string", "", optional=False, default=1))
        self.add_attribute(Attribute("myint", "integer", "", optional=False, default=1))
        self.add_attribute(Attribute("myArray", "number", "",Dimension("size")))
        self.add_attribute(BlueprintAttribute("children", self.get_path(), "",True,Dimension("size")))
        self.add_attribute(Attribute("mystrings", "string", "", Dimension("size")))
        self.add_attribute(BlueprintAttribute("child", self.get_path(), "",True))
        self.add_attribute(EnumAttribute("myEnum","tests/SomeEnum",""))
        self.add_attribute(BlueprintAttribute("ref", self.get_path(), "",False))


class SomeEntity(Entity):

    """An entity used for testing"""

    def __init__(self):
        super().__init__()

        self.__blueprint = SomeEntityBlueprint()

    @property
    def blueprint(self) -> Blueprint:

        """Return blueprint that this entity represents"""
        return self.__blueprint

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)
