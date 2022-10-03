from dmt.blueprint import Blueprint
from dmt.attribute import Attribute

class EntityBlueprint(Blueprint):
    """Core entity"""

    def __init__(self, name="Entity", package_path="dmt", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
