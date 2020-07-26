import tkinter as tk
from View.LoginScreen import LogIn
from View.SignupScreen import SignUp
from View.ManagerScreen import ManagerScr
from View.CreateEventScr import CreateEvent
from View.ListEventScreen import ListEventScreen
from View.AttendanceMainScreen import AtendanceMainScreen
from View.SearchScreen import SearchScreen

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = 'top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (LogIn, SignUp, ManagerScr, CreateEvent, ListEventScreen, AtendanceMainScreen, SearchScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("LogIn")
    def show_frame(self, name):
        frame = self.frames[name]
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
