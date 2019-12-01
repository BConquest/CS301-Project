import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

class page_BuyerFunctionality(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl_Title = Label(self, text="Buyer Functionality")

        self.btn_newOrder = Button(self, text="New Order", command=self.new)
        self.btn_AccountInfo = Button(self, text="Account Information", command=self.info)
        self.btn_ViewOrders = Button(self, text="Order History", command=self.orders)
        self.btn_ViewPayments =Button(self, text="Payment Methods", command=self.payment)
        self.btn_Back = Button(self, text="Back", command=self.back)

        self.lbl_Title.grid(row=0,column=1)
        self.btn_newOrder.grid(row=1,column=0)
        self.btn_AccountInfo.grid(row=1,column=2)
        self.btn_ViewOrders.grid(row=2,column=0)
        self.btn_ViewPayments.grid(row=2,column=2)
        self.btn_Back.grid(row=3,column=0)

    def back(self):
        self.controller.show_frame("page_LoginMenu")

    def new(self):
        self.controller.show_frame("page_BuyerNewOrder")

    def info(self):
        self.controller.show_frame("page_BuyerInfo")

    def orders(self):
        self.controller.show_frame("page_BuyerOrders")

    def payment(self):
        self.controller.show_frame("page_BuyerPayments")
