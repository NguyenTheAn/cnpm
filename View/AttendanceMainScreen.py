import tkinter as tk
from Model.QRCode import QRCode
from View.QRScreen import QRScreen

class AtendanceMainScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        global name
        # changeInfo_bt = tk.Button(self, text="Chỉnh sửa thông tin")
        # changeInfo_bt.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        # changePw_bt = tk.Button(self, text="Đổi mật khẩu")
        # changePw_bt.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        findEvent_bt = tk.Button(self, text="Tìm kiếm sự kiện", command = lambda : controller.show_frame('SearchScreen'))
        findEvent_bt.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        genQr_bt = tk.Button(self, text="Tạo mã QR", command = self.gen)
        genQr_bt.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        logout_bt = tk.Button(self, text="Đăng xuất", command = lambda : self.controller.show_frame("LogIn"))
        logout_bt.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

    def gen(self):
        file = open("./Data/Session.txt", 'r')
        ele = file.readlines()[0].strip().split(' ')
        qrCode = QRCode(ele[1])
        img = qrCode.generate()
        frame = QRScreen(self.parent, self.controller, img)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
