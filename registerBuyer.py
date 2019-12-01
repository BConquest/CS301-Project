import tkinter as tk
from tkinter import *
import mysql.connector

def digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

class page_RegisterBuyer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbl_Title = tk.Label(self, text="Register Buyer")
        self.lbl_FName = tk.Label(self, text="First Name")
        self.lbl_LName = tk.Label(self, text="Last Name")
        self.lbl_UName = tk.Label(self, text="Username")
        self.lbl_Phone = tk.Label(self, text="Phone")
        self.lbl_1Pass = tk.Label(self, text="Password")
        self.lbl_2Pass = tk.Label(self, text="Confirm Password")
        self.lbl_Email = tk.Label(self, text="Email")
        self.lbl_State = tk.Label(self, text="State")
        self.lbl_Address = tk.Label(self, text="Address")
        self.lbl_ZipCode = tk.Label(self, text="ZipCode")
        self.lbl_City = tk.Label(self, text="City")

        self.txt_FName = StringVar()
        self.txt_LName = StringVar()
        self.txt_UName = StringVar()
        self.txt_Phone = StringVar()
        self.txt_1Pass = StringVar()
        self.txt_2Pass = StringVar()
        self.txt_Email = StringVar()
        self.txt_State = StringVar()
        self.txt_Address = StringVar()
        self.txt_ZipCode = StringVar()
        self.txt_City = StringVar()
        self.txt_Error = StringVar()

        self.ent_FName = tk.Entry(self, textvariable=self.txt_FName)
        self.ent_LName = tk.Entry(self, textvariable=self.txt_LName)
        self.ent_UName = tk.Entry(self, textvariable=self.txt_UName)
        self.ent_Phone = tk.Entry(self, textvariable=self.txt_Phone)
        self.ent_1Pass = tk.Entry(self, textvariable=self.txt_1Pass)
        self.ent_2Pass = tk.Entry(self, textvariable=self.txt_2Pass)
        self.ent_Email = tk.Entry(self, textvariable=self.txt_Email)
        self.ent_State = tk.Entry(self, textvariable=self.txt_State)
        self.ent_Address = tk.Entry(self, textvariable=self.txt_Address)
        self.ent_ZipCode = tk.Entry(self, textvariable=self.txt_ZipCode)
        self.ent_City = tk.Entry(self, textvariable=self.txt_City)
        self.lbl_Error = tk.Label(self, textvariable=self.txt_Error)

        self.btn_Back = tk.Button(self, text="Back", command=self.back)
        self.btn_Register = tk.Button(self, text="Register", command=self.register)

        self.lbl_Title.grid(row=0,column=2)
        self.lbl_FName.grid(row=1,column=0)
        self.ent_FName.grid(row=1,column=1)
        self.lbl_LName.grid(row=1,column=3)
        self.ent_LName.grid(row=1,column=4)
        self.lbl_UName.grid(row=2,column=0)
        self.ent_UName.grid(row=2,column=1)
        self.lbl_Phone.grid(row=2,column=3)
        self.ent_Phone.grid(row=2,column=4)
        self.lbl_1Pass.grid(row=3,column=0)
        self.ent_1Pass.grid(row=3,column=1)
        self.lbl_2Pass.grid(row=3,column=3)
        self.ent_2Pass.grid(row=3,column=4)
        self.lbl_Email.grid(row=4,column=0)
        self.ent_Email.grid(row=4,column=1)
        self.lbl_State.grid(row=4,column=3)
        self.ent_State.grid(row=4,column=4)
        self.lbl_Address.grid(row=5,column=0)
        self.ent_Address.grid(row=5,column=1)
        self.lbl_ZipCode.grid(row=5,column=3)
        self.ent_ZipCode.grid(row=5,column=4)
        self.lbl_City.grid(row=6,column=0)
        self.ent_City.grid(row=6,column=1)
        self.lbl_Error.grid(row=6,column=3,columnspan=2)
        self.btn_Back.grid(row=7,column=1)
        self.btn_Register.grid(row=7,column=3)

    def back(self):
        self.controller.show_frame("page_Register")

    def register(self):
        print("Registering Started")
        self.txt_Error.set("Registration Started")

        if (self.txt_City.get() == '' or self.txt_FName.get() == '' or
            self.txt_LName.get() == '' or self.txt_UName.get() == '' or
            self.txt_Phone.get() == '' or self.txt_1Pass.get() == '' or
            self.txt_2Pass.get() == '' or self.txt_Email.get() == '' or
            self.txt_State.get() == '' or self.txt_Address.get() == '' or
            self.txt_ZipCode.get() == ''):
            self.txt_Error.set("All Feilds are required")
            return

        if self.txt_1Pass.get() != self.txt_2Pass.get():
            self.txt_Error.set("Passwords do not match")
            print("Registration Failed")
            return
        else:
            self.txt_Error.set("Passwords Matched")

        if (len(self.txt_ZipCode.get()) > 5 or len(self.txt_ZipCode.get()) < 5) or not digit(self.txt_ZipCode.get()):
            self.txt_Error.set("Zip Code is not valid")
            return
        else:
            self.txt_Error.set("Zip Code is Valid")

        phoneNumber = str(self.txt_Phone.get()).replace('-','')
        if len(phoneNumber) != 10 or not digit(phoneNumber):
            self.txt_Error.set("Phone Number is invalid")
            return
        else:
            self.txt_Error.set("Phone Number is valid")

        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        if not re.search(regex,self.txt_Email.get()):
            self.txt_Error.set("Invalid Email")
            return

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)

        query = ("SELECT username "
                 "FROM userr "
                 "WHERE username = %s")
        data_query = (self.txt_UName.get(),)
        print(data_query)
        cursor.execute(query, data_query)
        if cursor.rowcount != 0:
            self.txt_Error.set("Username is Taken")
            return

        query = ("INSERT INTO userr "
                 "(username, password, user_type, email, first_name, last_name) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data_query = (self.txt_UName.get(), self.txt_1Pass.get(), "buyer",
                      self.txt_Email.get(), self.txt_FName.get(), self.txt_LName.get(), phoneNumber)
        cursor.execute(query, data_query)

        query = ("INSERT INTO address "
                 "(house_number, street, city, state, zip_code)"
                 "VALUES (%s, %s, %s, %s, %s)")
        address = self.txt_Address.get()
        address = address.split(' ', 1)
        data_query = (address[0], address[1], self.txt_City.get(),
                      self.txt_State.get(), self.txt_ZipCode.get())
        print(data_query)
        cursor.execute(query, data_query)

        query = ("Select id "
                 "FROM address "
                 "Where house_number=%s and street=%s and city=%s and state=%s and zip_code=%s")
        cursor.execute(query, data_query)
        result = cursor.fetchall()

        query = ("INSERT INTO Buyer"
                 "(username, phone, address_id, default_payment, default_store_id) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data_query = (self.txt_UName.get(), self.txt_Phone.get(), result[0][0], "", 1)

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
