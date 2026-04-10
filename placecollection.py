"""
CP1404 Assignment 2
PlaceCollection Class
Student: Qiuhao Wu
ID: 15136727
"""
import json
from place import Place


class PlaceCollection:
    def __init__(self):
        self.places = []

    def load_places(self, filename):
        self.places = []
        with open(filename) as file:
            data = json.load(file)
            for item in data:
                place = Place(item["name"], item["country"], item["priority"], item["visited"])
                self.places.append(place)

    def save_places(self, filename):
        data = [{"name": p.name, "country": p.country, "priority": p.priority, "visited": p.visited} for p in
                self.places]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

    def add_place(self, place):
        self.places.append(place)

    def get_unvisited_count(self):
        return sum(1 for p in self.places if not p.visited)

    def sort(self, key):
        self.places.sort(key=lambda x: getattr(x, key))