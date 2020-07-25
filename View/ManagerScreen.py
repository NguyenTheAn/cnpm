import tkinter as tk


class ManagerScr(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global name

        self.logout_bt = tk.Button(self, text='Log Out', width=20, height=2)
        self.logout_bt.grid(row=1, column=0, sticky='E')
        self.create_event_bt = tk.Button(self, text='Create Event', width=20, height=2, command = lambda : self.controller.show_frame("CreateEvent"))
        self.create_event_bt.grid(row=0, column=0, sticky='E')
        self.diemdanh_bt = tk.Button(self, text='List Event', width=20, height=2)
        self.diemdanh_bt.grid(row=0, column=1, sticky='E')
