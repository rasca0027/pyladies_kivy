from __future__ import print_function
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout


class PasswordCheck(BoxLayout):
    password = StringProperty("1234")
    message = StringProperty("")

    def validate(self, data):
        if self.password == data:
            self.message = "Correct"
        else:
            self.message = "Fail"


class SyncApp(App):
    pass


app = SyncApp()
app.run()