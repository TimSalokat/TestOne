from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, IconLeftWidget, ThreeLineAvatarIconListItem, ImageLeftWidget #the 2 before are for custom images
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

global center
center = {"center_x":0.5, "center_y":0.5}

username_helper = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "or click forgot username"
    helper_text_mode: "on_focus"

    icon_right: "laptop"
    icon_right_color: app.theme_cls.primary_color

    pos_hint:{"center_x":0.5, "center_y":0.5}
    size_hint_x:None
    width:200
"""#possibilities for help

button_helper = """
MDRectangleFlatButton:
    text: "Submit"
    pos_hint: {"center_x":.5, "center_y":.4}
    on_release: app.show_input()
"""

class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.theme_style = "Light"

        screen = Screen()

        self.button = Builder.load_string(button_helper)
        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)
        screen.add_widget(self.button)

        return screen

    def show_input(self):
        print("Called")
        self.dialog = MDDialog(text=f"Hello", title="Username", size_hint=(0.6,1))
        self.dialog.open()
        if self.username.text != "":
            print(self.username.text)
            self.username.text = ""

TestApp().run()