from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from Model.books import Books
from Model.cart import Cart
from Repository.cart_repository import CartRepository
from Repository.books_repository import BooksRepository
from Utill.const import CURRENT_SELECTED_ID

class BooksShoppingCartPage:
    def __init__(self, master,customerid,name,email):
        self.root = master
        self.root.state('zoomed')
        self.cusid = customerid
        self.name=name
        self.email=email
        self.root.title('Books Shopping Cart')
        self.cart_repository = CartRepository()
        self.book_repository = BooksRepository()
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

        self.table['columns'] = ('CartId', 'Quantity', 'BookId')
        self.table.column('#0', width=0, stretch=0)
        self.table.column('CartId', anchor=W, width=50)
        self.table.column('Quantity', anchor=W, width=50)
        self.table.column('BookId', anchor=W, width=80)
       

        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('CartId', text='Cart ID', anchor=CENTER)
        self.table.heading('Quantity', text='Quantity', anchor=CENTER)
        self.table.heading('BookId', text='BookId', anchor=CENTER)
      
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
        l1 = Label(self.root, text='Book Name : ', font=('Times new Roman', 18))
        l1.place(x=50, y=170)
        self.bookname = StringVar()
        self.e1 = Entry(self.root, textvariable=self.bookname, font=('Times', 17),state='readonly')
        self.e1.place(x=230, y=170)

        l3 = Label(self.root, text='Author Name', font=('Times new Roman', 18))
        l3.place(x=480, y=170)
        self.authorname = StringVar()
        self.e3 = Entry(self.root, textvariable=self.authorname, font=('Times new Roman', 17),state='readonly')
        self.e3.place(x=700, y=170)

        l5 = Label(self.root, text='Book Edition', font=('Times new Roman', 18))
        l5.place(x=50, y=230)
        self.edition = StringVar()
        self.e5 = Entry(self.root, textvariable=self.edition, font=('Times new Roman', 17),state='readonly')
        self.e5.place(x=230, y=230)

        l6 = Label(self.root, text='Quantity: ', font=('Times new Roman', 18))
        l6.place(x=480, y=230)
        self.quantity = StringVar()
        self.e6 = Entry(self.root, textvariable=self.quantity, font=('Times new Roman', 17))
        self.e6.place(x=700, y=230)
        self.e6.bind("<KeyRelease>", self.textbox_changed)

        l8 = Label(self.root, text='Price: ', font=('Times new Roman', 18))
        l8.place(x=970, y=230)
        self.price = StringVar()
        self.e8 = Entry(self.root, textvariable=self.price, font=('Times new Roman', 17),state='readonly')
        self.e8.place(x=1070, y=230)

        l9 = Label(self.root, text='Description: ', font=('Times', 18))
        l9.place(x=50, y=290)
        self.description = StringVar()
        self.e9 = Entry(self.root, textvariable=self.description, font=('Times', 15),state='readonly')
        self.e9.place(x=230, y=290, width=350, height=50)

        l14 = Label(self.root, text='Date: ', font=('Times New Roman', 18))
        l14.place(x=970, y=170)
        self.e14 = Entry(self.root, width=20, font=('Times New Roman', 17))
        self.e14.place(x=1070, y=170)
        self.my_time()

        # Buttons
        self.b1 = Button(canvas, text='   BACK   ', width=10, bd=5, relief=RIDGE, background="white", command=self.back,
                    font=('Times New Roman', 15, 'bold'), bg='Light Grey')
        self.b1.place(x=20, y=40)

        self.b2 = Button(self.root, text='  UPDATE  ', relief=RIDGE, width=10, font=('Times New Roman', 15, 'bold'),
                    bg='cadetblue3', bd=5, command=self.updatebutton)
        self.b2.place(x=1080, y=400)

        self.re1 = Button(self.root, text='    CHECKOUT  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                      bg='cadetblue3', bd=5, command=self.checkout)
        self.re1.place(x=870, y=400)

        self.b6 = Button(self.root, text='  DELETE  ', relief=RIDGE, width=10, bd=5, font=('Times New Roman', 15, 'bold'),
                     bg='cadetblue3', command=self.delete)
        self.b6.place(x=1210, y=400)
         # Binding
        self.table.bind("<ButtonRelease-1>", self.select)

        to14 = Label(self.root, text='Total : ', font=('Times New Roman', 18))
        to14.place(x=50, y=400,width=200)

        self.total_amount = StringVar()
        self.total_amount.set("")
        self.s8 = Entry(self.root, textvariable=self.total_amount, font=('Times new Roman', 17),state='readonly')
        self.s8.place(x=300, y=400)

        # Initial Query to populate Treeview
        self.query_database()

    def back(self):
         self.root.destroy()
         from userhomepage import HomeUserPage
         HomeUserPage(Tk(),self.cusid,self.name,self.email)
       
    def query_database(self):
        self.table.delete(*self.table.get_children())
        get_all_book=self.cart_repository.get_carts_by_user(self.cusid)
        self.total_amount.set(self.cart_repository.get_total_amount(self.cusid))
        for bookinfo_cart in get_all_book:
        
            self.table.insert(parent='', index='end', text='',
                        values=(bookinfo_cart.cart_id,bookinfo_cart.qty,bookinfo_cart.book_id))


    def my_time(self):
        time_string = datetime.now().strftime('         %x ')
        self.e14.delete(0,END)
        self.e14.insert(0,time_string)
        self.e14.after(1000,self.my_time)

    def updatebutton(self):
           
            quantity=self.e6.get()
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            bookdata=self.book_repository.get_by_id(values1[2])
            if(float(quantity)<float(bookdata.stock)):
                self.cart_repository.update_cart_quantity(self.cusid, values1[2],quantity)
                messagebox.showinfo('Cart Update', 'Successfully  Update Cart Quantity ')
            else:
                 messagebox.showinfo('Cart Update', 'Insufficient Stock')
            self.query_database()
    def textbox_changed(self, event):
        # This function will be called whenever the content of the Entry changes
        new_text = self.quantity.get()
        selected = self.table.focus()
        values = self.table.item(selected, 'values')
        values1=list(values)
        bookdetails=self.book_repository.get_by_id(values1[2])
        print(bookdetails.price)
        bookstock=values1[5]
        print(bookstock)
        if(float(bookstock)>float(new_text)):
             self.price.set(float(bookdetails.price)*float(new_text))
        else:
             messagebox.showinfo('Book', 'Insufficient Quantity')
        
        print(values1)

            

    def select(self,e):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            bookdetails=self.book_repository.get_by_id(values1[2])
            print(bookdetails.book_name)
            self.bookname.set(bookdetails.book_name)
            self.authorname.set(bookdetails.author)
            self.edition.set(bookdetails.book_edition)
            self.description.set(bookdetails.description)
            self.quantity.set(values1[1])
            self.price.set(float(bookdetails.price)*float(values1[1]))
            CURRENT_SELECTED_ID=values1[0]

    def delete(self):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            self.cart_repository.delete_cart_entry(values1[0])
            messagebox.showinfo('Cart Delete', 'Successfully  Delete Cart Item')
            self.query_database()
    
    def checkout(self):
     self.root.destroy()
     from checkout import CheckoutPage
     CheckoutPage(Tk(),self.cusid,self.name,self.email)
  
       
