"""
CP1404 Assignment 2
Tests for PlaceCollection
Student: Qiuhao Wu
ID: 15136727
"""
from placecollection import PlaceCollection
from place import Place


def test_collection():
    c = PlaceCollection()
    c.add_place(Place("A", "B", 1, False))
    c.add_place(Place("C", "D", 2, True))
    assert len(c.places) == 2
    assert c.get_unvisited_count() == 1
    print("All tests passed")


test_collection()