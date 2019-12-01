import tkinter as tk
from tkinter import *
import mysql.connector

def digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

class page_LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbl_login = tk.Label(self, text="User Login:")

        self.txtUser = StringVar()
        self.txtPass = StringVar()

        self.ent_User = tk.Entry(self, textvariable=self.txtUser)
        self.ent_Pass = tk.Entry(self, textvariable=self.txtPass)

        self.lbl_User = tk.Label(self, text="Username:")
        self.lbl_Pass = tk.Label(self, text="Password:")

        self.btn_Login = tk.Button(self, text="Login", command=self.login)
        self.btn_Register = tk.Button(self, text="Register", command=self.register)

        self.lbl_login.grid(row=0, column=1)
        self.lbl_User.grid(row=1, column=0)
        self.ent_User.grid(row=1, column=2)
        self.lbl_Pass.grid(row=2, column=0)
        self.ent_Pass.grid(row=2, column=2)
        self.btn_Login.grid(row=3, column=0)
        self.btn_Register.grid(row=3,column=2)

    def login(self):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT username, password, user_type "
                 "FROM userr "
                 "WHERE username = %s AND password = %s")
        cursor.execute(query, (self.ent_User.get(), self.ent_Pass.get()))
        result = cursor.fetchone()
        if cursor.rowcount == 1:
                print(result[2])
                print("Successfully Logged In")
                if result[2] == 'buyer':
                    cursor.close()
                    cnx.close()
                    print("Buyer Type")
                    self.controller.shared_data["username"].set(self.ent_User.get())
                    self.controller.show_frame("page_BuyerFunctionality")
                elif result[2] == 'deliverer':
                    cursor.close()
                    cnx.close()
                    print("Deliverer Type")
                    self.controller.shared_data["username"].set(self.ent_User.get())
                    self.controller.show_frame("page_delivererFunctionality")
                elif result[2] == 'manager':
                    cursor.close()
                    cnx.close()
                    print("Manager Type")
                    self.controller.shared_data["username"].set(self.ent_User.get())
                    self.controller.show_frame("page_ManagerFunctionality")
                else:
                    print("Unkown User Type")
        else:
                print("Failed to login")
        cursor.close()
        cnx.close()


    def register(self):
        self.controller.show_frame("page_Register")
