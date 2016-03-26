from __future__ import print_function
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        button = Button(text='PyLadies Rocks',
                        font_size=40,
                        color=(0, 0, 254, 1),
                        background_color=(1, 0, 0, 1))

        button.on_press = lambda: print("yo")
        return button


app = MyApp()
app.run()