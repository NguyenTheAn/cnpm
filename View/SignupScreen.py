import tkinter as tk
from tkinter import ttk

class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Labels

        label1 = tk.Label(self, width=40, height=2, text='Name  :')
        label1.grid(row=0, column=0, sticky="W")

        label2 = tk.Label(self, width=40, height=2, text='Age  :')
        label2.grid(row=1, column=0, sticky="W")

        label3 = tk.Label(self, width=40, height=2, text='Gender  :')
        label3.grid(row=2, column=0, sticky="W")

        label4 = tk.Label(self, width=40, height=2, text='DOB  :')
        label4.grid(row=3, column=0, sticky="W")

        label5 = tk.Label(self, width=40, height=2, text='Email  :')
        label5.grid(row=4, column=0, sticky="W")

        label6 = tk.Label(self, width=40, height=2, text='Username  :')
        label6.grid(row=5, column=0, sticky="W")

        label7 = tk.Label(self, width=40, height=2, text='Password  :')
        label7.grid(row=6, column=0, sticky="W")

        # entry

        self.namevar = tk.StringVar()
        self.agevar = tk.StringVar()
        self.emailvar = tk.StringVar()
        self.usernamevar = tk.StringVar()
        self.passwordvar = tk.StringVar()

        entry1 = tk.Entry(self, textvar=self.namevar)
        entry1.grid(row=0, column=1)

        self.combo1 = ttk.Combobox(self, values=list(range(1, 100)))
        self.combo1.grid(row=1, column=1)
        self.combo1.current(0)

        self.combo2 = ttk.Combobox(self, values=['Male', 'Female', 'Other'])
        self.combo2.grid(row=2, column=1)
        self.combo2.current(0)

        self.combo3 = ttk.Combobox(self, values=list(range(1, 32)))
        self.combo3.grid(row=3, column=1)
        self.combo3.current(0)

        self.combo4 = ttk.Combobox(self, values=list(range(1, 13)))
        self.combo4.grid(row=3, column=2)
        self.combo4.current(0)

        self.combo5 = ttk.Combobox(self, values=list(range(1919, 2020)))
        self.combo5.grid(row=3, column=3)
        self.combo5.current(0)

        entry3 = tk.Entry(self, textvar=self.emailvar)
        entry3.grid(row=4, column=1)

        entry4 = tk.Entry(self, textvar=self.usernamevar)
        entry4.grid(row=5, column=1)

        entry5 = tk.Entry(self, show='*', textvar=self.passwordvar)
        entry5.grid(row=6, column=1)

        # button

        btn1 = tk.Button(self, text='Sign Up', width=20, height=2)
        btn1.grid(row=7, column=1, sticky='E')

        btn2 = tk.Button(self, text='Cancel', width=20, height=2, command = lambda : controller.show_frame("LogIn"))
        btn2.grid(row=7, column=0)

    def __name__(self):
        return "SignUp"