import tkinter as tk
from Controller.LoginController import LoginController
from Model.Account import Account
from tkinter import ttk
from tkinter import messagebox

class LogIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global name
        self.usernamevar = tk.StringVar()
        self.passwordvar = tk.StringVar()
        # Labels

        label1 = tk.Label(self, width=40, height=2, text='Username  :')
        label1.grid(row=0, column=0, sticky="W")

        label2 = tk.Label(self, width=40, height=2, text='Password  :')
        label2.grid(row=1, column=0, sticky="W")

        label3 = tk.Label(self, width=40, height=2, text='Role  :')
        label3.grid(row=2, column=0, sticky="W")

        # Entries

        self.entry1 = tk.Entry(self, textvar=self.usernamevar)
        self.entry1.grid(row=0, column=1)

        self.entry2 = tk.Entry(self, show='*', textvar=self.passwordvar)
        self.entry2.grid(row=1, column=1)

        self.combo1 = ttk.Combobox(self, values=['Manager', 'Attendance', 'Admin'])
        self.combo1.grid(row=2, column=1)
        self.combo1.current(0)

        btn1 = tk.Button(self, text='Log In', width=20, height=2, command = self.logIn)
        btn1.grid(row=3, column=1, sticky='E')
        # Buttons
        btn2 = tk.Button(self, text='Sign Up', width=20, height=2, command = lambda : controller.show_frame("SignUp"))
        btn2.grid(row=3, column=0, sticky='W')

    def logIn(self):
        controll = LoginController()
        account = Account()
        account.set(self.entry1.get(), self.entry2.get(), self.combo1.get())
        if controll.verify(account) == True:
            if account.role == 'Manager':
                self.controller.show_frame('ManagerScr')
        else:
            messagebox.showerror(title='Login', message="Wrong username or password")


