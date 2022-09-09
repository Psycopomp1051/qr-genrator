from doctest import master
import imghdr
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
class EmpData:
    def __init__(self,empID,qrPath):
        self.empID = empID
        self.qrPath = qrPath
    
    def __str__(self) :
        return f"Emp ID: {self.empID}\nQr Path:  {self.qrPath}"


class LibraryUI:
    def __init__(self,empDataList):
        self.empDataList = empDataList
        self.tk  = Tk()
        self.tk.geometry("900x500")
        lbl = Label(self.tk,text="LIBRARY",width=300,height=3,bg="#E04646",fg="white",font="nunito 15",)
        lbl.pack(side=TOP,anchor=NW)
        
        self.addListFrame()
        self.lblQR = Label(self.tk,text="No QR",bg='#3f51b5',fg='white',bd=1,)
        self.lblQR.place(x=575, y=175, width=180, height=180)
        self.tk.mainloop()
    
    def addListFrame(self):
        self.listFrame = Frame(self.tk,width=200,height=500,bg="#000000",relief=RIDGE)
        self.listFrame.pack(side=LEFT,anchor=NW,pady=30,padx=53)

        # Create main frame
        main_frame = Frame(self.listFrame)
        main_frame.pack(fill=BOTH,expand=1)

        # Create Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=2)

        # Add scrollbar to canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_scrollbar.bind("<Configure>",lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

        # Create Another Frame Inside canvas
        second_frame = Frame(my_canvas)

        # Add frame to window in canvas
        my_canvas.create_window((0,0),window=second_frame,anchor="nw")
        for x in self.empDataList:
            btn = Button(second_frame,text=x.empID,bg="#DD8989",width=20,height=1,font="roboto 20 bold",fg="#ffffff")
            # self.showQr(x.qrPath)
            self.configureButtons(btn,x.qrPath)
            btn.pack(side=TOP,anchor=NW,pady=(0,10))

    def configureButtons(self,btn,path):
        btn.configure(command=lambda: self.showQr(path))


    def showQr(self,x):
        self.im=ImageTk.PhotoImage(master=self.tk,file="Employee_QR/"+x)
        print("Employee_QR/"+x)

        self.lblQR.configure(image=self.im)

def start():
    fileList = os.listdir('Employee_QR')
    empDataList = []
    for x in fileList:
        fileName = x.split("_")[1]
        id = fileName.split(".")[0]
        empData = EmpData(id,x)
        empDataList.append(empData)

    LibraryUI(empDataList)