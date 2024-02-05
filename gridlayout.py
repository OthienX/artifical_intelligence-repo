from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Baddest(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40,
                            spacing=40, padding=10)
        self.weight = TextInput(text="enter weight")
        self.height = TextInput(text="enter the height")
        submit = Button(text="submit", on_press=self.submit)
        layout.add_widget(self.height)
        layout.add_widget(self.weight)
        layout.add_widget(submit)
        return layout

    def submit(self, obj):
        print("weight:" + self.weight.text)
        print("height:" + self.height.text)

if __name__ == "__main__":
    Baddest().run()
