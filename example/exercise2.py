from kivy.app import App
from kivy.properties import StringProperty, NumericProperty


class Exercise2App(App):
    message = StringProperty("")
    count = NumericProperty(0)

    def to_press(self):
        self.count += 1
        self.message = str(self.count)


Exercise2App().run()






