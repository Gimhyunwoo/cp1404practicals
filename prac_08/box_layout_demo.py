from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemoApp(App):
    def build(self):
        self.title = "BoxLayout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""
