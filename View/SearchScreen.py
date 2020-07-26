import tkinter as tk
from Controller.SearchController import SeachController
from View.SearchResultScreen import SearchResultScreen

class SearchScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        global name

        self.searchName = ''

        label1 = tk.Label(self, width=40, height=2, text='Search')
        label1.grid(row=0, column=0, sticky="W")

        self.entry1 = tk.Entry(self, textvar=self.searchName)
        self.entry1.grid(row=0, column=1)

        btn1 = tk.Button(self, text='Search', width=20, height=2, command = self.search)
        btn1.grid(row=1, column=1, sticky='E')

    def search(self):
        self.searchName = self.entry1.get()
        searchController = SeachController()
        resultList = searchController.seach(self.searchName)
        frame = SearchResultScreen(self.parent, self.controller, resultList)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()



