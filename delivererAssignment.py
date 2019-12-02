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

class page_DelivererAssignment(tk.Frame):
    def back(self):
        self.controller.show_frame("page_DelivererAssign")

    def update(self):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor()
        query = ("UPDATE deliveredby SET deliveredby.is_delivered = 0 "
              "where order_id = %s")
        data_query=(int(self.controller.shared_data["selectedTv"].get()),)
        cursor.execute(query, data_query)
        try:
            cnx.commit()
        except mysql.connector.Error as err:
            print("Error Updating: " + err)
            return

        cursor.close()
        cnx.close()
        self.controller.show_frame("page_DelivererAssignment")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbl_Title = Label(self, text="Assignment")

        self.lbl_Place = Label(self, text="Order Place")
        self.lbl_DTime = Label(self, text="Delivery Time")
        self.lbl_Stats = Label(self, text="Status")
        self.lbl_Addrs = Label(self, text="Buyer Address")
        self.lbl_Sname = Label(self, text="Store Name")

        self.txt_Place = StringVar()
        self.txt_DTime = StringVar()
        self.txt_Stats = StringVar()
        self.txt_Addrs = StringVar()
        self.txt_Sname = StringVar()

        self.ent_Place = Entry(self, state="disabled", textvariable=self.txt_Place)
        self.ent_DTime = Entry(self, state="disabled", textvariable=self.txt_DTime)
        self.ent_Stats = Entry(self, state="disabled", textvariable=self.txt_Stats)
        self.ent_Addrs = Entry(self, state="disabled", textvariable=self.txt_Addrs)
        self.ent_Sname = Entry(self, state="disabled", textvariable=self.txt_Sname)

        self.lbl_IName = Label(self, text="Item Name")
        self.lbl_Quant = Label(self, text="Quantity")

        self.tv_Assignments = Treeview(self)
        self.tv_Assignments['columns'] = ('Quantity')
        self.tv_Assignments.heading('#0', text='Item Name')
        self.tv_Assignments.column('#0', anchor="w")
        self.tv_Assignments.heading('Quantity', text='Quantity')
        self.tv_Assignments.column('Quantity', anchor="w")

        self.btn_Back = Button(self, text="Back", command=self.back)
        self.btn_Update = Button(self, text="Update", command=self.update)

        self.lbl_Title.grid(row=0,column=2)
        self.lbl_Place.grid(row=1,column=0)
        self.ent_Place.grid(row=1,column=1)
        self.lbl_DTime.grid(row=2,column=0)
        self.ent_DTime.grid(row=2,column=1)
        self.lbl_Stats.grid(row=3,column=0)
        self.ent_Stats.grid(row=3,column=1)
        self.lbl_Addrs.grid(row=4,column=0)
        self.ent_Addrs.grid(row=4,column=1)
        self.lbl_Sname.grid(row=5,column=0)
        self.ent_Sname.grid(row=5,column=1)
        self.btn_Back.grid(row=6,column=0)
        self.btn_Update.grid(row=6,column=4)
        self.lbl_IName.grid(row=1,column=3)
        self.lbl_Quant.grid(row=1,column=4)
        self.tv_Assignments.grid(row=2,column=3,rowspan=2,columnspan=4)

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor()

        query = ("SELECT orderr.order_placed_time, orderr.delivery_time, deliveredby.is_delivered, address.house_number, address.street, address.city, address.state, address.zip_code "
                "FROM orderr, deliveredby, address, buyer, orderedby "
                "WHERE orderr.order_id = %s AND deliveredby.order_id = %s AND buyer.address_id =  address.id AND buyer.username = orderedby.buyer_username AND orderedby.order_id = %s")
        data_query = (self.controller.shared_data["selectedTv"].get(),self.controller.shared_data["selectedTv"].get(),self.controller.shared_data["selectedTv"].get())
        cursor.execute(query, data_query,)
        a = cursor.fetchall()
        self.txt_Place.set(a)
        self.txt_DTime.set(a)
        if a == 1:
            self.txt_Stats.set("Pending")
        else:
            self.txt_Stats.set("Delivered")
        address = str(a) + " " + str(a) + " " + str(a) + " " + str(a) + " " + str(a)
        self.txt_Addrs.set(address)
        query = ("SELECT store_name FROM grocerystore, orderfrom WHERE store_address_id = store_id and orderfrom.order_id = %s")
        data_query = (self.controller.shared_data["selectedTv"].get(),)
        cursor.execute(query, data_query)
        results = cursor.fetchall()
        self.txt_Sname.set(results)

        query = ("SELECT item.item_name, selectitem.quantity "
                 "FROM  selectitem, item "
                "WHERE selectitem.order_id = %s AND selectitem.item_id = item.item_id")
        data_query = (self.controller.shared_data["selectedTv"].get(),)
        cursor.execute(query, data_query)
        results = cursor.fetchall()
        for x in results:
            self.tv_Assignments.insert('','end',text=x[0], values=(x[1]))
