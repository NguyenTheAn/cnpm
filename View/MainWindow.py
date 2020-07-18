import tkinter as tk
from View.LoginScreen import LogIn

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = 'top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = LogIn(container, self)
        self.frames[frame.__name__] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(frame.__name__)
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
