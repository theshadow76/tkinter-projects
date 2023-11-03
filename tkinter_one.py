import builtins
import tkinter
from tkinter import Button, Grid, Image, PanedWindow, PhotoImage, Text, Tk, image_types, messagebox
from tkinter.constants import BUTT, CENTER, COMMAND, LEFT, TOP
from PIL import Image,ImageTk
import subprocess
from subprocess import call
import webbrowser
import os

TK_SILENCE_DEPRECATION=1

window = Tk()
window.resizable()
window.geometry("800x800")
window.configure(bg="grey")
window.title('ShadowNS')


''''
# Icon
photo_icon_btn = PhotoImage(file = r"/Users/vigowalker/Downloads/instagram.png")
img = (Image.open('/Users/vigowalker/Downloads/instagram.png'))
btn_icon = Button(window, image = photo_icon_btn, width=350, height=350)
resized_image= img.resize((10,10), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
btn_icon.pack(side=LEFT, padx=10, pady=10)
'''

'''
#panel 2
p1_1 = PanedWindow(window, bg="Black", width=10000, height=120)
p1_1.pack(side=TOP, padx=0, pady=0)

#panel 1
p1 = PanedWindow(window, bg="Black", width=120, height=10000, )
p1.pack(side=LEFT, padx=0, pady=0)
'''

#setings for open new windows
#login = call(["python", "/Users/vigowalker/Library/Mobile Documents/com~apple~CloudDocs/coding/python/tkinter_one_login.py"])
#send_email = call(['python', '/Users/vigowalker/Library/Mobile Documents/com~apple~CloudDocs/coding/python/tkinter_one_email.py'])

# Mode to be set 
mode = 0o666
  
# flags
flags = os.O_RDWR | os.O_CREAT

login = os.open('/Users/vigowalker/Library/Mobile Documents/com~apple~CloudDocs/coding/python/tkinter_one_login.py', flags, mode)

#los defs
#opens instagram
def go_to_instagram():
    webbrowser.open('https://www.instagram.com/vigo_walker')
#login
def Login():
    login_yesno = messagebox.askquestion("Login","quieres registrarte en esta app? diga si si quieres registrarse, diga no si quieres registrarse desde google")
    while (login_yesno == messagebox.YES):
        login
        break
#opens youtube
def go_to_youtube():
    webbrowser.open('https://www.youtube.com/channel/UCQOcFQcVfL4uQIVj7bf-PuQ')
#opens instagram from photo
def open_instagram():
    webbrowser.open('https://www.instagram.com/vigo_walker')
#opens Email Sender


#Button Login
btn_login = Button(window, text="Login", command=Login)
btn_login.grid(row=1, column=0)

#button instagram
btn_instagram = Button(window, text="folow on instagram", command=go_to_instagram)
btn_instagram.grid(row=1, column=1)

#Button youtube
btn_youtube = Button(text="Follow on Youtube", command=go_to_youtube)
btn_youtube.grid(row=1, column=2)

#Logo
photo_icon_btn = PhotoImage(file = r"/Users/vigowalker/Downloads/instagram2.png", width=100, height=100)
img = (Image.open('/Users/vigowalker/Downloads/instagram.png'))

btn_img_logo = Button(image=photo_icon_btn, command=open_instagram)
btn_img_logo.grid(row=2, column=0)

#Send Emails
btn_email = Button(text="Send Eamil")
btn_email.grid(row=1, column=3)

p1 = PanedWindow(window, bg="black", width=500, height=100)
p1.grid(row=3, column=1)

window.mainloop()