import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

class page_ManagerOrders(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbl_Title = Label(self, text="Outstanding Orders")

        self.tv_Orders = Treeview(self)
        self.tv_Orders['columns'] = ('Store Address','Order id',
                                    'Date', 'Total Price', 'Total Number of Items',
                                    'Delivery Address')
        self.tv_Orders.heading('#0', text='Store Name')
        self.tv_Orders.column('#0', anchor="w")
        self.tv_Orders.heading('Store Address', text='Store Address')
        self.tv_Orders.column('Store Address', anchor="w")
        self.tv_Orders.heading('Order id', text='Order id')
        self.tv_Orders.column('Order id', anchor="w")
        self.tv_Orders.heading('Date', text='Date')
        self.tv_Orders.column('Date', anchor="w")
        self.tv_Orders.heading('Total Price', text='Total Price')
        self.tv_Orders.column('Total Price', anchor="w")
        self.tv_Orders.heading('Total Number of Items', text='Total Number of Items')
        self.tv_Orders.column('Total Number of Items', anchor="w")
        self.tv_Orders.heading('Delivery Address', text='Delivery Address')
        self.tv_Orders.column('Delivery Address', anchor="w")

        self.btn_Back = Button(self, text="Back", command=self.back)

        self.lbl_Title.grid(row=0,column=0)
        self.tv_Orders.grid(row=1,column=0)
        self.btn_Back.grid(row=2,column=0)

        self.tv_Orders.insert('','end',text="Test", values=('Temp','Temp','Temp','Temp','Temp','Temp'))
    def back(self):
        self.controller.show_frame("page_ManagerFunctionality")
