import pygame
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


#Class holding the design stuff
class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(f"Name:{self.name.text}, Email: {self.email.text}")
        self.name.text = self.email.text = ""


#First app definition
class FirstApp(App):
    def build(self):
        return MyGrid()


#run the code
if __name__ == "__main__":
    FirstApp().run()