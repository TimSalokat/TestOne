from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (300,500)


#-----Different color backgrounds-----
# from kivy.uix.screenmanager import Screen
# from kivymd.uix.button import MDRectangleFlatButton

# KV = """
# <Box@BoxLayout>
#     bg: 0,0,0,0

#     canvas:
#         Color:
#             rgba: root.bg
#         Rectangle:
#             pos: self.pos
#             size: self.size
# BoxLayout:
#     Box:
#         bg: app.theme_cls.bg_light
#     Box:
#         bg: app.theme_cls.bg_normal
#     Box:
#         bg: app.theme_cls.bg_dark
#     Box:
#         bg: app.theme_cls.bg_darkest

# """

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Light"
#         return Builder.load_string(KV)
#----------------------------------------------------

#-----Floating plus button (position hint for phone)-----
# KV="""
# Screen:
#     MDFloatingActionButton:
#         icon: "plus"
#         md_bg_color: app.theme_cls.primary_color
#         elevation_normal: 10
#         pos_hint: {"center_x":.8, "center_y": .1}
#         size_hint_x: None
#         width: 60
# """
#------------------------------------------------------


#-----Hopefully navigation drawers-----
from kivy.uix.boxlayout import BoxLayout
KV = """
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "100dp", "100dp"
            source: "nyan.png"
    
    MDLabel:
        text: "Name"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
    
    MDLabel:
        text: "Mail"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
    
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: "Hello"
                IconLeftWidget:
                    icon: "laptop"
        

Screen:
    ScreenManager:
        Screen:
            BoxLayout:
                orientation: "vertical"
                MDToolbar:
                    title: "Navigation Drawer"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                Widget:
    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            
"""
class DrawerList():
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)




















MainApp().run()