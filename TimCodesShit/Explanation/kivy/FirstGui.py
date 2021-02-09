from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

Window.size = (300,500)


KV = """
<Box@MDBoxLayout>
    bg: 0,0,0,0

    canvas:
        Color:
            rgba: root.bg
        Rectangle:
            pos: self.pos
            size: self.size


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    ScrollView:

        MDList:

            OneLineIconListItem:
                text: "Chat"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.transition.direction = "down"
                    root.screen_manager.current = "Chat"
                IconLeftWidget:
                    icon: "chat"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.transition.direction = "down"
                        root.screen_manager.current = "Chat"

            OneLineIconListItem:
                text: "To-Do"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.transition.direction = "down"
                    root.screen_manager.current = "Todo"
                IconLeftWidget:
                    icon: "checkbox-marked-circle-outline"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.transition.direction = "down"
                        root.screen_manager.current = "Todo"

            OneLineIconListItem:
                text: "Devices"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.transition.direction = "down"
                    root.screen_manager.current = "Devices"
                IconLeftWidget:
                    icon: "devices"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.transition.direction = "down"
                        root.screen_manager.current = "Devices"
            
            OneLineIconListItem:
                text: "Tilih"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.transition.direction = "down"
                    root.screen_manager.current = "Tilih"
                IconLeftWidget:
                    icon: "console-line"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.transition.direction = "down"
                        root.screen_manager.current = "Tilih"

    MDList:
        OneLineIconListItem:
            text: "Logout"
        

Screen:

    ScreenManager:
        id: screen_manager

        Screen:
            name: "Home"
            
            MDBoxLayout:
                orientation: "vertical"

                MDToolbar:
                    title: "Main"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                Widget:
        
        Screen:
            name: "Chat"

            MDBoxLayout:
                orientation: "vertical"

                MDToolbar:
                    title: "Chat"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                Box:
                    bg: 177/255,230/255,229/255,.7
                    ScrollView:
                            
                        MDLabel:
                            id: ChatBox
                            text: "Text"
                Box:
                    bg: 177/255,230/255,229/255,.7
                    adaptive_height: True

                    MDTextField:
                        multiline: True
                        mode: "rectangle"
                        mode: "fill"
                        fill_color: 177/255,230/255,229/255,.5
                        hint_text: "Input"
                            
                    MDFloatingActionButton:
                        md_bg_color: app.theme_cls.primary_color
                        icon: "send"

                       
        
        Screen:
            name: "Todo"

            MDBoxLayout:
                orientation: "vertical"

                MDToolbar:
                    title: "To-Do"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                Widget:

                MDList:
                    OneLineListItem:
                        text: "Hi"

        Screen:
            name: "Devices"

            MDBoxLayout:
                orientation: "vertical"

                MDToolbar:
                    title: "Devices"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                Widget:

        Screen:
            name: "Tilih"
            
            MDBoxLayout:
                orientation: "vertical"

                MDToolbar:
                    title: "Tilih"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        orientation: "vertical"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: None, None

            Image:
                id: avatar
                size_hint: None, None
                size: "100dp", "100dp"
                source: "nyan.png"

            MDBoxLayout:
                orientation: "vertical"
                size_hint: None, None
                padding: "10dp"
                spacing: "10dp"

                MDLabel:
                    text: "Name: "
                    font_style: "Button"
                    theme_text_color: "Custom"
                    text_color: 1,1,1
                    size_hint_y: None
                    height: self.texture_size[1]
                
                MDLabel:
                    text: "Permission: "
                    theme_text_color: "Custom"
                    text_color: 1,1,1
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
            
"""


class DrawerList():
    pass

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "800" 
        self.theme_cls.theme_style = "Dark"

        return Builder.load_string(KV)

def babafunktion(self,obj):
    print("hello")

MainApp().run()