
from kivy.lang import Builder
from kivymd.app import MDApp

string = """
Screen:
    MDLabel:
        text: "Hello"
"""

class myApp(MDApp):
    def build(self):
        return Builder.load_string(string)

myApp().run()