# example/widget_trial_with_size.py
# https://kivy.org/docs/api-kivy.uix.widget.html
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        button = Button(text='PyLadies Rocks',
                        size_hint_x=0.9,
                        size_hint_y=0.5,
                        pos_hint={'x': 0.05, 'y':0.25},
                        font_size=40,
                        background_color=(1, 0, 0, 1))

        return button


app = MyApp()
app.run()