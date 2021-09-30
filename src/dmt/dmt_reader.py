""" Creates entities from Dicts """


import json
from importlib import import_module
from typing import Dict, Sequence
from .attribute import Attribute
from .blueprint_attribute import BlueprintAttribute
from .entity import Entity


class DMTReader():
    """ Creates entities from Dicts """

    class Reference:
        """Holds a reference until it can be resolved"""

        def __init__(self,entity, prop: Attribute,uid: str):
            self.entity = entity
            self.prop = prop
            self.uid = uid

    def __init__(self):
        self.entities = dict()
        self.unresolved = list()

    def read(self, filename) -> Entity:
        """ Read entity from file """
        with open(filename, 'r',encoding="utf-8") as file:
            res=json.load(file)
            return self.from_dict(res)


    def from_dict(self,ent_dict: Dict) -> Entity:
        """ Create entity from Dict """
        entity=self.__from_dict(ent_dict)
        self.__resolve_all()
        return entity

    def from_dicts(self,ent_dicts: Sequence[Dict]) -> Sequence[Entity]:
        """ Create entity from Dict """
        entities = [self.__from_dict(e) for e in ent_dicts]
        self.__resolve_all()
        return entities

    def __resolve_all(self):
        for ref in self.unresolved:
            if not self.__resolve(ref):
                raise Exception(f"Unresolved reference: {ref}")


    def __from_dict(self,ent_dict: Dict) -> Entity:
        """ Read entities from Dict """
        entity_type: str=ent_dict["type"]
        pkg: any = None
        parts = entity_type.split("/")
        if parts[0] == "":
            del parts[0]
        ename = parts.pop()
        package_path = ".".join(parts)
        pkg = import_module(package_path)
        if not pkg:
            raise Exception(f"Unable to load package {package_path}")

        constructor = pkg.__dict__.get(ename)
        if not constructor:
            raise Exception(f"Unkown entity type {entity_type}")
        entity_instance: Entity = constructor()
        blueprint = entity_instance.blueprint
        for key, value in ent_dict.items():
            if key == "_id":
                uid = value
                self.entities[uid] = entity_instance
                continue
            if key == "type":
                continue
            attribute = blueprint.get_attribute(key)
            if not attribute:
                #FIXME
                continue
            if isinstance(attribute, BlueprintAttribute):
                self.__set_blueprint_value(entity_instance,attribute,key,value)
            else:
                setattr(entity_instance,key, value)

        return entity_instance

    def __set_blueprint_value(self,entity_instance: Entity, attribute: BlueprintAttribute,key: str,value):
        if attribute.contained:
            self.__set_value(entity_instance,attribute,value)
        else:
            self.__set_reference(entity_instance,attribute,value)

    def __set_reference(self,entity_instance: Entity,prop: Attribute,value):
        if isinstance(value, Dict):
            uid=value["_id"]
            ref = self.Reference(entity_instance,prop,uid)
            if not self.__resolve(ref):
                self.unresolved.append(ref)
        return

    def __set_value(self,entity_instance: Entity, attribute: BlueprintAttribute,value):
        if isinstance(value, Sequence):
            children = [self.__from_dict(v) for v in value]
            setattr(entity_instance,attribute.name, children)
        elif isinstance(value, Dict):
            child=self.__from_dict(value)
            if child:
                setattr(entity_instance,attribute.name, child)
        else:
            setattr(entity_instance,attribute.name, value)

    def __resolve(self, ref: Reference):
        value = self.entities.get(ref.uid)
        if value:
            self.__set_value(ref.entity,ref.prop,value)
            return True
        return False
