from KivyMd1Helpers import username_helper
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivy.lang import Builder

global center
center = {"center_x":0.5, "center_y":0.5}

#Labels and Icons with options
# class TestApp(MDApp):
#     def build(self):
#         label = MDLabel(text="Hello World!", halign="center", theme_text_color="Custom", text_color=(0.5,0.4,1,1),
#                         font_style="H3")

#         icon_label = MDIcon(icon="laptop", halign="center", theme_text_color="Hint")
#         return icon_label 

#Buttons
# class TestApp(MDApp):
#     def build(self):
#         screen = Screen()

#         button_flat = MDRectangleFlatButton(text="Hello World!", pos_hint={"center_x":0.5,"center_y":0.5})

#         icon_btn = MDFloatingActionButton(icon="airplay", pos_hint={"center_x":0.5,"center_y":0.5})

#         screen.add_widget(icon_btn)
#         return screen

#Themes and colors
# class TestApp(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Purple"
#         #Hue is smth like the saturation
#         self.theme_cls.primary_hue = "700"
#         #there is only Light and Dark
#         self.theme_cls.theme_style = "Dark"

#         screen = Screen()
#         btn_flat = MDRectangleFlatButton(text="Hello World", pos_hint={"center_x":0.5, "center_y":0.5})

#         screen.add_widget(btn_flat)
#         return screen


class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.theme_style = "Light"

        screen = Screen()

        button = MDRectangleFlatButton(text="Submit", pos_hint={"center_x":0.5, "center_y":0.4},
                                        on_release=self.show_input)
        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)
        screen.add_widget(button)

        return screen

    def show_input(self, obj):
        print(self.username.text)
        self.username.text = ""




TestApp().run()