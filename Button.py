from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
#from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        spacing = 20
        paddind = 40
        rec_btn = MDRectangleFlatButton(text="hello world",
                                pos_hint={"center_x": .5, "center_y": 0.7})
        rect_btn1 = MDRectangleFlatButton(text= "hello world", 
                                          pos_hint= {"center_x": .5, "center_y": .5})
        screen.add_widget(rec_btn)  # Use screen instance to add the widget
        screen.add_widget(rect_btn1)
        return screen  # Return the screen instance, not the class

if __name__ == "__main__":
    DemoApp().run()
