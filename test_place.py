"""
CP1404 Assignment 2
Place Class Unit Tests
"""
from place import Place

def run_tests():
    # Test 1: Default constructor
    place1 = Place()
    assert place1.name == ""
    assert place1.country == ""
    assert place1.priority == 0
    assert place1.visited is False

    # Test 2: Parameterized constructor
    place2 = Place("Paris", "France", 1, True)
    assert place2.name == "Paris"
    assert place2.country == "France"
    assert place2.priority == 1
    assert place2.visited is True

    # Test 3: __str__ method
    assert str(place2) == "Paris, France, priority 1 (visited)"
    assert str(place1) == ", , priority 0 (unvisited)"

    # Test 4: mark_visited and mark_unvisited methods
    place1.mark_visited()
    assert place1.visited is True
    place1.mark_unvisited()
    assert place1.visited is False

    # Test 5: is_important method
    assert place2.is_important() is True  # priority 1 <= 2
    place3 = Place("Sydney", "Australia", 3, False)
    assert place3.is_important() is False  # priority 3 > 2

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()