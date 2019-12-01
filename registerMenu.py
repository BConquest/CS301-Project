import tkinter as tk
from tkinter import *
import mysql.connector

class page_Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl_Title = tk.Label(self, text="Register Navigation")

        self.btn_Buyer = tk.Button(self, text="Buyer", command=self.buyer)
        self.btn_Deliverer = tk.Button(self, text="Deliverer", command=self.deliverer)
        self.btn_Manager = tk.Button(self, text="Manager", command=self.manager)
        self.btn_Back = tk.Button(self, text="Back", command=self.back)

        self.lbl_Title.grid(row=0,column=0)
        self.btn_Buyer.grid(row=1,column=0)
        self.btn_Deliverer.grid(row=2,column=0)
        self.btn_Manager.grid(row=3, column=0)
        self.btn_Back.grid(row=4,column=0)

    def buyer(self):
        self.controller.show_frame("page_RegisterBuyer")

    def deliverer(self):
        self.controller.show_frame("page_RegisterDeliverer")

    def manager(self):
        self.controller.show_frame("page_RegisterManager")

    def back(self):
        self.controller.show_frame("page_LoginMenu")
