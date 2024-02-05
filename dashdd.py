from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window

class MyApp(MDApp):
    def build(self):
        # Adjusted window size for a typical mobile app
        Window.size = (360, 640)  # Portrait orientation (adjust as needed)

        button = MDRectangleFlatButton(
            text="Get Started",
            pos_hint={"center_x": 0.5, "y": 0.1},  # Position at middle bottom
            size_hint=(0.8, 0.2),  # Adjust width and height proportions
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),  # Black text color
            md_bg_color=(0, 150/255, 136/255, 1),  # Green background color
            font_style='H5',  # Font size 25
            on_release=self.show_other_interface
        )
        return button

    def show_other_interface(self, instance):
        # Replace this placeholder with code to display the other interface
        print("Button clicked! Displaying other interface...")

if __name__ == "__main__":
    MyApp().run()
