from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from Model.books import Books
from Repository.books_repository import BooksRepository

from Model.cart import Cart
from Repository.cart_repository import CartRepository
from Model.shipping_info import ShippingInfo
from Repository.shipping_info_repository import ShippingInfoRepository

from Model.order import Order
from Repository.order_repository import OrderRepository

from Model.payment import Payment
from Repository.payment_repository import PaymentRepository

from Model.order_items import OrderItems
from Repository.order_items_repository import OrderItemsRepository

from Utill.const import CURRENT_SELECTED_ID

class OrderManagmentPage:
    def __init__(self, master):
        self.root = master
        self.root.state('zoomed')
        self.root.title('Books Management')
      
        self.book_repository = BooksRepository()
        self.cart_repository = CartRepository()
        self.shipping_repository = ShippingInfoRepository()
        self.payment_repository = PaymentRepository()
        self.order_repository = OrderRepository()
        self.orderitem_repository = OrderItemsRepository()

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

        self.ordertable['columns'] = ('OrderItemId', 'BookName', 'Author', 'Edition', 'Description', 'Quantity', 'Price')
        self.ordertable.column('#0', width=0, stretch=0)
        self.ordertable.column('OrderItemId', anchor=W, width=50)
        self.ordertable.column('BookName', anchor=W, width=50)
        self.ordertable.column('Author', anchor=W, width=80)
        self.ordertable.column('Edition', anchor=W, width=80)
        self.ordertable.column('Description', anchor=W, width=80)
        self.ordertable.column('Quantity', anchor=W, width=50)
        self.ordertable.column('Price', anchor=W, width=100)

        self.ordertable.heading('#0', text='', anchor=CENTER)
        self.ordertable.heading('OrderItemId', text='Order Item ID', anchor=CENTER)
        self.ordertable.heading('BookName', text='Book Name', anchor=CENTER)
        self.ordertable.heading('Author', text='Author Name', anchor=CENTER)
        self.ordertable.heading('Edition', text='Edition', anchor=CENTER)
        self.ordertable.heading('Description', text='Description', anchor=CENTER)
        self.ordertable.heading('Quantity', text='Quantity', anchor=CENTER)
        self.ordertable.heading('Price', text='Price', anchor=CENTER)
       

    
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

        self.table['columns'] = ('OrderId', 'Date', 'Price', 'Address', 'State','City', 'Zipcode','OrderStatus')
        self.table.column('#0', width=0, stretch=0)
        self.table.column('OrderId', anchor=W, width=50)
        self.table.column('Date', anchor=W, width=50)
        self.table.column('Price', anchor=W, width=50)
        self.table.column('Address', anchor=W, width=50)
        self.table.column('State', anchor=W, width=80)
        self.table.column('City', anchor=W, width=80)
        self.table.column('Zipcode', anchor=W, width=80)
        self.table.column('OrderStatus', anchor=W, width=50)
       
       

        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('OrderId', text='Order ID', anchor=CENTER)
        self.table.heading('Date', text='Date', anchor=CENTER)
        self.table.heading('Price', text='Price', anchor=CENTER)
        self.table.heading('Address', text='Address', anchor=CENTER)
        self.table.heading('State', text='State', anchor=CENTER)
        self.table.heading('City', text='City', anchor=CENTER)
        self.table.heading('Zipcode', text='Zipcode', anchor=CENTER)
        self.table.heading('OrderStatus', text='Order Status', anchor=CENTER)
        
    
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

        e13 = ['Dispatched', 'Delivered']
        self.combobox = ttk.Combobox(self.root, values=e13, font=('Times New Roman', 18, "bold"))
        self.combobox.place(x=50, y=400, width=200, height=35)
        self.combobox.set('Order Staus')

        self.b3 = Button(self.root, text='    Update Status  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                    bg='cadetblue3', bd=5, command=self.update)
        self.b3.place(x=300, y=400)
       
    
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
        get_all_order=self.order_repository.get_orders()
       
        for order in get_all_order:
            shipinfo=self.shipping_repository.get_shipping_info_by_id(order.shipping_id)
            self.table.insert(parent='', index='end', text='',
                        values=(order.order_id,order.order_date,order.price, shipinfo.address, shipinfo.state,shipinfo.city, shipinfo.zip_code,order.orderstatus))
    def update(self):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            selected_value = self.combobox.get()
            self.order_repository.update_order_status(values1[0],selected_value)
            self.query_database()
           
 
    def select(self,e):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            print(values1)
            self.ordertable.delete(*self.ordertable.get_children())
            get_all_order=self.orderitem_repository.get_order_items_by_order_id(values1[0])
            for order in get_all_order:
                bookinfo=self.book_repository.get_by_id(order.book_id)
                self.ordertable.insert(parent='', index='end', text='',
                            values=(order.order_items_id,    
                                    bookinfo.book_name, bookinfo.author, bookinfo.book_edition, bookinfo.description, order.qty,order.price))


           
