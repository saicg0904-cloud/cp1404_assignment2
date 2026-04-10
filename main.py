"""
CP1404 Assignment 2
GUI Program
Student: Qiuhao Wu
ID: 15136727
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from place import Place
from placecollection import PlaceCollection


class TravelApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collection = PlaceCollection()
        self.collection.load_places("places.json")

    def build(self):
        self.title = "Travel Tracker 2.0"
        self.root = Builder.load_file("app.kv")
        self.update_places()
        return self.root

    def update_places(self):
        self.root.ids.place_layout.clear_widgets()
        for place in self.collection.places:
            btn = Button(text=f"{place.name} - {place.country}")
            if place.visited:
                btn.background_color = 0.5, 1, 0.5, 1
            else:
                btn.background_color = 1, 0.7, 0.7, 1
            btn.bind(on_press=lambda x, p=place: self.toggle_place(p))
            self.root.ids.place_layout.add_widget(btn)
        self.root.ids.status_label.text = f"Places to visit: {self.collection.get_unvisited_count()}"

    def toggle_place(self, place):
        place.visited = not place.visited
        if place.visited:
            if place.is_important():
                self.root.ids.message_label.text = f"You visited {place.name}. Great travelling!"
            else:
                self.root.ids.message_label.text = f"You visited {place.name}."
        else:
            if place.is_important():
                self.root.ids.message_label.text = f"You need to visit {place.name}. Get going!"
            else:
                self.root.ids.message_label.text = f"You need to visit {place.name}."
        self.update_places()
        self.collection.save_places("places.json")

    def add_new_place(self):
        name = self.root.ids.name_input.text.strip()
        country = self.root.ids.country_input.text.strip()
        priority_str = self.root.ids.priority_input.text.strip()

        if not name or not country or not priority_str:
            self.root.ids.message_label.text = "All fields must be completed"
            return

        try:
            priority = int(priority_str)
            if priority < 1:
                self.root.ids.message_label.text = "Priority must be > 0"
                return
        except ValueError:
            self.root.ids.message_label.text = "Please enter a valid number"
            return

        self.collection.add_place(Place(name, country, priority, False))
        self.collection.save_places("places.json")
        self.update_places()
        self.clear_inputs()
        self.root.ids.message_label.text = f"Added {name}"

    def clear_inputs(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
        self.root.ids.message_label.text = ""

    def sort_places(self):
        key = self.root.ids.sort_spinner.text
        self.collection.sort(key)
        self.update_places()


if __name__ == '__main__':
    TravelApp().run()