from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config

# Set window size to 340x640
Config.set('graphics', 'width', '340')
Config.set('graphics', 'height', '640')

class MyApp(MDApp):
    def build(self):
        # Create the main layout (replace with appropriate layout)
        main_layout = GridLayout(cols=3, rows=2)  # Use GridLayout instead of MDGridLayout

        # Add buttons based on their positions in the image
        button1 = MDRectangleFlatButton(
            text="enter your full name",
            pos_hint={"center_x": 0.4, "center_y": 0.1},  # Set column and row positions
            size_hint=(0.5, 0.2),  # Set width and height proportions
            theme_text_color="Primary",  # Use a valid option
            text_color=(0, 0, 0, 1),
            md_bg_color=(0, 150/255, 136/255, 1),  # Green background
            font_style="H5",  # Font size 25 (adjust as needed)
            on_release=self.button1_click  # Set callback function
        )
        button2 = MDRectangleFlatButton(
            text="enter your email",
            pos_hint={"center_x": 0.5, "center_y": 0.2},  # Fix typo in 'center_y'
            size_hint=(0.6, 0.2),
            theme_text_color="Primary",  # Use a valid option
            text_color=(0, 0, 0, 1),
            md_bg_color=(0, 150/255, 136/255, 1),
            font_style='H5',
            on_release=self.button2_click
        )
        main_layout.add_widget(button1)
        main_layout.add_widget(button2)

        # Repeat for other buttons, adjusting text, positions, and callbacks

        return main_layout

    # Define callback functions for button clicks
    def button1_click(self, instance):
        # Actions for button 1 click
        pass

    def button2_click(self, instance):
        # Actions for button 2 click
        pass

    # Add callback functions for other buttons

if __name__ == "__main__":
    MyApp().run()
