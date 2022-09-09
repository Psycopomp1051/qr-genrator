import imp
from msilib.schema import File
from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from tkinter import font
from turtle import title
from list import start
import os

class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry('900x500+200+50')
        self.root.title("QR Generator")

        title =Label(self.root,text="   QR generator",font=("times new roman",40), bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        btnGotoList = Button(self.root,text="Go TO List",bg="#ff0000",width=10,height=1,font=("goudy old style",10),command=self.goToList)
        btnGotoList.pack(side=TOP,anchor=NE,padx=10,pady=20)

        #-----------Employe Details Window------------
        #-------------VARIABLE--------
        self.var_emp_code=StringVar()
        self.var_name= StringVar()
        self.var_department= StringVar()
        self.var_designation= StringVar()

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        emp_title= Label(emp_Frame, text="EMPLOYEE DETAIL", font=("goudy old style",20), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)


        lbl_emp_code= Label(emp_Frame, text="EMPLOYEE ID", font=(" times new roman",15,'bold'), bg='white').place(x=20, y=60)
        lbl_emp_code = Label(emp_Frame, text="NAME", font=(" times new roman", 15, 'bold'), bg='white').place(x=20, y=100)
        lbl_emp_code= Label(emp_Frame, text="DEPARTMENT", font=(" times new roman",15,'bold'), bg='white').place(x=20, y=140)
        lbl_emp_code = Label(emp_Frame, text="DESIGNATION", font=(" times new roman", 15, 'bold'), bg='white').place(x=20, y=180)

        txt_emp_code= Entry(emp_Frame,  font=(" times new roman",15,),textvariable=self.var_emp_code, bg='light yellow').place(x=200, y=60)
        txt_emp_code =Entry(emp_Frame,  font=(" times new roman", 15,),textvariable=self.var_name ,bg='light yellow').place(x=200, y=100)
        txt_emp_code= Entry(emp_Frame,  font=(" times new roman",15,),textvariable=self.var_department ,bg='light yellow').place(x=200, y=140)
        txt_emp_code =Entry(emp_Frame,  font=(" times new roman", 15,),textvariable=self.var_designation, bg='light yellow').place(x=200, y=180)


        btn_generate=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=280,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg, font=(" times new roman",20,), bg='white',fg='green')
        self.lbl_msg.place(x=0, y=310,relwidth=1)

        # -----------Employe QR CODE Window------------
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380)

        emp_title = Label(qr_Frame, text="EMPLOYEE QR CODE", font=("goudy old style",17), bg='#043256',fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code=Label(qr_Frame,text='No QR\nAvialable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def goToList(self):
        start()
        
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

        self.msg = 'ALL FIELDS ARE REQUIRED!!!'
        self.lbl_msg.config(text=self.msg, fg='red')

    def generate(self):
        if self.var_designation.get()==''or self.var_department.get()=='' or self.var_name.get()=='' or self.var_emp_code.get()=='':
            self.msg='ALL FIELDS ARE REQUIRED!!!'
            self.lbl_msg.config(text=self.msg,fg='red')

        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment :{self.var_department.get()}\nDesignation :{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')


            #----------qr image update--------


            self.im=ImageTk.PhotoImage(file="Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)


            #-------------notification-------------



            self.msg='QR generated Successfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')




root = Tk()
obj = Qr_Generator(root)
root.mainloop()
