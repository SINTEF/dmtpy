from dmt.blueprint import Blueprint
from dmt.attribute import Attribute
from .entity import EntityBlueprint

class NamedEntityBlueprint(EntityBlueprint):
    """Core named entity"""

    def __init__(self, name="NamedEntity", package_path="dmt", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
