from tkinter import *
from PIL import ImageTk, Image
from Model.user import User
from Repository.order_repository import OrderRepository

class HomeUserPage:
    def __init__(self, master,userid,username, email):
        self.master = master
        self.master.title('Book Mart - User | Homepage')
        self.master.state('zoomed')
        self.custid=userid
        self.name=username
        self.email=email
        self.orderrepo=OrderRepository()

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

        l2 = Label(self.master, text='Total Order \n['+str(self.orderrepo.get_order_count_by_user_id(self.custid))+"]", background='DeepSkyBlue2', bd=5, relief=RIDGE,
                   activebackground='Light Blue', font=('Times New Roman', 20, 'bold'))
        l2.place(x=400, y=250, width=280, height=150)

        

        l7 = Label(self.master, text='Dashboard', font=('Times New Roman', 32, 'bold'))
        l7.place(x=370, y=150)

        l8 = Label(self.master, text=self.name, foreground='black', bd=5, relief=RIDGE, background='RoyalBlue1',
                   activebackground='Light Blue', font=('Times New Roman', 28, 'bold'))
        l8.place(x=0, y=320, width=320, height=80)

        self.b1 = Button(self.master, text='Book Shopping', command=self.switch_to_book_management, compound=LEFT,
                         bd=5, relief=RIDGE, background="white", font=('Times New Roman', 22))
        self.b1.place(x=0, y=400, width=320, height=60)
        
        self.b1 = Button(self.master, text='Purchase Books',command = self.switch_to_book_management,compound=LEFT,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b1.place(x = 0,y = 400,width = 320,height = 60)

        self.b2 = Button(self.master, text='Orders Details',width = 12,command= self.switch_to_order_management ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b2.place(x = 0,y = 460,width = 320,height = 60)

        self.b3 = Button(self.master, text='Shopping Cart',width = 12,command= self.switch_to_shopping ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b3.place(x = 0,y = 520,width = 320,height = 60)

        self.b5 = Button(self.master, text='Logout',width = 12,command= self.logout,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
        self.b5.place(x = 0,y = 580,width = 320,height = 60)


    def switch_to_book_management(self):
        self.master.destroy()
        from bookshopping import BookShoppingPage
        BookShoppingPage(Tk(),self.custid,self.name,self.email)
    def switch_to_order_management(self):
        self.master.destroy()
        from orderDetails import OrderPage
        OrderPage(Tk(),self.custid,self.name,self.email)

    def switch_to_shopping(self):
        self.master.destroy()
        from shoppingcart import BooksShoppingCartPage
        BooksShoppingCartPage(Tk(),self.custid,self.name,self.email) 
    
    def logout(self):
        self.master.destroy()
        from login import LoginPage
        LoginPage(Tk())

