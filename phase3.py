import tkinter as tk
from tkinter import *
import mysql.connector

from registerBuyer import page_RegisterBuyer
from registerDeliverer import page_RegisterDeliverer
from registerManager import page_RegisterManager

from managerMenu import page_ManagerFunctionality
from managerInfo import page_ManagerInfo
from managerReport import page_ManagerReport
from managerOrders import page_ManagerOrders
from managerInventory import page_ManagerInventory

from buyerMenu import page_BuyerFunctionality
from buyerInfo import page_BuyerInfo
from buyerNOrder import page_BuyerNewOrder
from buyerOrders import page_BuyerOrders
from buyerPayments import page_BuyerPayments

from delivererMenu import page_delivererFunctionality
from delivererInfo import page_DelivererInfo

from login import page_Login
from registerMenu import page_Register
from loginMenu import page_LoginMenu

def digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

class shopApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data = {
            "username": StringVar()
        }

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.container = container

        self.frames = {}

        for F in (page_Register, page_Login, page_RegisterBuyer, page_LoginMenu,
                  page_RegisterDeliverer, page_RegisterManager, page_ManagerFunctionality,
                  page_ManagerInfo, page_ManagerOrders, page_ManagerInventory,
                  page_ManagerReport, page_BuyerFunctionality, page_BuyerInfo,
                  page_BuyerNewOrder, page_BuyerOrders, page_BuyerPayments,
                  page_delivererFunctionality, page_DelivererInfo):
            print("Initiliazing page: " + F.__name__)
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("page_LoginMenu")

    def show_frame(self, page_name):
        print("Loading Frame: " + str(page_name))
        self.update_frame()
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
        frame.tkraise()
        frame.winfo_toplevel().geometry("")
        print("Frame Successfully Loaded")


    def update_frame(self):
        for F in (page_Register, page_Login, page_RegisterBuyer, page_LoginMenu,
                  page_RegisterDeliverer, page_RegisterManager, page_ManagerFunctionality,
                  page_ManagerInfo, page_ManagerOrders, page_ManagerInventory,
                  page_ManagerReport, page_BuyerFunctionality, page_BuyerInfo,
                  page_BuyerNewOrder, page_BuyerOrders, page_BuyerPayments,
                  page_delivererFunctionality, page_DelivererInfo):
            print("Recreating page: " + F.__name__)
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = shopApp()
    app.mainloop()
