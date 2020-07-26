import tkinter as tk
from PIL import ImageTk

class QRScreen(tk.Frame):
    def __init__(self, parent, controller, img):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        global name

        lmain = tk.Label(self)
        lmain.grid(row=0, column=0)

        btn = tk.Button(self, text="Cancel", width=20, height=2,
                        command=lambda: self.controller.show_frame("AtendanceMainScreen"))
        btn.grid(row=0, column=1, sticky='E', )

        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
