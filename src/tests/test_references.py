"""Round trip of cross references, single and lists, through JSON and H5"""
from pathlib import Path

import pytest

from dmt.dmt_reader import DMTReader
from dmt.dmt_writer import DMTWriter
from dmt.h5.h5_reader import H5Reader
from dmt.h5.h5_writer import H5Writer
from tests.some_entity import SomeEntity


def __create_root():
    root = SomeEntity()
    root.name = "root"
    first, second, third = SomeEntity(), SomeEntity(), SomeEntity()
    first.name = "first"
    second.name = "second"
    third.name = "third"
    root.children = [first, second, third]
    # Forward and backward references, so some resolve only after the whole file is read
    second.refs = [third, first]
    first.ref = third
    return root


def __assert_references(root: SomeEntity):
    first, second, third = root.children
    assert len(second.refs) == 2
    assert second.refs[0] is third
    assert second.refs[1] is first
    assert first.ref is third
    assert first.refs == []
    assert third.ref is None


def test_write_reference_list():
    res = DMTWriter().to_dict(__create_root())
    first, second, third = res["children"]
    assert second["refs"] == [{"_id": third["_id"]}, {"_id": first["_id"]}]
    assert first["ref"] == {"_id": third["_id"]}
    assert "refs" not in first


def test_json_round_trip(tmpdir):
    file = Path(tmpdir) / "test.json"
    DMTWriter().write(__create_root(), file)
    __assert_references(DMTReader().read(file))


def test_h5_round_trip(tmpdir):
    file = Path(tmpdir) / "test.h5"
    H5Writer().write([__create_root()], file)
    entities = H5Reader().read(file)
    assert len(entities) == 1
    __assert_references(entities[0])


def test_unresolved_reference_in_list():
    res = DMTWriter().to_dict(__create_root())
    res["children"][1]["refs"].append({"_id": "missing"})
    with pytest.raises(ValueError, match="Unresolved reference"):
        DMTReader().from_dict(res)
