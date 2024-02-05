from kivy.tests.common import GraphicUnitTest
import pytest

class MyTestCase(GraphicUnitTest):
     def test_runtouchapp(self):
         from kivy.app import runTouchApp
         from kivy.uix.button import Button
         button = Button()
         runTouchApp(button)
         
         from kivy.base import EventLoop
         EventLoop.ensure_window()
         window = EventLoop.window
         
         self.assertEqual(window.children[0], button)
         self.assertEqual(window.children[0], button)
         self.assertEqual(
         window.children[0].height,
         window.height
        )

