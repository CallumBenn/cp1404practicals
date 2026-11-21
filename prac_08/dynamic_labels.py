"""
CP1404/CP5632 - Practical 08
Callum Bennett
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red

class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Callum Bennett"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        return self.root

    def create_label(self):
        """Create label for each string in list."""
        for name in self.names:
            label = Label(text=str(name))
            self.root.ids.main.add_widget(label)

DynamicLabelsApp().run()