from tkinter import *
from PIL import ImageTk, Image
from Repository.books_repository import BooksRepository
from Repository.user_repository import UserRepository
from Repository.order_repository  import OrderRepository

class HomeAdminPage:
    def __init__(self, master):
        self.master = master
        self.master.title('Book Mart - Admin | Homepage')
        self.master.state('zoomed')
        self.bookcount=BooksRepository().get_total_book_count()
        self.usercount=UserRepository().get_total_user_count()
        self.ordercount=OrderRepository().get_total_order_count()
        self.todayordercount=OrderRepository().get_today_order_count()
        self.incompleteordercount=OrderRepository().get_order_incomplete_count()


        self.canvas2 = Canvas(self.master, width=1400, height=700)
        self.canvas2.pack()
        self.r2 = self.canvas2.create_rectangle(360, 230, 1350, 700, outline="Black")
        self.canvas2.update()

        self.frame1 = Frame(self.master, bg='cyan4')
        self.frame1.place(x=0, y=0, width=1400, height=120)

        self.frame2 = Frame(self.master, bg='black')
        self.frame2.place(x=0, y=120, width=1400, height=20)

        self.frame3 = Frame(self.master, bd=3, relief=RIDGE)
        self.frame3.place(x=0, y=140, width=320, height=600)

        image1 = Image.open("Image/admin.png")
        image1 = image1.resize((200, 200), resample=Image.LANCZOS)
        self.img_admin = ImageTk.PhotoImage(image1)

        title = Label(self.frame3, text='', image=self.img_admin)
        title.place(x=56, y=0)

        l1 = Label(self.master, text='Book Mart - Book Sales and Management System', foreground='white',
                   background='cyan4', activebackground='Light Blue', font=('Times New Roman', 45, 'bold'))
        l1.place(x=40, y=20)

        l2 = Label(self.master, text='Total Books\n'+str(self.bookcount), background='DeepSkyBlue2', bd=5, relief=RIDGE,
                   activebackground='Light Blue', font=('Times New Roman', 20, 'bold'))
        l2.place(x=400, y=250, width=280, height=150)

        l3 = Label(self.master, text='Total Order\n'+str(self.ordercount), background='DeepSkyBlue2', bd=5, relief=RIDGE,
                   activebackground='Light Blue', font=('Times New Roman', 20, 'bold'))
        l3.place(x=730, y=250, width=280, height=150)

        l4 = Label(self.master, text='Total Customers\n'+str(self.usercount), background='DeepSkyBlue2', bd=5, relief=RIDGE,
                   activebackground='Light Blue', font=('Times New Roman', 20, 'bold'))
        l4.place(x=1050, y=250, width=280, height=150)

        l5 = Label(self.master, text='Total Incomplete\n'+str(self.incompleteordercount), background='DeepSkyBlue2', bd=5, relief=RIDGE,
                   activebackground='Light Blue', font=('Times New Roman', 20, 'bold'))
        l5.place(x=400, y=500, width=280, height=150)

        l6 = Label(self.master, text='Total Today Orders\n'+str(self.todayordercount), background='DeepSkyBlue2', bd=5, relief=RIDGE,
                   activebackground='Light Blue', font=('Times New Roman', 20, 'bold'))
        l6.place(x=730, y=500, width=280, height=150)

        l7 = Label(self.master, text='Dashboard', font=('Times New Roman', 32, 'bold'))
        l7.place(x=370, y=150)

        l8 = Label(self.master, text='Admin', foreground='black', bd=5, relief=RIDGE, background='RoyalBlue1',
                   activebackground='Light Blue', font=('Times New Roman', 28, 'bold'))
        l8.place(x=0, y=320, width=320, height=80)

        self.b1 = Button(self.master, text='Books Management', command=self.switch_to_book_management, compound=LEFT,
                         bd=5, relief=RIDGE, background="white", font=('Times New Roman', 22))
        self.b1.place(x=0, y=400, width=320, height=60)
        
        self.b1 = Button(self.master, text='Books Management',command = self.switch_to_book_management,compound=LEFT,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b1.place(x = 0,y = 400,width = 320,height = 60)

        self.b2 = Button(self.master, text='Orders Management',width = 12,command= self.switch_to_order_management ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b2.place(x = 0,y = 460,width = 320,height = 60)

        self.b3 = Button(self.master, text='Customer Managment',width = 12,command= self.switch_to_customer_management ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b3.place(x = 0,y = 520,width = 320,height = 60)

        self.b4 = Button(self.master, text='Sales Report',width = 12,command= self.switch_to_sales_management ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b4.place(x = 0,y = 580,width = 320,height = 60)

        self.b5 = Button(self.master, text='Logout',width = 12,command= self.logout,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b5.place(x = 0,y = 640,width = 320,height = 60)


    def switch_to_book_management(self):
        self.master.destroy()
        from bookmanagement import BooksManagementPage
        BooksManagementPage(Tk())
    def switch_to_order_management(self):
        self.master.destroy()
        from ordermanagement import OrderManagmentPage
        OrderManagmentPage(Tk())
    def switch_to_customer_management(self):
        self.master.destroy()
        from customermanagement import CustomerManagmentPage
        CustomerManagmentPage(Tk())
    def switch_to_sales_management(self):
        self.master.destroy()
        from salesReport import SalesManagmentPage
        SalesManagmentPage(Tk())
    def logout(self):
        self.master.destroy()
        from login import LoginPage
        LoginPage(Tk())

