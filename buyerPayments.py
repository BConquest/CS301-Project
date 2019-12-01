import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

class page_BuyerPayments(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl_Title = Label(self, text="Buyer Functionality")

        self.lbl_Title.grid(row=0,column=1)
