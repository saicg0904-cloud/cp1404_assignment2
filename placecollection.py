"""
CP1404 Assignment 2
PlaceCollection Class
"""
import json
from place import Place


class PlaceCollection:
    def __init__(self):
        self.places = []

    def load_places(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    place = Place(item["name"], item["country"], item["priority"], item["visited"])
                    self.places.append(place)
        except FileNotFoundError:
            pass

    def save_places(self, filename):
        data = []
        for place in self.places:
            data.append({
                "name": place.name,
                "country": place.country,
                "priority": place.priority,
                "visited": place.visited
            })
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def add_place(self, place):
        self.places.append(place)

    def get_unvisited_count(self):
        return len([p for p in self.places if not p.visited])

    def sort(self, key):
        self.places.sort(key=lambda x: (getattr(x, key), x.priority))