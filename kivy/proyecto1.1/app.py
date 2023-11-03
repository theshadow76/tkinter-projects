from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import numpy as np
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
import json
from matplotlib import pyplot as plt
import time

from kivy.lang import Builder

data = np.array({'username' : '', 'password' : ''})
dt = [{'username' : '', 'password' : ''}]

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #add widgets to window
        self.hello_world = Label(text="Say Hello", font_size = 50, color = "gold")
        self.window.add_widget(self.hello_world)

        self.btn_one = Button(text="Press Me", background_color = "red", pos=(12, 20)) 
        self.window.add_widget(self.btn_one)
        self.btn_one.bind(on_press = self.pressme)

        self.btn_two = Button(text="get data")
        self.window.add_widget(self.btn_two)
        self.btn_two.bind(on_press = self.getData)

        self.txt_one = TextInput(hint_text="Bien")
        self.window.add_widget(self.txt_one)

        return self.window

    def pressme(self, e):
        self.hello_world.text = "buenas"
        l1=[]
        l2=[]
        for i in range(0,50):
            i=i-5
            l1.append(i)
            i1=5*i-i*i
            l2.append(i1)
        plt.plot(l1,l2)
        plt.show()
    def getData(self, e):
        self.getdt = Label(text=str(self.txt_one.text))
        if (self.txt_one.text != ""):
            self.window.add_widget(self.getdt)
        else:
            self.txtx = Label(text="mal, mejor andate a la punta del zero. pon algo!")
            self.window.add_widget(self.txtx)


if __name__ == "__main__":
    SayHello().run()