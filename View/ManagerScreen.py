import tkinter as tk
from Controller.LoginController import LoginController
from Model.Account import Account
from tkinter import ttk
from tkinter import messagebox

class ManagerScr(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global name

        self.event_combo = ttk.Combobox(self, value=[])
        self.event_combo.grid(row=0, column=1)
        self.event_combo.current(0)

        self.logout_bt = tk.Button(self, text='Log Out', width=20, height=2)
        self.logout_bt.grid(row=3, column=0, sticky='E')
        self.create_event_bt = tk.Button(self, text='Create Event', width=20, height=2)
        self.create_event_bt.grid(row=3, column=2, sticky='E')
        self.diemdanh_bt = tk.Button(self, text='Điểm danh', width=20, height=2)
        self.diemdanh_bt.grid(row=3, column=0, sticky='E')
