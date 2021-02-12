import pygame
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


#First app definition
class SecondApp(App):
    def build(self):
        return FloatLayout()


#run the code
if __name__ == "__main__":
    SecondApp().run()