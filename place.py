"""
CP1404 Assignment 2
Place Class for Travel Tracker
Student: Qiuhao Wu
ID: 15136727
"""

class Place:
    def __init__(self, name="", country="", priority=0, visited=False):
        """Initialize a Place with name, country, priority, and visited status."""
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        """Return string representation of a Place."""
        return f"{self.name} in {self.country} (priority {self.priority}) {'visited' if self.visited else 'unvisited'}"

    def mark_visited(self):
        """Mark the place as visited."""
        self.visited = True

    def mark_unvisited(self):
        """Mark the place as unvisited."""
        self.visited = False

    def is_important(self):
        """Return True if the place is important (priority <= 2)."""
        return self.priority <= 2