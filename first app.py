import kivy
from kivy.app import App
from kivy.uix.label import Label

class baddest(App):
    def build(self):
        return Label(text = "hellow world")
if __name__=="__main__":
    baddest().run()
        