from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from Model.books import Books
from Model.cart import Cart
from Repository.cart_repository import CartRepository
from Repository.books_repository import BooksRepository
from Utill.const import CURRENT_SELECTED_ID

class BookShoppingPage:
    def __init__(self, master, customerid,name,email):
        self.root = master
        self.cusid = customerid
        self.name=name
        self.email=email
        self.root.state('zoomed')
        self.root.title('Books Shopping')
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

        self.table['columns'] = ('BookId', 'BookName', 'Author', 'Edition', 'Description', 'Quantity', 'Price')
        self.table.column('#0', width=0, stretch=0)
        self.table.column('BookId', anchor=W, width=50)
        self.table.column('BookName', anchor=W, width=50)
        self.table.column('Author', anchor=W, width=80)
        self.table.column('Edition', anchor=W, width=80)
        self.table.column('Description', anchor=W, width=80)
        self.table.column('Quantity', anchor=W, width=50)
        self.table.column('Price', anchor=W, width=100)

        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('BookId', text='Book Id', anchor=CENTER)
        self.table.heading('BookName', text='Book Name', anchor=CENTER)
        self.table.heading('Author', text='Author Name', anchor=CENTER)
        self.table.heading('Edition', text='Edition', anchor=CENTER)
        self.table.heading('Description', text='Description', anchor=CENTER)
        self.table.heading('Quantity', text='Quantity', anchor=CENTER)
        self.table.heading('Price', text='Price', anchor=CENTER)
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
        l4 = Label(self.root, text='Books Shopping ', foreground='white', background='cyan4',
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

        self.b1 = Button(canvas, text='   ViewCart   ', width=10, bd=5, relief=RIDGE, background="white", command=self.viewCart,
                    font=('Times New Roman', 15, 'bold'), bg='Light Grey')
        self.b1.place(x=200, y=40)

       

        self.b3 = Button(self.root, text='    SEARCH  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                    bg='cadetblue3', bd=5, command=self.search)
        self.b3.place(x=670, y=400)

        self.re1 = Button(self.root, text='    RESET  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                      bg='cadetblue3', bd=5, command=self.reset)
        self.re1.place(x=870, y=400)

        self.b4 = Button(self.root, text='     ADD TO CART   ', relief=RIDGE, width=10, font=('Times New Roman', 15, 'bold'),
                     bg='cadetblue3', command=self.save, bd=5)
        self.b4.place(x=600, y=290)

       

        # Combobox and Entry for searching
        e13 = ['BookName', 'Author', "PriceRange"]
        self.combobox = ttk.Combobox(self.root, values=e13, font=('Times New Roman', 18, "bold"))
        self.combobox.place(x=50, y=400, width=200, height=35)
        self.combobox.set('Search by')

        self.search_ = StringVar()
        self.search_.set("100-300")
        self.s8 = Entry(self.root, textvariable=self.search_, font=('Times new Roman', 17))
        self.s8.place(x=300, y=400)

        # Binding
        self.table.bind("<ButtonRelease-1>", self.select)

        # Initial Query to populate Treeview
        self.query_database()

    def back(self):
         self.root.destroy()
         from userhomepage import HomeUserPage
         HomeUserPage(Tk(),self.cusid,self.name,self.email)
    
    def viewCart(self):
         self.root.destroy()
         from shoppingcart import BooksShoppingCartPage
         BooksShoppingCartPage(Tk(),self.cusid,self.name,self.email)

         
    def textbox_changed(self, event):
        # This function will be called whenever the content of the Entry changes
        new_text = self.quantity.get()
        selected = self.table.focus()
        values = self.table.item(selected, 'values')
        values1=list(values)
        bookstock=values1[5]
        print(bookstock)
        if(float(bookstock)>float(new_text)):
             self.price.set(float(values1[6])*float(new_text))
        else:
             messagebox.showinfo('Book', 'Insufficient Quantity')
        print(values1)

        print("Textbox changed:", new_text)
       

    def query_database(self):
        self.table.delete(*self.table.get_children())
        get_all_book=self.book_repository.get_books()
        
        for bookinfo in get_all_book:
            print(bookinfo.book_name)
            self.table.insert(parent='', index='end', text='',
                        values=(bookinfo.book_id,bookinfo.book_name, bookinfo.author, bookinfo.book_edition, bookinfo.description, bookinfo.stock,bookinfo.price))

    def save(self):
       
        selected = self.table.focus()
        values = self.table.item(selected, 'values')
        values1=list(values)
        bookid=values1[0]
        quantity=self.e6.get()
        book_cart = Cart(None, quantity,bookid, self.cusid)
        self.cart_repository.add_cart(book_cart)
        messagebox.showinfo('Book', 'Successfully Add to Cart')
        self.query_database()
            

    def my_time(self):
        time_string = datetime.now().strftime('         %x ')
        self.e14.delete(0,END)
        self.e14.insert(0,time_string)
        self.e14.after(1000,self.my_time)



    def select(self,e):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            print(values1)
            self.bookname.set(values1[1])
            self.authorname.set(values1[2])
            self.edition.set(values1[3])
            self.description.set(values1[4])
            self.price.set(values1[6])
            self.quantity.set(1)
       
            CURRENT_SELECTED_ID=values1[0]

  
    def search(self):
        selected_value = self.combobox.get()
        searchtext=self.s8.get()
        if(searchtext!=""):
            self.table.delete(*self.table.get_children())
            get_all_book=self.book_repository.get_books()
            if(selected_value=="Author"):
                get_all_book=self.book_repository.get_books_by_author(searchtext)
            elif(selected_value=="BookName"):
                get_all_book=self.book_repository.get_books_by_name(searchtext)   
            elif(selected_value=="PriceRange"):
                val_range=searchtext.split("-")
                if(len(val_range)==2):
                        get_all_book=self.book_repository.get_books_by_price_range(val_range[0],val_range[1]) 
                else:
                        get_all_book=self.book_repository.get_books_by_price_range(0,val_range[0])
            else:
                get_all_book=self.book_repository.search_books(searchtext)
                
            for bookinfo in get_all_book:
                print(bookinfo.book_name)
                self.table.insert(parent='', index='end', text='',
                            values=(bookinfo.book_id,bookinfo.book_name, bookinfo.author, bookinfo.book_edition, bookinfo.description, bookinfo.stock,bookinfo.price))

    def reset(self):
     self.query_database()
     self.search_.set("Range like 100-300")
     self.combobox.set('Search by')
       

