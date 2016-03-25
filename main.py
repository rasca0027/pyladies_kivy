from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
import requests

APP_ID = '93b4bc2c1a8637730962f114155febb5'

def get_weather(cityname):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s'
    r = requests.get(url % (cityname, APP_ID))
    r = r.json()
    temp = r['main']['temp']
    # convert to celcius degree
    degree = temp - 273
    humidity = r['main']['humidity']
    return int(degree), humidity


class WeatherDashboard(BoxLayout):
    degree = NumericProperty(0)
    humid = NumericProperty(0)
    location = StringProperty('Taipei')

    def __init__(self, **kwargs):
        super(WeatherDashboard, self).__init__(**kwargs)
        self.degree, self.humid = get_weather('Taipei')

    def change_location(self, cityname):
        self.location = cityname
        print cityname

class MyApp(App):

    def build(self):
        return WeatherDashboard()


if __name__ == '__main__':
    MyApp().run()
