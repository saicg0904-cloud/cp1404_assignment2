"""
CP1404 Assignment 2
PlaceCollection Class Unit Tests
"""
from placecollection import PlaceCollection
from place import Place
import json
import os

def run_tests():
    # Test 1: Default constructor
    collection = PlaceCollection()
    assert len(collection.places) == 0

    # Test 2: add_place method
    place1 = Place("Paris", "France", 1, True)
    place2 = Place("Tokyo", "Japan", 2, False)
    collection.add_place(place1)
    collection.add_place(place2)
    assert len(collection.places) == 2

    # Test 3: get_unvisited_count method
    assert collection.get_unvisited_count() == 1  # Only Tokyo is unvisited

    # Test 4: sort method
    collection.sort("priority")
    assert collection.places[0].name == "Paris"  # priority 1 comes first
    collection.sort("name")
    assert collection.places[0].name == "Paris"  # Alphabetical order

    # Test 5: save_places and load_places
    test_file = "test_places.json"
    collection.save_places(test_file)
    # Verify file content
    with open(test_file, 'r') as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]["name"] == "Paris"

    # Load into new collection
    new_collection = PlaceCollection()
    new_collection.load_places(test_file)
    assert len(new_collection.places) == 2
    assert new_collection.places[0].name == "Paris"

    # Clean up test file
    os.remove(test_file)

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()