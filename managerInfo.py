import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import mysql.connector

def digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

class page_ManagerInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbl_Title = Label(self, text="Manager Account Information")

        self.lbl_FName = Label(self, text="First Name")
        self.lbl_LName = Label(self, text="Last Name")
        self.lbl_UName = Label(self, text="Username")
        self.lbl_Phone = Label(self, text="Phone")
        self.lbl_Store = Label(self, text="Managed Grocery Store")
        self.lbl_Addrs = Label(self, text="Grocery Store Address")
        self.lbl_Email = Label(self, text="Email")

        self.txt_FName = StringVar()
        self.txt_LName = StringVar()
        self.txt_UName = StringVar()
        self.txt_Phone = StringVar()
        self.txt_Store = StringVar()
        self.txt_Email = StringVar()
        self.txt_Addrs = StringVar()
        self.txt_Error = StringVar()

        self.ent_FName = Entry(self, textvariable=self.txt_FName, state='disabled')
        self.ent_LName = Entry(self, textvariable=self.txt_LName, state='disabled')
        self.ent_UName = Entry(self, textvariable=self.txt_UName, state='disabled')
        self.ent_Phone = Entry(self, textvariable=self.txt_Phone)
        self.ent_Addrs = Entry(self, textvariable=self.txt_Addrs)
        self.ent_Email = Entry(self, textvariable=self.txt_Email)

        self.btn_Back = Button(self, text="Back", command=self.back)
        self.btn_Delete = Button(self, text="Delete Account", command=self.delete)
        self.btn_Update = Button(self, text="Update", command=self.update)

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)

        query = ("SELECT store_name, house_number, street, city, state, zip_code, address.id "
                 "FROM groceryStore, address "
                 "WHERE groceryStore.address_id = address.id")
        cursor.execute(query)

        self.OPTIONS = cursor.fetchall()
        self.txt_Store = StringVar()

        self.opt_Store = OptionMenu(self, self.txt_Store, *self.OPTIONS)

        self.lbl_Title.grid(row=0,column=2)
        self.lbl_FName.grid(row=1,column=0)
        self.ent_FName.grid(row=1,column=1)
        self.lbl_LName.grid(row=1,column=3)
        self.ent_LName.grid(row=1,column=4)
        self.lbl_UName.grid(row=2,column=0)
        self.ent_UName.grid(row=2,column=1)
        self.lbl_Phone.grid(row=2,column=3)
        self.ent_Phone.grid(row=2,column=4)
        self.lbl_Store.grid(row=3,column=0)
        self.opt_Store.grid(row=3,column=1)
        self.lbl_Addrs.grid(row=4,column=0)
        self.ent_Addrs.grid(row=4,column=1)
        self.lbl_Email.grid(row=5,column=0)
        self.ent_Email.grid(row=5,column=1)
        self.btn_Back.grid(row=6,column=0)
        self.btn_Delete.grid(row=6,column=3)
        self.btn_Update.grid(row=6,column=4)

        query = ("SELECT first_name, last_name, email "
                 "FROM userr "
                 "WHERE userr.username = %s")
        data_query = (self.controller.shared_data["username"].get(),)

        cursor.execute(query, data_query)
        results = cursor.fetchone()

        self.txt_UName.set(self.controller.shared_data["username"].get())
        if cursor.rowcount == 1:
            self.txt_FName.set(results[0])
            self.txt_LName.set(results[1])
            self.txt_Email.set(results[2])

        query = ("SELECT phone, address_id, house_number, street "
                 "FROM manages, address, grocerystore "
                 "WHERE manages.username=%s and grocerystore.address_id = store_address "
                 "and address.id = grocerystore.address_id")
        cursor.execute(query, data_query)
        results = cursor.fetchone()

        if cursor.rowcount == 1:
            self.txt_Phone.set(results[0])
            self.txt_Addrs.set(str(results[2]) + ' ' + str(results[3]))

            counter = 0
            for x in self.OPTIONS:
                if x[6] == results[1]:
                    break
                else:
                    counter += 1
            self.txt_Store.set(self.OPTIONS[counter])

    def back(self):
        self.controller.show_frame("page_ManagerFunctionality")

    def delete(self):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)

        query="DELETE FROM `userr` WHERE username = %s"
        data_query = (self.controller.shared_data["username"].get(),)
        cursor.execute(query, data_query)

        try:
            cnx.commit()
        except mysql.connector.Error as err:
            self.txt_Error.set("Error Deleting Person: " + err)
            print("Error Deleting Person: " + err)
            return
        self.controller.show_frame("page_LoginMenu")

    def update(self):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)

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

        query = ("UPDATE userr SET email = %s, phone = %s WHERE username=%s")
        query_data = (self.txt_Email.get(), phoneNumber, self.controller.shared_data["username"].get())
        cursor.execute(query,query_data)

        query = ("SELECT phone, address_id, house_number, street "
                 "FROM manages, address, grocerystore "
                 "WHERE manages.username=%s and grocerystore.address_id = store_address "
                 "and address.id = grocerystore.address_id")
        query_data = (self.controller.shared_data["username"].get(),)
        cursor.execute(query,query_data)

        results = cursor.fetchone()

        query = ("UPDATE groceryStore SET phone=%s WHERE address_id=%s")
        query_data = (phoneNumber, results[1])
        cursor.execute(query,query_data)

        query = ("UPDATE address Set house_number=%s, street=%s WHERE id=%s")
        address = self.txt_Addrs.get()
        address = address.split(' ', 1)
        query_data = (address[0],address[1],results[1])

        cursor.execute(query,query_data)

        try:
            cnx.commit()
        except mysql.connector.Error as err:
            self.txt_Error.set("Error Updating Person: " + err)
            print("Error Updating Person: " + err)
            return

        cursor.close()
        cnx.close()
        self.controller.show_frame("page_ManagerInfo")
