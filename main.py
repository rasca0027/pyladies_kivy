from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class WeatherDashboard(BoxLayout):
    pass


class MyApp(App):

    def build(self):
        return WeatherDashboard()


if __name__ == '__main__':
    MyApp().run()
