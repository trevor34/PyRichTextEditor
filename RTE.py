import tkinter as tk
from tkinter import font as tkFont
import tkinter.ttk as tkk

class Application(tk.Frame):
    def __init__(self, name, master=None):
        super().__init__(master)
        self.style = tkk.Style()
        self.text = ""

        self.default = name
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.bind("<Key>", self.key_pressed)  # Bind send if key is clicked

    def create_widgets(self):
        self.style.configure('W.TButton', font =
               ('calibri', 10, 'bold'))
        self.buttontest = tkk.Button(self, text="B", style="W.TButton").grid(column=0, row=0)
        self.buttontest2 = tkk.Button(self, text="N").grid(column=1, row=0)
        self.canvas = tk.Canvas(self, width=200, height=100)
        self.canvas.grid(row=1)
        self.canvasText = self.canvas.create_text([5, 5], text="", anchor="nw")

    def key_pressed(self, event):
        print(event.char, event.keycode)
        self.text += event.char
        self.canvas.itemconfig(self.canvasText, text=self.text)
        

        


root = tk.Tk()
app = Application("RTE.py", master=root)
app.mainloop()
