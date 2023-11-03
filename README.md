
## My tkinter projects

here I will put all my tkinter projects I make in python


## Installation

Install tkinter

```bash
  pip install tkinter
```
    
## Tkinter - importing

#### import

```http
  import tkinter as tk
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Tkinter` | `import` | **Tkinter is pre-installed** |


## Tkinter tutorial - basic window

learn how to make a simple window in Tkinter

## importing tkinter

```http
  import tkinter as tk
```

now that we have imported tkinter, it's time to make our first window!

## making our first window

```http
    window = tk.window()
    window.title('First window')
    window.geometry("800x800")

    window.mainloop()
```

in **window = tk.window()** we are creating the window but in order to get the window displayed
we need to add a title and some resolution.
Then you have to close the window with **window.mainloop()**