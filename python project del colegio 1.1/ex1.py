import tkinter as tk

window=tk.Tk()
window.geometry('400x400')
window.title('Calculator')
v1=tk.Entry(text='')
v1.place(x=30,y=20)
v2=None
v3=None
def solv():
    global v2,v3
    v2=v1.get()
    v3=eval(v2)
    txt1=tk.Label(v3)
    txt1.place(x=30,y=60)
bt1=tk.Button(text='Résoudre le calcul',command=solv())
bt1.place(x=120,y=20)
window.mainloop()
