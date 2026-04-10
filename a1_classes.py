"""
CP1404 Assignment 2
Console Version using Classes
"""
from place import Place
from placecollection import PlaceCollection
import random

MENU = """Menu:
L - List places
A - Add new place
M - Mark place as visited
R - Random place
Q - Quit"""


def main():
    print("Travel Tracker 2.0")
    collection = PlaceCollection()
    collection.load_places("places.json")
    print(f"Loaded {len(collection.places)} places from places.json")

    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "L":
            list_places(collection)
        elif choice == "A":
            add_place(collection)
        elif choice == "M":
            mark_visited(collection)
        elif choice == "R":
            random_place(collection)
        elif choice == "Q":
            collection.save_places("places.json")
            print(f"Saved {len(collection.places)} places to places.json")
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice")


def list_places(collection):
    if not collection.places:
        print("No places in the list!")
        return
    collection.sort("visited")
    print(f"{'Name':<20} {'Country':<15} {'Priority':<8} {'Visited':<8}")
    print("-" * 55)
    for i, place in enumerate(collection.places, 1):
        visited_mark = "*" if not place.visited else ""
        print(f"{i}. {place.name:<18} {place.country:<15} {place.priority:<8} {visited_mark}")
    print(f"\n{collection.get_unvisited_count()} places still to visit!")


def add_place(collection):
    name = input("Name: ").strip()
    while not name:
        print("Name cannot be blank!")
        name = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Country cannot be blank!")
        country = input("Country: ").strip()

    while True:
        try:
            priority = int(input("Priority: "))
            if priority < 1:
                print("Priority must be >= 1!")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number!")

    new_place = Place(name, country, priority, False)
    collection.add_place(new_place)
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker!")


def mark_visited(collection):
    unvisited_places = [p for p in collection.places if not p.visited]
    if not unvisited_places:
        print("No unvisited places!")
        return

    list_places(collection)
    while True:
        try:
            choice = int(input("Enter the number of the place to mark as visited: "))
            if 1 <= choice <= len(collection.places):
                place = collection.places[choice - 1]
                if place.visited:
                    print("That place is already visited!")
                else:
                    place.mark_visited()
                    print(f"{place.name} in {place.country} marked as visited!")
                    break
            else:
                print("Invalid place number!")
        except ValueError:
            print("Invalid input; enter a valid number!")


def random_place(collection):
    if not collection.places:
        print("No places in the list!")
        return
    place = random.choice(collection.places)
    print(f"Random place: {place.name} in {place.country} (priority {place.priority})")


if __name__ == "__main__":
    main()