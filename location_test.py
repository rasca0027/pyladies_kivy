from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty


class Location(BoxLayout):
    
    def press_btn(self, cityname):
        print cityname

class LocateApp(App):

    def build(self):
        return Location()


if __name__ == '__main__':
    LocateApp().run()
