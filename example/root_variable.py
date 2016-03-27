# examples/root.py  && root.kv
from kivy.app import App
from kivy.properties import StringProperty


class RootApp(App):
    data = StringProperty("sample")


RootApp().run()