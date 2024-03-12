from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from Model.books import Books
from Repository.books_repository import BooksRepository
from Utill.const import CURRENT_SELECTED_ID

class BooksManagementPage:
    def __init__(self, master):
        self.root = master
        self.root.state('zoomed')
        self.root.title('Books Management')
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
        l4 = Label(self.root, text='Books Mart', foreground='white', background='cyan4',
                   activebackground='Light Blue', font=('Times New Roman', 45, 'bold'))
        l4.place(x=500, y=20)

        # Labels and Entry Widgets
        l1 = Label(self.root, text='Book Name : ', font=('Times new Roman', 18))
        l1.place(x=50, y=170)
        self.bookname = StringVar()
        self.e1 = Entry(self.root, textvariable=self.bookname, font=('Times', 17))
        self.e1.place(x=230, y=170)

        l3 = Label(self.root, text='Author Name', font=('Times new Roman', 18))
        l3.place(x=480, y=170)
        self.authorname = StringVar()
        self.e3 = Entry(self.root, textvariable=self.authorname, font=('Times new Roman', 17))
        self.e3.place(x=700, y=170)

        l5 = Label(self.root, text='Book Edition', font=('Times new Roman', 18))
        l5.place(x=50, y=230)
        self.edition = StringVar()
        self.e5 = Entry(self.root, textvariable=self.edition, font=('Times new Roman', 17))
        self.e5.place(x=230, y=230)

        l6 = Label(self.root, text='Quantity: ', font=('Times new Roman', 18))
        l6.place(x=480, y=230)
        self.quantity = StringVar()
        self.e6 = Entry(self.root, textvariable=self.quantity, font=('Times new Roman', 17))
        self.e6.place(x=700, y=230)

        l8 = Label(self.root, text='Price: ', font=('Times new Roman', 18))
        l8.place(x=970, y=230)
        self.price = StringVar()
        self.e8 = Entry(self.root, textvariable=self.price, font=('Times new Roman', 17))
        self.e8.place(x=1070, y=230)

        l9 = Label(self.root, text='Description: ', font=('Times', 18))
        l9.place(x=50, y=290)
        self.description = StringVar()
        self.e9 = Entry(self.root, textvariable=self.description, font=('Times', 15))
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

        self.b3 = Button(self.root, text='    SEARCH  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                    bg='cadetblue3', bd=5, command=self.search)
        self.b3.place(x=670, y=400)

        self.re1 = Button(self.root, text='    RESET  ', relief=RIDGE, font=('Times New Roman', 15, 'bold'),
                      bg='cadetblue3', bd=5, command=self.reset)
        self.re1.place(x=870, y=400)

        self.b4 = Button(self.root, text='     ADD    ', relief=RIDGE, width=10, font=('Times New Roman', 15, 'bold'),
                     bg='cadetblue3', command=self.save, bd=5)
        self.b4.place(x=600, y=290)

        self.b6 = Button(self.root, text='  DELETE  ', relief=RIDGE, width=10, bd=5, font=('Times New Roman', 15, 'bold'),
                     bg='cadetblue3', command=self.delete)
        self.b6.place(x=1210, y=400)

        self.b7 = Button(self.root, text='   CLEAR   ', relief=RIDGE, width=10, bd=5,
                     font=('Times New Roman', 15, 'bold'), bg='cadetblue3', command=self.clear)
        self.b7.place(x=800, y=290)

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
         from homepage import HomeAdminPage
         HomeAdminPage(Tk())
       

    def clear(self):
        self.e1.delete(0, END)
        self.e3.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.e8.delete(0, END)
        self.e9.delete(0, END)

    def query_database(self):
        self.table.delete(*self.table.get_children())
        get_all_book=self.book_repository.get_books()
        for bookinfo in get_all_book:
            print(bookinfo.book_name)
            self.table.insert(parent='', index='end', text='',
                        values=(bookinfo.book_id,bookinfo.book_name, bookinfo.author, bookinfo.book_edition, bookinfo.description, bookinfo.stock,bookinfo.price))

    def save(self):
        bookname=self.e1.get()
        bookauthor=self.e3.get()
        bookdescription=self.e9.get()
        bookedition=self.e5.get()
        price=self.e8.get()
        quantity=self.e6.get()
        if(bookname==""):
            messagebox.showerror("Required", "Please fill all Book Name")
        elif(bookauthor==""):
            messagebox.showerror("Required", "Please fill all Book Author")
        elif(bookdescription==""):
            messagebox.showerror("Required", "Please fill all Book Description")
        elif(bookedition==""):
            messagebox.showerror("Required", "Please fill all Book Edition")
        elif(price==""):
            messagebox.showerror("Required", "Please fill all Book Price")
        elif(quantity==""):
            messagebox.showerror("Required", "Please fill all Book quantity")
        else:
            
            book = Books(None, bookname,bookdescription, bookauthor,bookedition,price ,quantity)
            self.book_repository.add_book(book)
            messagebox.showinfo('Book', 'Successfully Add Book')
            self.query_database()
            

    def my_time(self):
        time_string = datetime.now().strftime('         %x ')
        self.e14.delete(0,END)
        self.e14.insert(0,time_string)
        self.e14.after(1000,self.my_time)

    def updatebutton(self):
            bookname=self.e1.get()
            bookauthor=self.e3.get()
            bookdescription=self.e9.get()
            bookedition=self.e5.get()
            price=self.e8.get()
            quantity=self.e6.get()
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            book = Books(None, bookname,bookdescription, bookauthor,bookedition,price ,quantity)
            self.book_repository.update_book(values1[0],book)
            messagebox.showinfo('Book Update', 'Successfully  Update Book')
            self.query_database()
            

    def select(self,e):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            print(values1)
            self.bookname.set(values1[1])
            self.authorname.set(values1[2])
            self.edition.set(values1[3])
            self.description.set(values1[4])
            self.quantity.set(values1[5])
            self.price.set(values1[6])
            CURRENT_SELECTED_ID=values1[0]

    def delete(self):
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            values1=list(values)
            self.book_repository.delete_book(values1[0])
            messagebox.showinfo('Book Delete', 'Successfully  Delete Book')
            self.query_database()
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
       
