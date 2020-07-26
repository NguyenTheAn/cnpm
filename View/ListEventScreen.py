import tkinter as tk
from Controller.EventController import EventController
from View.EventInforScreen import EventInforScreen

class ListEventScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        global name

        self.eventController = EventController()
        listEvent = self.eventController.readEventfromdb()

        label = tk.Label(self, width=40, height=2, text='List Event')
        label.grid(row = 0,column = 0, sticky="W")

        self.listbox = tk.Listbox(self)

        for i, event in enumerate(listEvent):
            self.listbox.insert(i, event.name)

        self.listbox.grid(row = 1,column = 0, sticky="E")

        btn1 = tk.Button(self, text='Show info', width=20, height=2, command = self.show_info_screen)
        btn1.grid(row = 2,column = 0, sticky="E")
        # Buttons
        btn2 = tk.Button(self, text='Cancel', width=20, height=2, command = lambda : controller.show_frame("ManagerScr"))
        btn2.grid(row = 2,column = 1, sticky="E")

    def show_info_screen(self):
        name = self.listbox.get(tk.ACTIVE)
        eventList = self.eventController.readEventfromdb()
        for event in eventList:
            if event.name == name:
                frame = EventInforScreen(self.parent, self.controller, event, self)
                frame.grid(row=0, column=0, sticky="nsew")
                frame.tkraise()
