# examples/kv_to_python.py  && kv2py.kv
from kivy.app import App
from kivy.properties import StringProperty


class Kv2PyApp(App):
    data = StringProperty("sample")

    def what(self):
        import datetime
        self.data = str(datetime.datetime.now())

Kv2PyApp().run()