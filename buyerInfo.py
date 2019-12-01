import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

class page_BuyerInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl_Title = Label(self, text="Buyer Account Information")

        self.lbl_FName = Label(self, text="First Name")
        self.lbl_LName = Label(self, text="Last Name")
        self.lbl_UName = Label(self, text="Username")
        self.lbl_Phone = Label(self, text="Phone")
        self.lbl_Store = Label(self, text="Prefered Grocery Store")
        self.lbl_HAddr = Label(self, text="Address")
        self.lbl_SAddr = Label(self, text="Store Address")
        self.lbl_City = Label(self, text="City")
        self.lbl_Email = Label(self, text="Email")
        self.lbl_State = Label(self, text="State")
        self.lbl_PCCNr = Label(self, text="Preffered Credit Card Number")
        self.lbl_ZCode = Label(self, text="Zip Code")
        self.lbl_RCode = Label(self, text="Routing Number")

        self.txt_FName = StringVar()
        self.txt_LName = StringVar()
        self.txt_UName = StringVar()
        self.txt_Phone = StringVar()
        self.txt_Store = StringVar()
        self.txt_HAddr = StringVar()
        self.txt_SAddr = StringVar()
        self.txt_City = StringVar()
        self.txt_Email = StringVar()
        self.txt_State = StringVar()
        self.txt_PCCNr = StringVar()
        self.txt_ZCode = StringVar()
        self.txt_RCode = StringVar()

        self.ent_FName = Entry(self, textvariable=self.txt_FName, state='disabled')
        self.ent_LName = Entry(self, textvariable=self.txt_LName, state='disabled')
        self.ent_UName = Entry(self, textvariable=self.txt_UName, state='disabled')
        self.ent_Phone = Entry(self, textvariable=self.txt_Phone)
        self.ent_Store = Entry(self, textvariable=self.txt_Store)
        self.ent_HAddr = Entry(self, textvariable=self.txt_HAddr)
        self.ent_SAddr = Entry(self, textvariable=self.txt_SAddr)
        self.ent_City = Entry(self, textvariable=self.txt_City)
        self.ent_Email = Entry(self, textvariable=self.txt_Email)
        self.ent_State = Entry(self, textvariable=self.txt_State)
        self.ent_PCCNr = Entry(self, textvariable=self.txt_PCCNr)
        self.ent_ZCode = Entry(self, textvariable=self.txt_ZCode)
        self.ent_RCode = Entry(self, textvariable=self.txt_RCode)

        self.btn_Back = Button(self, text="Back", command=self.back)
        self.btn_Delete = Button(self, text="Delete Account", command=self.delete)
        self.btn_Update = Button(self, text="Update Account", command=self.update)

        self.lbl_Title.grid(row=0,column=2)
        self.lbl_FName.grid(row=1,column=0)
        self.ent_FName.grid(row=1,column=1)
        self.lbl_LName.grid(row=1,column=3)
        self.ent_LName.grid(row=1,column=4)
        self.lbl_UName.grid(row=2,column=0)
        self.ent_UName.grid(row=2,column=1)
        self.lbl_Phone.grid(row=2,column=3)
        self.ent_Phone.grid(row=2,column=4)
        self.lbl_Store.grid(row=3,column=0)
        self.ent_Store.grid(row=3,column=1)
        self.lbl_HAddr.grid(row=3,column=3)
        self.ent_HAddr.grid(row=3,column=4)
        self.lbl_SAddr.grid(row=4,column=0)
        self.ent_SAddr.grid(row=4,column=1)
        self.lbl_City.grid(row=4,column=3)
        self.ent_City.grid(row=4,column=4)
        self.lbl_Email.grid(row=5,column=0)
        self.ent_Email.grid(row=5,column=1)
        self.lbl_State.grid(row=5,column=3)
        self.ent_State.grid(row=5,column=4)
        self.lbl_PCCNr.grid(row=6,column=0)
        self.ent_PCCNr.grid(row=6,column=1)
        self.lbl_ZCode.grid(row=6,column=3)
        self.ent_ZCode.grid(row=6,column=4)
        self.lbl_RCode.grid(row=7,column=0)
        self.ent_RCode.grid(row=7,column=1)
        self.btn_Back.grid(row=8,column=0)
        self.btn_Delete.grid(row=8,column=2)
        self.btn_Update.grid(row=8,column=4)

    def back(self):
        self.controller.show_frame("page_BuyerFunctionality")

    def delete(self):
        print("Delete")

    def update(self):
        print("Update")
