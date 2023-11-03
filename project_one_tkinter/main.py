import tkinter
from tkinter import Button, Tk
from typing import overload
import webbrowser

window = Tk()
window.geometry("800x800")
window.configure(bg="grey")

def instagram():
    webbrowser.open("https://www.instagram.com/")

go_to_instagram = Button(window, text="instagram", command=instagram)
go_to_instagram.pack()

window.mainloop()

