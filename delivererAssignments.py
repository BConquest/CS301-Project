import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

def digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

class page_DelivererInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.lbl_Title = Label(self, text="Assignments")

        self.btn_Back = Button(self, text="Back", command=self.back)
        self.btn_View = Button(self, text="View Assignment Details", command=self.view)

        self.tv_Assignments = Treeview(self)
        self.tv_Assignments['columns'] = ('Store Address','Order id',
                                    'Date', 'Time Order Made', 'Time of Delivery',
                                    'Order Price', 'Total Number of Items')
        self.tv_Assignments.heading('#0', text='Store Name')
        self.tv_Assignments.column('#0', anchor="w")
        self.tv_Assignments.heading('Store Address', text='Store Address')
        self.tv_Assignments.column('Store Address', anchor="w")
        self.tv_Assignments.heading('Order id', text='Order id')
        self.tv_Assignments.column('Order id', anchor="w")
        self.tv_Assignments.heading('Date', text='Date')
        self.tv_Assignments.column('Date', anchor="w")
        self.tv_Assignments.heading('Total Price', text='Total Price')
        self.tv_Assignments.column('Total Price', anchor="w")
        self.tv_Assignments.heading('Total Number of Items', text='Total Number of Items')
        self.tv_Assignments.column('Total Number of Items', anchor="w")
        self.tv_Assignments.heading('Delivery Address', text='Delivery Address')
        self.tv_Assignments.column('Delivery Address', anchor="w")

    def back(self):
        self.controller.show_frame("page_BuyerFunctionality")

    def view(self):
        print("Viewing assignment")