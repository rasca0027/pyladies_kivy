# example/add_more_widget.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):

    def build(self):

        left = Button(text='left')
        right = Button(text='right')

        layout = BoxLayout()

        layout.add_widget(left)
        layout.add_widget(right)

        return layout


app = MyApp()
app.run()