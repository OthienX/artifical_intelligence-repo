from kivy.uix.widget import Widget
from kivy.app import App
from kivy.graphics import Ellipse, Color

class othi(Widget):
    
    def __init__(self, **kwargs):
        super(othi, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()  # Call the method here

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0.5, 0.8, 0.9, 0.5)
            Ellipse(pos=self.pos, size=self.size)

class MyApp(App):
    def build(self):
        return othi()

if __name__ == "__main__":
    MyApp().run()
