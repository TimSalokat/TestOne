from KivyMd1Helpers import username_helper
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, IconLeftWidget, ThreeLineAvatarIconListItem, ImageLeftWidget #the 2 before are for custom images
from kivy.uix.scrollview import ScrollView

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

#---UserInput---
# class TestApp(MDApp):

#     def build(self):
#         self.theme_cls.primary_palette = "Purple"
#         self.theme_cls.primary_hue = "300"
#         self.theme_cls.theme_style = "Light"

#         screen = Screen()

#         button = MDRectangleFlatButton(text="Submit", pos_hint={"center_x":0.5, "center_y":0.4},
#                                         on_release=self.show_input)
#         self.username = Builder.load_string(username_helper)

#         screen.add_widget(self.username)
#         screen.add_widget(button)

#         return screen

#     def show_input(self, obj):

#         if self.username.text == "":
#             check_string = "Please enter a username"
#         else:
#             check_string = self.username.text + " does not exist"

#         close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
#         more_button = MDFlatButton(text="more")

#         self.dialog = MDDialog(text=f"{check_string}", title="Username", size_hint=(0.6,1), buttons=[close_button, more_button])
#         self.dialog.open()

#         print(self.username.text)
#         self.username.text = ""
    
#     def close_dialog(self,obj):
#         self.dialog.dismiss()
#---end user input---

#hard coded lists
# class TestApp(MDApp):
    
#     def build(self):

#         screen = Screen()
#         scroll_view = ScrollView()
#         list_view = MDList()

#         for _ in range(10):
#             #image = ImageLeftWidget(source="example.png")
#             icon = IconLeftWidget(icon="laptop")
#             items = ThreeLineIconListItem(text=f"Item {_ + 1}", secondary_text="Description", tertiary_text="More text")
#             list_view.add_widget(items) 

#             items.add_widget(icon)#or image


#         scroll_view.add_widget(list_view)
#         screen.add_widget(scroll_view)

#         return screen


#string lists with ids
# list_helper = """
# Screen:
#     ScrollView:
#         MDList:
#             id: container

# """

# class TestApp(MDApp):
#     def build(self):
#         screen = Builder.load_string(list_helper)

#         return screen

#     def on_start(self):
#         for _ in range(20):
#             items = OneLineListItem(text=f"Item {_ + 1}")
#             self.root.ids.container.add_widget(items)


screen_helper = """
Screen:
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Demo"
        MDLabel:
            text: "Hello world!"
            halign: "center"
"""

class TestApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)

        return screen



TestApp().run()