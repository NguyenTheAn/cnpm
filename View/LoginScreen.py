import tkinter as tk


class LogIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global name
        self.usernamevar = tk.StringVar()
        self.passwordvar = tk.StringVar()
        # Labels

        label1 = tk.Label(self, width=40, height=2, text='Username  :')
        label1.grid(row=0, column=0, sticky="W")

        label2 = tk.Label(self, width=40, height=2, text='Password  :')
        label2.grid(row=1, column=0, sticky="W")

        # Entries

        entry1 = tk.Entry(self, textvar=self.usernamevar)
        entry1.grid(row=0, column=1)

        entry2 = tk.Entry(self, show='*', textvar=self.passwordvar)
        entry2.grid(row=1, column=1)

        btn1 = tk.Button(self, text='Log In', width=20, height=2)
        btn1.grid(row=2, column=1, sticky='E')
        # Buttons
        btn2 = tk.Button(self, text='Sign Up', width=20, height=2)
        btn2.grid(row=2, column=0, sticky='W')
    def __name__(self):
        return "LogIn"
