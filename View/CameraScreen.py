import tkinter as tk
import cv2
from PIL import ImageTk, Image
from pyzbar import pyzbar
from Controller.AtendanceController import AtendanceController
from tkinter import messagebox

class CameraScreen(tk.Frame):
    def __init__(self, parent, controller, event):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.event = event
        self.parent = parent
        global name

        self.attendaceController = AtendanceController()

        self.video = cv2.VideoCapture(0)
        lmain = tk.Label(self)
        lmain.grid(row = 0, column = 0)

        btn = tk.Button(self, text="Cancel", width=20, height=2, command = lambda : self.controller.show_frame("ManagerScr"))
        btn.grid(row=0, column=1, sticky='E', )

        def show_frame():
            _, frame = self.video.read()
            frame = cv2.flip(frame, 1)
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                data = obj.data.decode("ascii")
                if self.attendaceController.verifyInfo(data, event):
                    messagebox.showinfo("Diem Danh", message=data.split("_")[0] + ' co mat')
                else:
                    messagebox.showerror("Diem Danh", message="Chua dang ky tham gia su kien")
                break

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)

        show_frame()



