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