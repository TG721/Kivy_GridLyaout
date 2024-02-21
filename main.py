from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file('design.kv')


class MyLayout(Widget):
    button_1_var = ObjectProperty(None)  # initially those things won't have any value
    button_2_var = ObjectProperty(None)
    button_3_var = ObjectProperty(None)
    button_4_var = ObjectProperty(None)
    button_6_var = ObjectProperty(None)
    label_var = ObjectProperty(None)

    def pressed_button_1(self):
        label = "This is label"
        self.label_var.text = label + " of button 1"
    def pressed_button_2(self):
        label = "This is label"
        self.label_var.text = label + " of button 2"
    def pressed_button_3(self):
        label = "This is label"
        self.label_var.text = label + " of button 3"
    def pressed_button_4(self):
        label = "This is label"
        self.label_var.text = label + " of button 4"
    def pressed_button_5(self):
        label = "This is label"
        self.label_var.text = label + " of button 5"


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
