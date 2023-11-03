from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout

class Tab(TabbedPanel):
    pass

class TestApp(App):
    def build(self):
        self.windows = GridLayout
        self.windows.cols = 1


        return self.windows
if __name__ == "__main__":
    TestApp().run()