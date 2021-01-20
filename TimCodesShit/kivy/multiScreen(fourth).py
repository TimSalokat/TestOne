from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

#then it doesnt have to be the name of the app
kv = Builder.load_file("fourth.kv")

class fourthApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    fourthApp().run()