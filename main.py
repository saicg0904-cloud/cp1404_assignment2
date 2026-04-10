"""
CP1404 Assignment 2
Kivy GUI Main Program
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from place import Place
from placecollection import PlaceCollection

Builder.load_file('app.kv')

class TravelTrackerApp(App):
    def build(self):
        self.collection = PlaceCollection()
        self.collection.load_places("places.json")
        self.title = "Travel Tracker 2.0"

        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Status label
        self.status_label = Label(text=f"{self.collection.get_unvisited_count()} places to visit!", size_hint=(1, 0.1))
        self.main_layout.add_widget(self.status_label)

        # Places list layout
        self.places_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.7))
        self.update_places_list()
        self.main_layout.add_widget(self.places_layout)

        # Input layout for adding new place
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)
        self.name_input = TextInput(hint_text="Name", size_hint=(0.3, 1))
        self.country_input = TextInput(hint_text="Country", size_hint=(0.3, 1))
        self.priority_spinner = Spinner(text="1", values=[str(i) for i in range(1, 6)], size_hint=(0.2, 1))
        add_button = Button(text="Add Place", size_hint=(0.2, 1), on_press=self.add_place)
        input_layout.add_widget(self.name_input)
        input_layout.add_widget(self.country_input)
        input_layout.add_widget(self.priority_spinner)
        input_layout.add_widget(add_button)
        self.main_layout.add_widget(input_layout)

        return self.main_layout

    def update_places_list(self):
        self.places_layout.clear_widgets()
        self.collection.sort("visited")
        for i, place in enumerate(self.collection.places, 1):
            visited_mark = "*" if not place.visited else ""
            btn = Button(
                text=f"{i}. {place.name} - {place.country} (Priority {place.priority}) {visited_mark}",
                size_hint=(1, None),
                height=40
            )
            btn.bind(on_press=lambda instance, p=place: self.mark_visited(p))
            self.places_layout.add_widget(btn)
        self.status_label.text = f"{self.collection.get_unvisited_count()} places to visit!"

    def mark_visited(self, place):
        if not place.visited:
            place.mark_visited()
            self.collection.save_places("places.json")
            self.update_places_list()

    def add_place(self, instance):
        name = self.name_input.text.strip()
        country = self.country_input.text.strip()
        priority = int(self.priority_spinner.text)
        if name and country:
            new_place = Place(name, country, priority, False)
            self.collection.add_place(new_place)
            self.collection.save_places("places.json")
            self.update_places_list()
            self.name_input.text = ""
            self.country_input.text = ""

    def on_stop(self):
        self.collection.save_places("places.json")

if __name__ == "__main__":
    TravelTrackerApp().run()