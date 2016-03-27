# example/basic_widget.py
from __future__ import print_function
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton


class MyApp(App):

    def build(self):
        button = ToggleButton(text='PyLadies Rocks')

        button.on_press = lambda: print("yo")
        return button


app = MyApp()
app.run()