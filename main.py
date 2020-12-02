
from kivy import Config
from kivy.app import App
from kivymd.app import MDApp
Config.set('graphics','width','480')
Config.set('graphics','height','640')
#Config.set('kivy', 'keyboard_mode', 'systemanddock')
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.theming import ThemeManager
import json
from data import db
import os


class Login(Screen):
    def do_login(self, loginText, passwordText):
        if db.authentication(loginText, passwordText):
            print("authentication...")
            manager = TouristApp.get_screen_manager(self)
            manager.add_widget(Homepage(name='homepage'))
            manager.current = 'homepage'
        else:
            self.ids['wrong_data'].text = "Wrong password or login"
    def go_to_signup_page(self):
        manager=TouristApp.get_screen_manager(self)
        from models.sign_up import Signup
        manager.add_widget(Signup(name='signup'))
        manager.current = 'signup'

class Homepage(Screen):
    def __init__(self,**kvargs):
        super(Homepage, self).__init__(**kvargs)
        from models.location import location
        latitude,longitude,self.ids['current_location'].text =location.get_current_location()
        """
        from models.map import Map
        self.map=Map(zoom=8, lat=latitude,lon=longitude)
        x,y=self.map.get_window_xy_from(latitude,longitude,16)
        self.map.set_zoom_at(9,x,y)
        """
        #self.ids["map_container"].add_widget(map)
    def show_location(self):
        pass


class TouristApp(MDApp):

    def __init__(self,**kvargs):
        super(TouristApp, self).__init__(**kvargs)
        self.manager=None

    def build(self):

        self.load_all_kv_files("kivy_file")
        self.manager = ScreenManager()
        self.manager.add_widget(Login(name='login'))

        Window.size = (480, 640)

        return self.manager

    def load_all_kv_files(self, directory_kv_files):

         for kv_file in os.listdir(directory_kv_files):

             kv_file = os.path.join(directory_kv_files, kv_file)

             if os.path.isfile(kv_file):

                Builder.load_file(kv_file)


    def get_screen_manager(self):
       return self.manager
if __name__ == '__main__':
    TouristApp().run()
