import tkinter as tk
from tkinter import *
import mysql.connector

def digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

class page_RegisterManager(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbl_Title = tk.Label(self, text="Register Manager ")
        self.lbl_FName = tk.Label(self, text="First Name")
        self.lbl_LName = tk.Label(self, text="Last Name")
        self.lbl_UName = tk.Label(self, text="Username")
        self.lbl_CCode = tk.Label(self, text="Confirmation Code")
        self.lbl_1Pass = tk.Label(self, text="Password")
        self.lbl_2Pass = tk.Label(self, text="Confirm Password")
        self.lbl_Email = tk.Label(self, text="Email")
        self.lbl_Phone = tk.Label(self, text="Phone")

        self.txt_Title = StringVar()
        self.txt_FName = StringVar()
        self.txt_LName = StringVar()
        self.txt_UName = StringVar()
        self.txt_CCode = StringVar()
        self.txt_1Pass = StringVar()
        self.txt_2Pass = StringVar()
        self.txt_Email = StringVar()
        self.txt_Phone = StringVar()

        self.ent_Title = tk.Entry(self, textvariable=self.txt_Title)
        self.ent_FName = tk.Entry(self, textvariable=self.txt_FName)
        self.ent_LName = tk.Entry(self, textvariable=self.txt_LName)
        self.ent_UName = tk.Entry(self, textvariable=self.txt_UName)
        self.ent_CCode = tk.Entry(self, textvariable=self.txt_CCode)
        self.ent_1Pass = tk.Entry(self, textvariable=self.txt_1Pass)
        self.ent_2Pass = tk.Entry(self, textvariable=self.txt_2Pass)
        self.ent_Email = tk.Entry(self, textvariable=self.txt_Email)
        self.ent_Phone = tk.Entry(self, textvariable=self.txt_Phone)

        self.btn_Back = tk.Button(self, text="Back", command=self.back)
        self.btn_Register = tk.Button(self, text="Register", command=self.Register)

        self.txt_Error = StringVar()
        self.txt_Error.set("Registering Manager")
        self.lbl_Error = tk.Label(self, textvariable=self.txt_Error)

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)

        query = ("SELECT store_name, house_number, street, city, state, zip_code, address.id "
                 "FROM groceryStore, address "
                 "WHERE groceryStore.address_id = address.id")
        cursor.execute(query)

        OPTIONS = cursor.fetchall()

        self.txt_Store = StringVar()
        self.txt_Store.set(OPTIONS[0])

        self.opt_Store = tk.OptionMenu(self, self.txt_Store, *OPTIONS)

        self.lbl_Title.grid(row=0,column=2)
        self.lbl_FName.grid(row=1,column=0)
        self.ent_FName.grid(row=1,column=1)
        self.lbl_LName.grid(row=1,column=3)
        self.ent_LName.grid(row=1,column=4)
        self.lbl_UName.grid(row=2,column=0)
        self.ent_UName.grid(row=2,column=1)
        self.lbl_CCode.grid(row=2,column=3)
        self.ent_CCode.grid(row=2,column=4)
        self.lbl_1Pass.grid(row=3,column=0)
        self.ent_1Pass.grid(row=3,column=1)
        self.lbl_2Pass.grid(row=3,column=3)
        self.ent_2Pass.grid(row=3,column=4)
        self.lbl_Email.grid(row=4,column=0)
        self.ent_Email.grid(row=4,column=1)
        self.lbl_Phone.grid(row=5,column=0)
        self.ent_Phone.grid(row=5,column=1)
        self.lbl_Error.grid(row=4,column=2,columnspan=3)
        self.opt_Store.grid(row=5,column=2,columnspan=3)
        self.btn_Back.grid(row=6,column=1)
        self.btn_Register.grid(row=6,column=3)

    def back(self):
        self.controller.show_frame("page_Register")

    def Register(self):
        print("Registering")
        if (self.txt_Title.get == '' or self.txt_FName.get == '' or
            self.txt_LName.get == '' or self.txt_UName.get == '' or
            self.txt_CCode.get == '' or self.txt_1Pass.get == '' or
            self.txt_2Pass.get == '' or self.txt_Email.get == '' or
            self.txt_Phone.get == ''):
            self.txt_Error.set("All Feilds are Required")

        if self.txt_1Pass.get() != self.txt_2Pass.get():
            self.txt_Error.set("Passwords do not match")
            print("Registration Failed")
            return
        else:
            self.txt_Error.set("Passwords Matched")

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)

        query = ("SELECT username "
                 "FROM userr "
                 "WHERE username = %s")
        data_query = (self.txt_UName.get(),)

        cursor.execute(query, data_query)
        if cursor.rowcount != 0:
            self.txt_Error.set("Username is Taken")
            return

        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        if not re.search(regex,self.txt_Email.get()):
            self.txt_Error.set("Invalid Email")
            return

        phoneNumber = str(self.txt_Phone.get()).replace('-','')
        if len(phoneNumber) != 10 or not digit(phoneNumber):
            self.txt_Error.set("Phone Number is invalid")
            return
        else:
            self.txt_Error.set("Phone Number is valid")

        query = ("SELECT * "
                 "FROM systeminformation "
                 "WHERE user_codes = %s")
        data_query = (self.txt_CCode.get(),)

        cursor.execute(query, data_query)
        if cursor.rowcount != 1:
            self.txt_Error.set("Confirmation Code invalid")
            return

        query = ("INSERT INTO userr "
                 "(username, password, user_type, email, first_name, last_name, phone) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data_query = (self.txt_UName.get(), self.txt_1Pass.get(), "manager",
                      self.txt_Email.get(), self.txt_FName.get(), self.txt_LName.get(), phoneNumber)
        cursor.execute(query, data_query)

        query = ("INSERT INTO manages "
                "(username, store_address) "
                "VALUES (%s, %s)")
        data_query = (self.txt_UName.get(), self.txt_Store.get().strip(')').split(',')[6])
        cursor.execute(query, data_query)

        try:
            cnx.commit()
        except mysql.connector.Error as err:
            self.txt_Error.set("Error Adding Person: " + err)
            print("Error Adding Person: " + err)
            return

        cursor.close()
        cnx.close()
        self.controller.show_frame("page_LoginMenu")
