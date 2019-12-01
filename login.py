import tkinter as tk
from tkinter import *
import mysql.connector

class page_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lable = tk.Label(self, text="Logged in").pack()
