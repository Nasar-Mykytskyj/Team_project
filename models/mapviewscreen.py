from kivy.uix.screenmanager import Screen
from models.map import map

class MapScreen(Screen):
    def __init__(self):
        self.add_widget(map)
    pass
