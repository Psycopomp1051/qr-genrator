import tkinter
from tkinter import *

import PIL
import qrcode
from PIL import ImageTk


class QRImage:
    def _init_(self):
        self.tk = tkinter.Tk()
        self.tk.geometry("700x700")
        self.tk.configure(bg="#2C2C2C")

        self.addLabelEnterData()
        self.addInputForData()
        self.addBtnGenerate()
        self.addQRImage()

        self.tk.mainloop()

    def addLabelEnterData(self):
        self.lblEnterData = Label(self.tk,text="Enter Data",bg="#2C2C2C",font="nunito 20",fg="#ffffff")
        self.lblEnterData.pack(side=TOP, anchor=NW, pady=(50,0), padx=50)

    def addInputForData(self):
        self.txtUrl = Entry(self.tk, width=400, bg="#B8B8B8",font="nunito 20",fg="#3A3A3A")
        self.txtUrl.pack(side=TOP, anchor=CENTER, pady=(10,25), padx=50)

    def addBtnGenerate(self):
        self.btnGenerate = Button(self.tk, width=10, height=1, text="Generate",font="nunito 20",bg="#B8B8B8",fg="#3A3A3A")
        self.btnGenerate.pack(side=TOP, anchor=CENTER, padx=10, pady=10)
        self.btnGenerate.configure(command=self.generate)

    def addQRImage(self):
        lblQRimage = Label(self.tk, width=500, height=500,bg="#2C2C2C")
        lblQRimage.pack(side=TOP, anchor=CENTER, padx=10, pady=10)
        lblQRimage.pack_propagate(0)
        self.lblQRimage = lblQRimage

    def generate(self):
        data = self.txtUrl.get()
        qr = qrcode.QRCode(
            version=15,
            box_size=5,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True, )
        img = qr.make_image(fill="black", back_color="white")
        img.save("code.png")
        print(data)
        self.qrImage = PIL.Image.open("code.png")
        self.qrImage = ImageTk.PhotoImage(self.qrImage)
        self.lblQRimage.configure(image=self.qrImage)

QRImage()