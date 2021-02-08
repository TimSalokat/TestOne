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
"""#possibilities for helper_text_mode = on_focus, on_error or persistent

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: "menu"
    MDRectangleFlatButton:
        text: "Profile"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        on_press: root.manager.current = "profile"
    MDRectangleFlatButton:
        text: "Upload"
        pos_hint: {"center_x":0.5, "center_y":0.4}
        on_press: root.manager.current = "upload"

<ProfileScreen>:
    name: "profile"
    MDLabel:
        text: "Welcome to the Profile"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "menu"

<UploadScreen>:
    name: "upload"
    MDLabel:
        text: "Upload files"
        halign: "center"
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "menu"
    
"""

navigation_helper="""
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"

                    MDToolbar: 
                        title: "Demonstration"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation: 11

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                spacing: "8dp"
                padding: "8dp"
                orientation: "vertical"

                MDLabel:
                    text: "Name"
                    font_style: "Subtitle1"
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
                            text: "Item1"
                            IconLeftWidget:
                                icon: "face-profile-woman"

                        OneLineIconListItem
                            text: "Item2"
                            IconLeftWidget:
                                icon: "file-upload"
                        
                        OneLineIconListItem:
                            text: "Item3"
                            IconLeftWidget:
                                icon: "logout"

"""