from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextFieldRound


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("boxLayout.kv")  # Load the login.kv file

    def logger(self):
        self.root.ids.welcome_label.text = f"Sup {self.root.ids.user.text}!"

    def clear(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

if __name__ == "__main__":
    MainApp().run()
