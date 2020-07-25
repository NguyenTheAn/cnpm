import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Controller.EventController import EventController


class CreateEvent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global name

        # Labels

        event_name_label = tk.Label(self, width=40, height=2, text='EventName :')
        event_name_label.grid(row=0, column=0, sticky="W")
        des_label = tk.Label(self, width=40, height=2, text='Description :')
        des_label.grid(row=1, column=0, sticky="W")
        start_date_label = tk.Label(self, width=40, height=2, text='StartDate  :')
        start_date_label.grid(row=2, column=0, sticky="W")
        end_date_label = tk.Label(self, width=40, height=2, text='EndDate  :')
        end_date_label.grid(row=3, column=0, sticky="W")

        # entry

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1)
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1)

        self.combo3 = ttk.Combobox(self, values=list(range(1, 32)))
        self.combo3.grid(row=2, column=1)
        self.combo3.current(0)
        self.combo4 = ttk.Combobox(self, values=list(range(1, 13)))
        self.combo4.grid(row=2, column=2)
        self.combo4.current(0)
        self.combo5 = ttk.Combobox(self, values=list(range(1919, 2020)))
        self.combo5.grid(row=2, column=3)
        self.combo5.current(0)
        
        self.combo6 = ttk.Combobox(self, values=list(range(1, 32)))
        self.combo6.grid(row=3, column=1)
        self.combo6.current(0)
        self.combo7 = ttk.Combobox(self, values=list(range(1, 13)))
        self.combo7.grid(row=3, column=2)
        self.combo7.current(0)
        self.combo8 = ttk.Combobox(self, values=list(range(1919, 2020)))
        self.combo8.grid(row=3, column=3)
        self.combo8.current(0)

        # button

        self.btn1 = tk.Button(self, text='Create', width=20, height=2, command = self.check)
        self.btn1.grid(row=8, column=1, sticky='E')

        self.btn2 = tk.Button(self, text='Cancel', width=20, height=2, command = lambda : self.controller.show_frame("ManagerScr"))
        self.btn2.grid(row=8, column=0)

    def __name__(self):
        return "CreateEvent"

    def check (self):
        check = False
        if len(self.entry1.get()) == 0:
            self.entry1.config({"background": 'Yellow'})
            check = True
        if len(self.entry2.get()) == 0:
            self.entry2.config({"background": 'Yellow'})
            check = True

        if check == False:
            eventController = EventController()
            eventController.saveToDb(
                self.entry1.get(),
                self.entry2.get(),
                f"{self.combo3.get()}/{self.combo4.get()}/{self.combo5.get()}",
                f"{self.combo6.get()}/{self.combo7.get()}/{self.combo8.get()}"
            )
