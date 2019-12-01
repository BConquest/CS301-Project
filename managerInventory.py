import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

class page_ManagerInventory(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.txt_Title = StringVar()
            self.txt_Title.set("Inventory Total Items: ")
            self.lbl_Title = Label(self, textvariable=self.txt_Title)

            self.tv_Orders = Treeview(self)
            self.tv_Orders['columns'] = ('Description','Quantity',
                                        'Retail Price', 'Wholesale Price', 'Expiration Date')
            self.tv_Orders.heading('#0', text='Item Name')
            self.tv_Orders.column('#0', anchor="w")
            self.tv_Orders.heading('Description', text='Description')
            self.tv_Orders.column('Description', anchor="w")
            self.tv_Orders.heading('Quantity', text='Quantity')
            self.tv_Orders.column('Quantity', anchor="w")
            self.tv_Orders.heading('Retail Price', text='Retail Price')
            self.tv_Orders.column('Retail Price', anchor="w")
            self.tv_Orders.heading('Wholesale Price', text='Wholesale Price')
            self.tv_Orders.column('Wholesale Price', anchor="w")
            self.tv_Orders.heading('Expiration Date', text='Expiration Date')
            self.tv_Orders.column('Expiration Date', anchor="w")

            self.btn_Back = Button(self, text="Back", command=self.back)
            self.btn_Add = Button(self, text="Add", command=self.add)
            self.btn_Delete = Button(self, text="Delete", command=self.delete)

            self.lbl_Title.grid(row=0,column=0)
            self.tv_Orders.grid(row=1,column=0)
            self.btn_Back.grid(row=2,column=0,columnspan=3)
            self.btn_Add.grid(row=2,column=1)
            self.btn_Delete.grid(row=2,column=2)

            self.tv_Orders.insert('','end',text="Test", values=('Temp','Temp','Temp','Temp','Temp'))

        def back(self):
            self.controller.show_frame("page_ManagerFunctionality")

        def add(self):
            print("Added 1 of object")

        def delete(self):
            print("Removed 1 of object")
