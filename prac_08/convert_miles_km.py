from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.output_text = "0.0 km"
        return Builder.load_file("convert_miles_km.kv")

    def handle_convert(self):
        miles = self.get_valid_number()
        km = miles * MILES_TO_KM
        self.output_text = f"{km:.3f} km"

    def handle_increment(self, change):
        try:
            current = float(self.root.ids.input_miles.text)
        except ValueError:
            current = 0.0
        new_value = current + change
        self.root.ids.input_miles.text = str(new_value)
        self.handle_convert()

    def g
