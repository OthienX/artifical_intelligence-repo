import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChildApp(GridLayout):
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Student Name"))
        self.s_name = TextInput()
        self.add_widget(self.s_name)  # Use add_widget to add TextInput to the layout
        self.add_widget(Label(text="Student Marks"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)  # Use add_widget to add TextInput to the layout
        self.add_widget(Label(text="Student Gender"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)  # Use add_widget to add TextInput to the layout

        self.press = Button(text="Click me")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name of student is " + self.s_name.text)
        print("Marks of student are " + self.s_marks.text)
        print("Gender of student is " + self.s_gender.text)
        print("")

class ParentApp(App):
    def build(self):
        return ChildApp()

if __name__ == "__main__":
    ParentApp().run()
