import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 


class Baddest(GridLayout):
    
    def __init__(self, **kwargs):
        super(Baddest, self).__init__(**kwargs)
        self.cols = 2
        self.padding = [10, 10]
        self.spacing = [10, 10]
        
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
        self.add_widget(Label(text="Password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        return Baddest()


if __name__ == "__main__":
    MyApp().run()
