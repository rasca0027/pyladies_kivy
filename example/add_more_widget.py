import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        l1 = Label(text='Hello world 1')
        l2 = Label(text='Hello world 2')
        layout = BoxLayout()
        layout.add_widget(l1)
        layout.add_widget(l2)
        return layout


MyApp().run()