from dmt.attribute import Attribute

def test_attribute_creation():

    attribute  = Attribute("myint","integer","description")
    assert attribute.name is "myint"
    assert attribute.is_primitive

    
