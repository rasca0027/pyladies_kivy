# examples/custom_widget.py
from kivy.app import App
from kivy.uix.label import Label


class PriceLabel(Label):
    color = (1,0,0,1)


class CApp(App):
    pass

CApp().run()
