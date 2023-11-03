import tkinter
import random
from tkinter import Tk

mycolorlist = None
v1=None

mycolorlist = ['black', '#212121', 'white', 'blue', 'green']
v1=random.choice(mycolorlist)

window = Tk()
window.geometry("500x500")
window.configure(bg=v1)



window.mainloop()