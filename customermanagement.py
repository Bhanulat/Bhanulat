from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

from Model.shipping_info import ShippingInfo
from Repository.shipping_info_repository import ShippingInfoRepository

from Model.user import User
from Repository.user_repository import UserRepository



from Utill.const import CURRENT_SELECTED_ID

class CustomerManagmentPage:
    def __init__(self, master):
        self.root = master
        self.root.state('zoomed')
        self.root.title('Customer Books Management')
      
        
        self.shipping_repository = ShippingInfoRepository()
        self.user_repository = UserRepository()
      

        self.create_widgets()
    def create_widgets(self):
        # Canvas 1
        canvas = Canvas(self.root, width=1920, height=120)
        canvas.pack()
        r1 = canvas.create_rectangle(0, 0, 1920, 150, outline='cyan4', fill='cyan4')
        canvas.update()

        # Canvas 2
        canvas2 = Canvas(self.root, width=1500, height=290)
        canvas2.pack()
      

        # Treeview
        self.ordertable = ttk.Treeview(self.root)
        self.ordertable.pack()

        s = ttk.Style(self.root)
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        self.ordertable['columns'] = ( 'Address', 'State', 'City', 'Zipcode')
        self.ordertable.column('#0', width=0, stretch=0)
        self.ordertable.column('Address', anchor=W, width=50)
        self.ordertable.column('State', anchor=W, width=80)
        self.ordertable.column('City', anchor=W, width=80)
        self.ordertable.column('Zipcode', anchor=W, width=80)
       

        self.ordertable.heading('#0', text='', anchor=CENTER)
        self.ordertable.heading('Address', text='Address', anchor=CENTER)
        self.ordertable.heading('State', text='State', anchor=CENTER)
        self.ordertable.heading('City', text='City', anchor=CENTER)
        self.ordertable.heading('Zipcode', text='Zipcode', anchor=CENTER)
       

    
        self.ordertable.place(x=40, y=450, width=1300, height=250)

        # Scrollbar
        vsb = ttk.Scrollbar(self.ordertable, orient='vertical')
        vsb.configure(command=self.ordertable.yview)
        self.ordertable.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side=RIGHT)

        s = ttk.Style(self.root)
        s.theme_use("clam")
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        # Label
        l4 = Label(self.root, text='Order Managment  ', foreground='white', background='cyan4',
                   activebackground='Light Blue', font=('Times New Roman', 45, 'bold'))
        l4.place(x=500, y=20)

       
        self.table = ttk.Treeview(self.root)
        self.table.pack()

        s = ttk.Style(self.root)
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        self.table['columns'] = ('CustomerId', 'Name', 'EMail', 'Mobile')
        self.table.column('#0', width=0, stretch=0)
        self.table.column('CustomerId', anchor=W, width=50)
        self.table.column('Name', anchor=W, width=50)
        self.table.column('EMail', anchor=W, width=50)
        self.table.column('Mobile', anchor=W, width=50)
       


        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('CustomerId', text='Order ID', anchor=CENTER)
        self.table.heading('Name', text='Name', anchor=CENTER)
        self.table.heading('EMail', text='Email', anchor=CENTER)
        self.table.heading('Mobile', text='Mobile', anchor=CENTER)
        
        self.table.place(x=30, y=150, width=1300, height=200)

        # Scrollbar
        vsb = ttk.Scrollbar(self.table, orient='vertical')
        vsb.configure(command=self.table.yview)
        self.table.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side=RIGHT)

        s = ttk.Style(self.root)
        s.theme_use("clam")
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        self.b1 = Button(canvas, text='   BACK   ', width=10, bd=5, relief=RIDGE, background="white", command=self.back,
                    font=('Times New Roman', 15, 'bold'), bg='Light Grey')
        self.b1.place(x=20, y=40)

       
       
    
        # Binding
        self.table.bind("<ButtonRelease-1>", self.select)

        # Initial Query to populate Treeview
        self.query_database()

    def back(self):
         self.root.destroy()
         from homepage import HomeAdminPage
         HomeAdminPage(Tk())

    def query_database(self):
        self.table.delete(*self.table.get_children())
        get_all_customer=self.user_repository.get_users()
       
        for customer in get_all_customer:
          
            self.table.insert(parent='', index='end', text='',
                        values=(customer.user_id,customer.first_name+" "+customer.last_name,customer.email, customer.phone))
    
    def select(self,e):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            print(values1)
            shipinfo=self.shipping_repository.get_shipping_info_by_customer_id(values1[0])
            self.ordertable.delete(*self.ordertable.get_children())
            for shipadd in shipinfo:
                
                self.ordertable.insert(parent='', index='end', text='',
                            values=(shipadd.address,    
                                    shipadd.state,shipadd.city,shipadd.zip_code))

