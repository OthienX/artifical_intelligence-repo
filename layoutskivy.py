import kivy 
from kivy.app import App 
from kivy.lang import Builder 

root = Builder.load_string('''
FloatLayout:
     canvas.before:
     color:
          rgba: 0, 1, 0, 1
     Rectangle:
         pos:self.pos
         size: self.size
     Button:
         text: 'hello world!'
         size_hint: .5, .5
         pos_hint: {'center_x': .5, 'center_y':.5}                  
                          ''' )
class  Baddest(App):
    
    def build(self):
        return root
if __name__=='__main__':
    Baddest().run()    