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
from tkcalendar import DateEntry
from Utill.const import CURRENT_SELECTED_ID

class SalesManagmentPage:
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
      
        # Label
        l4 = Label(self.root, text='Order Managment  ', foreground='white', background='cyan4',
                   activebackground='Light Blue', font=('Times New Roman', 45, 'bold'))
        l4.place(x=500, y=50)

       
        self.table = ttk.Treeview(self.root)
        self.table.pack()

        s = ttk.Style(self.root)
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        self.table['columns'] = ('OrderId', 'Date', 'Price', 'Address', 'State','City', 'Zipcode','OrderStatus','Action')
        self.table.column('#0', width=0, stretch=0)
        self.table.column('OrderId', anchor=W, width=50)
        self.table.column('Date', anchor=W, width=50)
        self.table.column('Price', anchor=W, width=50)
        self.table.column('Address', anchor=W, width=50)
        self.table.column('State', anchor=W, width=80)
        self.table.column('City', anchor=W, width=80)
        self.table.column('Zipcode', anchor=W, width=80)
        self.table.column('OrderStatus', anchor=W, width=50)
        self.table.column('Action',  anchor=W, width=50)
       

        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('OrderId', text='Order ID', anchor=CENTER)
        self.table.heading('Date', text='Date', anchor=CENTER)
        self.table.heading('Price', text='Price', anchor=CENTER)
        self.table.heading('Address', text='Address', anchor=CENTER)
        self.table.heading('State', text='State', anchor=CENTER)
        self.table.heading('City', text='City', anchor=CENTER)
        self.table.heading('Zipcode', text='Zipcode', anchor=CENTER)
        self.table.heading('OrderStatus', text='Order Status', anchor=CENTER)
        self.table.heading('Action', text='Action', anchor=CENTER)
    
        self.table.place(x=30, y=260, width=1300, height=380)

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

        self.start_date_label = Label(self.root, text="Start Date:",font=('Times new Roman', 18))
        self.start_date_label.place(x=50, y=200)
        self.start_date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white',  font=('Times new Roman', 18))
        self.start_date_entry.place(x=250, y=200)

        self.end_date_label = Label(self.root, text="End Date:", font=('Times new Roman', 18))
        self.end_date_label.place(x=500, y=200)
        self.end_date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', font=('Times new Roman', 18))
        self.end_date_entry.place(x=600, y=200)

        

        self.b3 = Button(self.root, text='    Search  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                    bg='cadetblue3', bd=5, command=self.update)
        self.b3.place(x=800, y=200)

        self.amount_label = Label(self.root, text="Total Amount:", font=('Times new Roman', 18))
        self.amount_label.place(x=800, y=625)
        self.total_amount = StringVar()
        self.total_amount.set("")
        self.s8 = Entry(self.root, textvariable=self.total_amount, font=('Times new Roman', 17),state='readonly')
        self.s8.place(x=1000, y=625)

        self.re1 = Button(self.root, text='    RESET  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                      bg='cadetblue3', bd=5, command=self.reset)
        self.re1.place(x=970, y=200)
       
    
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
            start_date_value =  self.start_date_entry.get_date()
            end_date_value = self.end_date_entry.get_date()
            self.total_amount.set(self.order_repository.get_total_amount_in_date_range(start_date_value,end_date_value))
            re=self.order_repository.get_orders_in_date_range(start_date_value,end_date_value)
            self.table.delete(*self.table.get_children())
            for order in re:
                shipinfo=self.shipping_repository.get_shipping_info_by_id(order.shipping_id)
                self.table.insert(parent='', index='end', text='',
                            values=(order.order_id,order.order_date,order.price, shipinfo.address, shipinfo.state,shipinfo.city, shipinfo.zip_code,order.orderstatus))

           
    def reset(self):
        self.query_database()
    
    def select(self,e):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            print(values1)
         
