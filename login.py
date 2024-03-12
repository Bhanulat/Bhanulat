from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
from Utill.validation import is_valid_email
from Model.user import User
from Repository.user_repository import UserRepository

class LoginPage:
    def __init__(self, master):
        
        self.master = master
        self.master.geometry('925x500+300+200')
        self.master.title('Book Mart')
        self.master.configure(background='white')
        self.master.resizable(False, False)
        self.userrepo=UserRepository()

        self.img1 = PhotoImage(file='Image/login_theme.png')
        Label(self.master, image=self.img1, bg='white').place(x=50, y=50)

        self.frame1 = Frame(self.master, bg='white')
        self.frame1.place(x=480, y=20, width=400, height=400)

        self.sign_in_label = Label(self.frame1, text='Sign in', background='white', foreground='DeepSkyBlue2',
                                   activebackground='Light Blue', font=('Microsoft YaHei UI light', 30, 'bold'))
        self.sign_in_label.place(x=120, y=0)

        self.setup_entries_and_labels()

        self.login_button = Button(self.frame1, text='Sign in', command=self.signin, fg='Black',
                                   background="DeepSkyBlue2", border=0, font=('Microsoft YaHei UI light', 15))
        self.login_button.place(x=10, y=280, width=400, height=35)

        self.dont_have_account_label = Label(self.frame1, text="Don't have an account?", background='white',
                                             foreground='Black', activebackground='Light Blue',
                                             font=('Microsoft YaHei UI light', 12))
        self.dont_have_account_label.place(x=50, y=350)

        self.signup_button = Button(self.frame1, text="Sign up!", background='white', foreground='Black',
                                    command=self.sign_up, border=0, cursor='hand2',
                                    font=('Microsoft YaHei UI light', 12, 'bold'))
        self.signup_button.place(x=240, y=346)

    def setup_entries_and_labels(self):
        self.e1_label = Label(self.frame1, text='Email Address', background='white', foreground='Black',
                               activebackground='Light Blue', font=('Microsoft YaHei UI light', 11, 'bold'))
        self.e1_label.place(x=6, y=100)
        self.e1 = Entry(self.frame1, bd=3, font=('Microsoft YaHei UI light', 12))
        self.e1.place(x=10, y=130, width=400, height=35)
        self.e1.insert(0, '')
        self.e1.bind("<FocusIn>", self.on_enter)
        self.e1.bind("<FocusOut>", self.on_leave)

        self.e2_label = Label(self.frame1, text='Password', background='white', foreground='Black',
                               activebackground='Light Blue', font=('Microsoft YaHei UI light', 11, 'bold'))
        self.e2_label.place(x=6, y=180)
        self.e2 = Entry(self.frame1, bd=3, font=('Microsoft YaHei UI light', 12))
        self.e2.place(x=10, y=210, width=400, height=35)
        self.e2.insert(0, '')
        self.e2.bind("<FocusIn>", self.on_enter)
        self.e2.bind("<FocusOut>", self.on_leave)

    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leave(self, e):
        widget = e.widget
        name = widget.get()
        if name == '':
            widget.insert(0, '')

    def sign_up(self):
        self.master.destroy()
        from signup import SignUpPage
        SignUpPage(Tk())

    def signin(self):
        if self.e1.get() == "":
            messagebox.showerror('Required', 'Email Id Required')
        elif self.e2.get() == "":
            messagebox.showerror('Required', 'Password Required')
        elif not is_valid_email(self.e1.get()):
            messagebox.showerror('Invalid', 'Invalid Email Id')
        elif self.e1.get() == "Admin@gmail.com" and self.e2.get() == "Admin":
            self.master.destroy()
            from homepage import HomeAdminPage
            HomeAdminPage(Tk())
    
        else:
            data=self.userrepo.get_user_details(self.e1.get(),self.e2.get())
            if(data==None):
                messagebox.showerror('Invalid', 'Invalid username or password')
            else:
                messagebox.showinfo('Welcome',"Welcome "+ data.first_name+" "+data.last_name)
                self.master.destroy()
                from userhomepage import HomeUserPage
                print(data.user_id,data.first_name,data.email)
                HomeUserPage(Tk(),data.user_id,data.first_name,data.email)
