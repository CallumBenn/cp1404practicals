"""
CP1404/CP5632 - Practical 08
Callum Bennett
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

INVALID_INPUT_WARNING = "Invalid input!"

class ConvertMilesApp(App):
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 250)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation, output result to label."""
        try:
            result = float(value) * 1.60934 # Convert miles to kilometres
            self.message = str(result)
            print("Calculated!")
        except ValueError:
            self.message = INVALID_INPUT_WARNING

    # def handle_update(self):
    #     """Handle changes to the text input by updating the model from the view."""
    #     self.message = self.root.ids.input_number.text

    def add_miles(self, value):
        try:
            result = float(value) + 1
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.message = INVALID_INPUT_WARNING

    def subtract_miles(self, value):
        try:
            result = float(value) - 1
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.message = INVALID_INPUT_WARNING


ConvertMilesApp().run()