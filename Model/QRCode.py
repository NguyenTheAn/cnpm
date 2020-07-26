import qrcode
from datetime import datetime

class QRCode():
    def __init__(self, name):
        self.name = name

    def generate(self):
        now = datetime.now()
        txt = f"{self.name}_{now}"
        img = qrcode.make(txt)
        return img



