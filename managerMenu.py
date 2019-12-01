import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

class page_ManagerFunctionality(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl_Title = Label(self, text="Manager Functionality")

        self.btn_ViewReport = Button(self, text="View Revenue Report", command=self.revenue)
        self.btn_AccountInfo = Button(self, text="Account Information", command=self.info)
        self.btn_ViewOrders = Button(self, text="View Orders", command=self.orders)
        self.btn_Back = Button(self, text="Back", command=self.back)
        self.btn_ViewInventory = Button(self, text="View Inventory", command=self.inventory)

        self.lbl_Title.grid(row=0,column=1)
        self.btn_ViewReport.grid(row=1,column=0)
        self.btn_AccountInfo.grid(row=1,column=2)
        self.btn_ViewOrders.grid(row=2,column=0)
        self.btn_Back.grid(row=2,column=2)
        self.btn_ViewInventory.grid(row=3,column=0)

    def back(self):
        self.controller.show_frame("page_LoginMenu")

    def revenue(self):
        self.controller.show_frame("page_ManagerReport")

    def info(self):
        self.controller.show_frame("page_ManagerInfo")

    def orders(self):
        self.controller.show_frame("page_ManagerOrders")

    def inventory(self):
        self.controller.show_frame("page_ManagerInventory")
