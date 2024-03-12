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

class CheckoutPage:
    def __init__(self, master,customerid,name,email):
        self.root = master
        self.root.state('zoomed')
        self.root.title('Books Management')
        self.custid=customerid
        self.name=name
        self.email=email
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
        r2 = canvas2.create_rectangle(25, 10, 1350, 250, outline='Black')
        canvas2.update()

        # Treeview
        self.table = ttk.Treeview(self.root)
        self.table.pack()

        s = ttk.Style(self.root)
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        self.table['columns'] = ('ShippingID', 'Address', 'State', 'City', 'Zipcode')
        self.table.column('#0', width=0, stretch=0)
        self.table.column('ShippingID', anchor=W, width=50)
        self.table.column('Address', anchor=W, width=50)
        self.table.column('State', anchor=W, width=80)
        self.table.column('City', anchor=W, width=80)
        self.table.column('Zipcode', anchor=W, width=80)
       

        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('ShippingID', text='Shipping ID', anchor=CENTER)
        self.table.heading('Address', text='Address', anchor=CENTER)
        self.table.heading('State', text='State', anchor=CENTER)
        self.table.heading('City', text='City', anchor=CENTER)
        self.table.heading('Zipcode', text='Zipcode', anchor=CENTER)
    
        self.table.place(x=40, y=450, width=1300, height=250)

        # Scrollbar
        vsb = ttk.Scrollbar(self.table, orient='vertical')
        vsb.configure(command=self.table.yview)
        self.table.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side=RIGHT)

        s = ttk.Style(self.root)
        s.theme_use("clam")
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        # Label
        l4 = Label(self.root, text='Books Mart', foreground='white', background='cyan4',
                   activebackground='Light Blue', font=('Times New Roman', 45, 'bold'))
        l4.place(x=500, y=20)

        # Labels and Entry Widgets
        l1 = Label(self.root, text='Address : ', font=('Times new Roman', 18))
        l1.place(x=50, y=170)
        self.address = StringVar()
        self.e1 = Entry(self.root, textvariable=self.address, font=('Times', 17))
        self.e1.place(x=230, y=170)

        l3 = Label(self.root, text='State', font=('Times new Roman', 18))
        l3.place(x=480, y=170)
        self.state = StringVar()
        self.e3 = Entry(self.root, textvariable=self.state, font=('Times new Roman', 17))
        self.e3.place(x=700, y=170)

        l5 = Label(self.root, text='City', font=('Times new Roman', 18))
        l5.place(x=50, y=230)
        self.city = StringVar()
        self.e5 = Entry(self.root, textvariable=self.city, font=('Times new Roman', 17))
        self.e5.place(x=230, y=230)

        l6 = Label(self.root, text='Zipcode: ', font=('Times new Roman', 18))
        l6.place(x=480, y=230)
        self.zipcode = StringVar()
        self.e6 = Entry(self.root, textvariable=self.zipcode, font=('Times new Roman', 17))
        self.e6.place(x=700, y=230)

        l8 = Label(self.root, text='PaymentMode: ', font=('Times new Roman', 18))
        l8.place(x=970, y=230)
        self.payment = ['CashOnDelivery']
        self.combobox = ttk.Combobox(self.root, values=self.payment, font=('Times New Roman', 18, "bold"))
        self.combobox.place(x=1120, y=230, width=160, height=35)
        self.combobox.set('')

        l14 = Label(self.root, text='Date: ', font=('Times New Roman', 18))
        l14.place(x=970, y=170)
        self.e14 = Entry(self.root, width=20, font=('Times New Roman', 17))
        self.e14.place(x=1070, y=170)
        self.my_time()
        to14 = Label(self.root, text='Total : ', font=('Times New Roman', 18))
        to14.place(x=50, y=400,width=200)

        self.total_amount = StringVar()
        self.total_amount.set("")
        self.s8 = Entry(self.root, textvariable=self.total_amount, font=('Times new Roman', 17),state='readonly')
        self.s8.place(x=300, y=400)

        # Buttons
        self.b1 = Button(canvas, text='   BACK   ', width=10, bd=5, relief=RIDGE, background="white", command=self.back,
                    font=('Times New Roman', 15, 'bold'), bg='Light Grey')
        self.b1.place(x=20, y=40)

        self.b2 = Button(self.root, text='  UPDATE  ', relief=RIDGE, width=10, font=('Times New Roman', 15, 'bold'),
                    bg='cadetblue3', bd=5, command=self.updatebutton)
        self.b2.place(x=1080, y=400)

        self.b3 = Button(self.root, text='    ORDERNOW  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                    bg='cadetblue3', bd=5, command=self.ordernow)
        self.b3.place(x=670, y=400)

        

        self.b4 = Button(self.root, text='     ADDNEW   ', relief=RIDGE, width=10, font=('Times New Roman', 15, 'bold'),
                     bg='cadetblue3', command=self.save, bd=5)
        self.b4.place(x=600, y=290)

        self.b6 = Button(self.root, text='  DELETE  ', relief=RIDGE, width=10, bd=5, font=('Times New Roman', 15, 'bold'),
                     bg='cadetblue3', command=self.delete)
        self.b6.place(x=1210, y=400)

        self.b7 = Button(self.root, text='   CLEAR   ', relief=RIDGE, width=10, bd=5,
                     font=('Times New Roman', 15, 'bold'), bg='cadetblue3', command=self.clear)
        self.b7.place(x=800, y=290)

        # Combobox and Entry for searching
        

        # Binding
        self.table.bind("<ButtonRelease-1>", self.select)

        # Initial Query to populate Treeview
        self.query_database()

    def back(self):
         self.root.destroy()
         from userhomepage import HomeUserPage
         HomeUserPage(Tk(),self.custid,self.name,self.email)
       

    def clear(self):
        self.e1.delete(0, END)
        self.e3.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
       
       

    def query_database(self):
        self.table.delete(*self.table.get_children())
        get_all_shipping=self.shipping_repository.get_shipping_info_by_customer_id(self.custid)
        self.total_amount.set(self.cart_repository.get_total_amount(self.custid))
        for shipinfo in get_all_shipping:
            print(shipinfo.address)
            self.table.insert(parent='', index='end', text='',
                        values=(shipinfo.shipping_id,shipinfo.address, shipinfo.state,shipinfo.city, shipinfo.zip_code))

    def save(self):
        address=self.e1.get()
        state=self.e3.get()
        city=self.e5.get()
        zipcode=self.e6.get()
        
        if(address==""):
            messagebox.showerror("Required", "Please fill  Address")
        elif(state==""):
            messagebox.showerror("Required", "Please fill State")
        elif(city==""):
            messagebox.showerror("Required", "Please fill City")
        elif(zipcode==""):
            messagebox.showerror("Required", "Please fill Zipcode")
      
        else:
            time_string = datetime.now()
            shipping = ShippingInfo(None, time_string,address, state,city,zipcode ,self.custid)
            self.shipping_repository.add_shipping_info(shipping)
            messagebox.showinfo('Shipping Address', 'Successfully Add')
            self.query_database()
            

    def my_time(self):
        time_string = datetime.now().strftime('         %x ')
        self.e14.delete(0,END)
        self.e14.insert(0,time_string)
        self.e14.after(1000,self.my_time)

    def updatebutton(self):
            address=self.e1.get()
            state=self.e3.get()
            city=self.e5.get()
            zipcode=self.e6.get()
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            time_string = datetime.now()
            shipping = ShippingInfo(None, time_string,address, state,city,zipcode ,self.custid)
            self.shipping_repository.update_shipping_info(values1[0],shipping)
            messagebox.showinfo('Shipping Address Update', 'Successfully  Update ')
            self.query_database()
    def ordernow(self):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            shippingid=values1[0]
            customerid=self.custid
            method = self.combobox.get()
            if(method==""):
                 method="CashonDelivery"
            time_string = datetime.now()
            paymentinfo = Payment(None, time_string,method, self.cart_repository.get_total_amount(self.custid),self.custid)
            paymentid=self.payment_repository.add_payment(paymentinfo)
            ordergenerate=Order(None, time_string,self.cart_repository.get_total_amount(self.custid),self.custid,paymentid,shippingid)
            orderid=self.order_repository.add_order(ordergenerate)
            get_all_book=self.cart_repository.get_carts_by_user(self.custid)
            for bookinfo_cart in get_all_book:
                 bookdetails=self.book_repository.get_by_id(bookinfo_cart.book_id)
                 price=float(bookdetails.price)*float(bookinfo_cart.qty)
                 orderitem=OrderItems(None,bookinfo_cart.qty,price,orderid,bookinfo_cart.book_id)
                 self.orderitem_repository.add_order_item(orderitem)
                 self.book_repository.update_book_stock(bookinfo_cart.book_id,bookinfo_cart.qty)
            self.cart_repository.delete_cart_entry_cusid(customerid)
            messagebox.showinfo('Order Status', 'Order Sucessfully')
            self.root.destroy()
            from userhomepage import HomeUserPage
            HomeUserPage(Tk(),self.custid,self.name,self.email)

    def select(self,e):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            print(values1)
            self.address.set(values1[1])
            self.state.set(values1[2])
            self.city.set(values1[3])
            self.zipcode.set(values1[4])
            self.total_amount.set(self.cart_repository.get_total_amount(self.custid))
            CURRENT_SELECTED_ID=values1[0]

    def delete(self):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            self.shipping_repository.delete_shipping_info_by_id(values1[0])
            messagebox.showinfo('ShippingInfo Delete', 'Successfully  Delete Shipping Info')
            self.query_database()
   
       
