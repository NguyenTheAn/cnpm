import tkinter as tk
from Controller.DAOAttendanceList import DAOAttendanceList
from tkinter import messagebox

class MainEventscreen(tk.Frame):
    def __init__(self, parent, controller, event, prev_frame):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.prev_frame = prev_frame
        self.event = event
        self.parent = parent
        global name

        label1 = tk.Label(self, text='Event Name:')
        label1.grid(row=0, column=0, sticky="W")
        event_name_label = tk.Label(self, text=event.name)
        event_name_label.grid(row=0, column=1, sticky="W")

        label2 = tk.Label(self, text='Description:')
        label2.grid(row=1, column=0, sticky="W")
        event_des_label = tk.Label(self, text=event.description)
        event_des_label.grid(row=1, column=1, sticky="W")

        label3 = tk.Label(self, text='Start Date:')
        label3.grid(row=2, column=0, sticky="W")
        start_date_label = tk.Label(self, text=event.startDate)
        start_date_label.grid(row=2, column=1, sticky="W")

        label4 = tk.Label(self, text='End Date:')
        label4.grid(row=3, column=0, sticky="W")
        end_date_label = tk.Label(self, text=event.endDate)
        end_date_label.grid(row=3, column=1, sticky="W")

        cancel_bt = tk.Button(self, text='Cancel', width=20, height=2, command = self.show_list)
        cancel_bt.grid(row=4, column=0, sticky='E')

        btn = tk.Button(self, text="Join", width=20, height=2, command = self.join)
        btn.grid(row=4, column=1, sticky='E')

    def show_list(self):
        frame = self.prev_frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def join(self):
        dao = DAOAttendanceList()
        file = open("./Data/Session.txt", 'r')
        line = file.readlines()[0].strip()
        dao.write(self.event.name, line)
        messagebox.showinfo(title='Join Event', message='Join successfull')


