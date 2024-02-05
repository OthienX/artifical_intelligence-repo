import kivy
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen

class NameEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = dp(10)

        self.label = Label(text="Enter your name:", size_hint_y=None, height=dp(40),
                           font_size=15, halign="center")
        self.add_widget(self.label)

        self.input = TextInput(size_hint_y=None, height=dp(40), multiline=False)
        self.add_widget(self.input)

        self.button = MDRaisedButton(text="Submit", size_hint_y=None, height=dp(40),
                                     on_press=self.submit_name)
        self.add_widget(self.button)

    def submit_name(self, instance):
        name = self.input.text
        print(f"User entered name: {name}")
        # You can do something with the entered name, like storing it or displaying it.

class MyScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = dp(10)

        self.button_full_name = MDRaisedButton(
            text="Full Name",
            pos_hint={"center_x": 0.5, "y": 0.1},
            size_hint=(0.8, 0.2),
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            md_bg_color=(0, 150/255, 136/255, 1),
            font_size=15,
            on_press=self.show_name_entry_screen
        )
        self.add_widget(self.button_full_name)

        self.button_email_password = MDRaisedButton(
            text="Enter your email password",
            pos_hint={"center_x": 0.6, "center_y": 0.2},
            size_hint=(0.4, 0.6),
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            md_bg_color=(0, 150/255, 136/255, 1),
            font_size=15,
            on_press=self.show_name_entry_screen
        )
        self.add_widget(self.button_email_password)

    def show_name_entry_screen(self, instance):
        name_entry_screen = NameEntryScreen()
        self.parent.add_widget(name_entry_screen)
        self.parent.current = "name_entry_screen"

class MyApp(App):
    def build(self):
        root = ScreenManager()
        main_screen = MyScreen()
        name_entry_screen = NameEntryScreen(name='name_entry_screen')
        root.add_widget(main_screen)
        root.add_widget(name_entry_screen)
        return root

if __name__ == "__main__":
    MyApp().run()
