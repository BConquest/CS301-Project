import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

class page_delivererFunctionality(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl_Title = Label(self, text="Buyer Functionality")

        self.btn_Assignments = Button(self, text="Assignments", command=self.assign)
        self.btn_AccountInfo = Button(self, text="Account Information", command=self.info)
        self.btn_Back = Button(self, text="Back", command=self.back)

        self.lbl_Title.grid(row=0,column=1)
        self.btn_Assignments.grid(row=1,column=0)
        self.btn_AccountInfo.grid(row=1,column=2)
        self.btn_Back.grid(row=2,column=0,columnspan=2)

    def back(self):
        self.controller.show_frame("page_LoginMenu")

    def assign(self):
        print("Assign")

    def info(self):
        self.controller.show_frame("page_DelivererInfo")
