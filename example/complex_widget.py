# examples/complex_widget.py, cw.kv
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class FormInput(BoxLayout):
    label_text = StringProperty("")


class CWApp(App):
    pass

CWApp().run()
