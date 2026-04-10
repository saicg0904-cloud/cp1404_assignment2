"""
CP1404 Assignment 2
Tests for Place
Student: Qiuhao Wu
ID: 15136727
"""
from place import Place


def test_place():
    p1 = Place("A", "B", 1, False)
    assert p1.name == "A"
    assert p1.country == "B"
    assert p1.priority == 1
    assert not p1.visited

    p1.mark_visited()
    assert p1.visited

    p1.mark_unvisited()
    assert not p1.visited

    assert p1.is_important() is True

    p2 = Place("C", "D", 3, False)
    assert p2.is_important() is False

    print("All tests passed")


test_place()