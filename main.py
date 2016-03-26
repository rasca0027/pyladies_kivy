from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.network.urlrequest import UrlRequest


APP_ID = 'YOUR API KEY'
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s'


class WeatherDashboard(BoxLayout):
    degree = NumericProperty(0)
    humid = NumericProperty(0)
    status = StringProperty('Clear') # Clear, Clouds, Rain, Mist

    def __init__(self, **kwargs):
        super(WeatherDashboard, self).__init__(**kwargs)
        req = UrlRequest(url % ('Taipei', APP_ID), self.got_weather)

    def got_weather(self, req, results):
        temp = results['main']['temp']
        self.degree = int(temp - 273)
        self.humid = results['main']['humidity']
        self.status = results['weather'][0]['main']


class MyApp(App):

    def build(self):
        return WeatherDashboard()


if __name__ == '__main__':
    MyApp().run()
