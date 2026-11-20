"""
CP1404/CP5632 - Practical 08
Callum Bennett
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesApp(App):
    def build(self):
        Window.size = (500, 250)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesApp().run()