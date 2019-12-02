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

class page_DelivererAssign(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbl_Title = Label(self, text="Assignments")

        self.btn_Back = Button(self, text="Back", command=self.back)
        self.btn_View = Button(self, text="View Assignment Details", command=self.view)

        self.tv_Assignments = Treeview(self)
        self.tv_Assignments['columns'] = ('Store Address','Order id',
                                    'Date', 'Time Order Made', 'Time of Delivery',
                                    'Order Price', 'Total Number of Items')
        self.tv_Assignments.heading('#0', text='Store Name')
        self.tv_Assignments.column('#0', anchor="w")
        self.tv_Assignments.heading('Store Address', text='Store Address')
        self.tv_Assignments.column('Store Address', anchor="w")
        self.tv_Assignments.heading('Order id', text='Order id')
        self.tv_Assignments.column('Order id', anchor="w")
        self.tv_Assignments.heading('Date', text='Date')
        self.tv_Assignments.column('Date', anchor="w")
        self.tv_Assignments.heading('Time Order Made', text='Time Order Made')
        self.tv_Assignments.column('Time Order Made', anchor="w")
        self.tv_Assignments.heading('Time of Delivery', text='Time of Delivery')
        self.tv_Assignments.column('Time of Delivery', anchor="w")
        self.tv_Assignments.heading('Order Price', text='Order Price')
        self.tv_Assignments.column('Order Price', anchor="w")
        self.tv_Assignments.heading('Total Number of Items', text='Total Number of Items')
        self.tv_Assignments.column('Total Number of Items', anchor="w")

        self.lbl_Title.grid(row=0,column=1)
        self.tv_Assignments.grid(row=1,column=0,columnspan=4)
        self.btn_Back.grid(row=2,column=0)
        self.btn_View.grid(row=2,column=3)

        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1', database='grocerybama')
        cursor = cnx.cursor(buffered=True)

        query = ("SELECT store_name, orderfrom.order_id, delivery_time, delivery_date, address_id "
                 "FROM deliveredby, orderfrom, grocerystore "
                 "WHERE is_delivered = 1 AND deliverer_username = %s AND orderfrom.order_id=deliveredby.order_id "
                 "and orderfrom.store_address_id=store_id")
        data_query = (self.controller.shared_data["username"].get(),)
        cursor.execute(query, data_query)
        results = cursor.fetchall()

        query = ("SELECT COUNT(selectitem.quantity), SUM(selectitem.quantity*item.listed_price), order_placed_time, house_number, "
                "street, city "
                "FROM selectitem, item, deliveredby, orderr, address "
                "WHERE deliveredby.order_id = %s AND item.item_id = selectitem.item_id AND "
                "deliveredby.deliverer_username = %s and deliveredby.order_id = selectitem.order_id AND "
                "orderr.order_id = deliveredby.order_id and address.id = %s")



        for x in results:
            data_query = (x[1], self.controller.shared_data["username"].get(), x[4])
            cursor.execute(query, data_query)
            result2 = cursor.fetchone()
            address_String = str(result2[3]) + " " + str(result2[4]) + " " + str(result2[5])
            self.tv_Assignments.insert('','end',text=x[0], values=(address_String,x[1],x[3],result2[2],x[2],result2[1],result2[0]))

    def back(self):
        self.controller.show_frame("page_delivererFunctionality")

    def view(self):
        viewDict = self.tv_Assignments.item(self.tv_Assignments.selection())['values']
        var = viewDict[1]
        #print(viewDict['values'][1])
        print(var)
        self.controller.shared_data["selectedTv"].set(var)
        self.controller.show_frame("page_DelivererAssignment")
