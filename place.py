"""
CP1404 Assignment 2
Place Class
Student: Qiuhao Wu
ID: 15136727
"""


class Place:
    def __init__(self, name="", country="", priority=0, visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        return f"{self.name} in {self.country} (priority {self.priority}) {'visited' if self.visited else 'unvisited'}"

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def is_important(self):
        return self.priority <= 2