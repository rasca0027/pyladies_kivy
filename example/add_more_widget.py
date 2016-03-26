from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):

    def build(self):

        label = Label(text='Label')
        button = Button(text='Click')
        layout = BoxLayout()
        layout.add_widget(label)
        layout.add_widget(button)

        return layout


app = MyApp()
app.run()