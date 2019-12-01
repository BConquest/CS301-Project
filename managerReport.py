import tkinter as tk
from tkinter import *
import mysql.connector

class page_ManagerReport(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbl_Title = tk.Label(self, text="Revenue Report")
        self.lbl_Store = tk.Label(self, text="Store Name")
        self.lbl_Number = tk.Label(self, text="Number of Items Sold")
        self.lbl_Profit = tk.Label(self, text="Total Profit")

        self.txt_Store = StringVar()
        self.txt_Number = StringVar()
        self.txt_Profit = StringVar()

        self.ent_Store = tk.Entry(self, textvariable=self.txt_Store, state='disabled')
        self.ent_Number = tk.Entry(self, textvariable=self.txt_Number, state='disabled')
        self.ent_Profit = tk.Entry(self, textvariable=self.txt_Profit, state='disabled')

        self.btn_Back = tk.Button(self, text="Back", command=self.back)

        self.lbl_Title.grid(row=0,column=1)
        self.lbl_Store.grid(row=1,column=0)
        self.ent_Store.grid(row=1,column=2)
        self.lbl_Number.grid(row=2,column=0)
        self.ent_Number.grid(row=2,column=2)
        self.lbl_Profit.grid(row=3,column=0)
        self.ent_Profit.grid(row=3,column=2)
        self.btn_Back.grid(row=4,column=0)

        results = self.generateRevenuReport(self.controller.shared_data["username"].get())
        self.txt_Store.set(results[0])
        self.txt_Number.set(results[1])
        self.txt_Profit.set(results[2])

    def back(self):
        self.controller.show_frame("page_ManagerFunctionality")

    def generateRevenuReport(self, username):
        results = ["","",""]
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)
        query = (
        "Select store_id, store_name "
        "From grocerystore, manages "
        "WHERE grocerystore.store_id = manages.store_address AND manages.username = %s"
        )
        data_query = (username,)
        cursor.execute(query, data_query)
        result = cursor.fetchone()
        print(result, end="\t")
        print(type(result))
        results[0] = result

        query = (
        "SELECT sum(quantity) "
        "FROM orderfrom, selectitem "
        "WHERE orderfrom.store_address_id = %s AND orderfrom.order_id = selectitem.order_id"
        )
        data_query = (result,)

        cursor.execute(query, data_query)
        results[0] = result
        return results
