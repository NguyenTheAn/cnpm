import tkinter as tk
from View.LoginScreen import LogIn
from View.SignupScreen import SignUp

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = 'top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.frames["LogIn"] = LogIn(container, self)
        self.frames["SignUp"] = SignUp(container, self)
        self.show_frame('LogIn')
    def show_frame(self, name):
        frame = self.frames[name]
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
