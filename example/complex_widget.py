# examples/complex_widget.py
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class FormInput(BoxLayout):
    label_text = StringProperty("")


class CWApp(App):
    pass

CWApp().run()
