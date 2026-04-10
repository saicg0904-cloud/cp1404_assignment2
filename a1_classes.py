"""
CP1404 Assignment 2
Console Program
Student: Qiuhao Wu
ID: 15136727
"""
from place import Place
from placecollection import PlaceCollection

MENU = "L - List places\nA - Add new place\nM - Mark place as visited\nQ - Quit"


def main():
    print("Travel Tracker 2.0")
    collection = PlaceCollection()
    collection.load_places("places.json")
    print(f"Loaded {len(collection.places)} places.")

    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "L":
            list_places(collection)
        elif choice == "A":
            add_place(collection)
        elif choice == "M":
            mark_place(collection)
        elif choice == "Q":
            collection.save_places("places.json")
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


def list_places(collection):
    for i, place in enumerate(collection.places):
        visited = "*" if not place.visited else ""
        print(f"{i + 1}. {place.name:<15} {place.country:<15} {place.priority:<5} {visited}")
    unvisited = collection.get_unvisited_count()
    print(f"Places to visit: {unvisited}")


def add_place(collection):
    name = input("Name: ")
    country = input("Country: ")
    while True:
        try:
            priority = int(input("Priority: "))
            if priority < 1:
                print("Priority must be > 0")
                continue
            break
        except ValueError:
            print("Invalid number")
    collection.add_place(Place(name, country, priority, False))
    print(f"{name} added.")


def mark_place(collection):
    list_places(collection)
    try:
        choice = int(input("Enter place number: ")) - 1
        place = collection.places[choice]
        place.mark_visited()
        print(f"{place.name} marked as visited.")
    except (ValueError, IndexError):
        print("Invalid number")


if __name__ == '__main__':
    main()