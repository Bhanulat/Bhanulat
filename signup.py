from tkinter import *
from tkinter import messagebox
from Utill.validation import is_valid_email, is_valid_mobile_number
from Model.user import User
from Repository.user_repository import UserRepository
class SignUpPage:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Book Mart")
        self.master.geometry('925x700+300+200')
        self.master.configure(bg='#fff')
        self.master.resizable(False, False)

        self.img = PhotoImage(file='Image/signup.png')
        Label(self.master, image=self.img, border=0, bg='white').place(x=50, y=200)

        self.frame = Frame(self.master, width=550, height=690, bg='#fff')
        self.frame.place(x=480, y=50)

        self.heading = Label(self.frame, text='Sign Up', fg='#57a1f8', bg='white',
                             font=('Microsoft Yahaei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        self.setup_entries_and_labels()

        self.signup_button = Button(self.frame, text='Sign Up', command=self.signup, fg='Black',
                                    background="DeepSkyBlue2", border=0, font=('Microsoft YaHei UI light', 15))
        self.signup_button.place(x=10, y=510, width=400, height=35)

        self.have_account_label = Label(self.frame, text="I have an account", background='white',
                                        foreground='Black', activebackground='Light Blue',
                                        font=('Microsoft YaHei UI light', 12))
        self.have_account_label.place(x=70, y=580)

        self.signin_button = Button(self.frame, text="Sign in!", background='white', foreground='Black',
                                     command=self.signin, border=0, cursor='hand2',
                                     font=('Microsoft YaHei UI light', 12, 'bold'))
        self.signin_button.place(x=220, y=576)

    def setup_entries_and_labels(self):
        self.l1 = Label(self.frame, text='First Name', background='white', foreground='Black',
                        activebackground='Light Blue', font=('Microsoft YaHei UI light', 11, 'bold'))
        self.l1.place(x=6, y=100)
        self.fname = Entry(self.frame, bd=3, font=('Microsoft YaHei UI light', 12))
        self.fname.place(x=10, y=130, width=400, height=35)
        self.fname.insert(0, '')
        self.fname.bind("<FocusIn>", self.on_enter)
        self.fname.bind("<FocusOut>", self.on_leave)

        self.l3 = Label(self.frame, text='Last Name', background='white', foreground='Black',
                        activebackground='Light Blue', font=('Microsoft YaHei UI light', 11, 'bold'))
        self.l3.place(x=6, y=180)
        self.lname = Entry(self.frame, bd=3, font=('Microsoft YaHei UI light', 12))
        self.lname.place(x=10, y=210, width=400, height=35)
        self.lname.insert(0, '')
        self.lname.bind("<FocusIn>", self.on_enter)
        self.lname.bind("<FocusOut>", self.on_leave)
        l2 = Label(self.frame, text='Password', background='white', foreground='Black',
                   activebackground='Light Blue', font=('Microsoft YaHei UI light', 11, 'bold'))
        l2.place(x=6, y=340)
        self.password = Entry(self.frame, bd=3, font=('Microsoft YaHei UI light', 12))
        self.password.place(x=10, y=370, width=400, height=35)
        self.password.insert(0, '')
        self.password.bind("<FocusIn>", self.on_enter)
        self.password.bind("<FocusOut>", self.on_leave)

        mno2 = Label(self.frame, text='Mobile Number', background='white', foreground='Black',
                     activebackground='Light Blue', font=('Microsoft YaHei UI light', 11, 'bold'))
        mno2.place(x=6, y=420)
        self.mno = Entry(self.frame, bd=3, font=('Microsoft YaHei UI light', 12))
        self.mno.place(x=10, y=450, width=400, height=35)
        self.mno.insert(0, '')
        self.mno.bind("<FocusIn>", self.on_enter)
        self.mno.bind("<FocusOut>", self.on_leave)

        l3 = Label(self.frame, text='Email ID', background='white', foreground='Black',
                   activebackground='Light Blue', font=('Microsoft YaHei UI light', 11, 'bold'))
        l3.place(x=6, y=260)
        self.email = Entry(self.frame, bd=3, font=('Microsoft YaHei UI light', 12))
        self.email.place(x=10, y=290, width=400, height=35)
        self.email.insert(0, '')
        self.email.bind("<FocusIn>", self.on_enter)
        self.email.bind("<FocusOut>", self.on_leave)
 

    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leave(self, e):
        widget = e.widget
        name = widget.get()
        if name == '':
            widget.insert(0, '')

    def signup(self):
        f_name = self.fname.get()
        l_name = self.lname.get()
        email_id = self.email.get()
        m_no = self.mno.get()
        pass_word = self.password.get()
      
        if(f_name == ""):
            messagebox.showerror('Required' , 'First Name Required')
        elif(email_id == ""):
            messagebox.showerror('Required' , 'Email ID Required')  
        elif(m_no == ''):
            messagebox.showerror('Required', 'Mobile Number Required')
        elif(pass_word == ''):
            messagebox.showerror('Required', 'Password Required')
        elif is_valid_email(email_id) == False:
            messagebox.showerror('Invalid' , 'Invalid Email Id')
        elif is_valid_mobile_number(m_no) == False:
            messagebox.showerror('Invalid' , 'Invalid Mobile Number')
        else:
            user_repository = UserRepository()
            if(user_repository.email_exists(email_id)):
                messagebox.showerror('Email' , 'Already Email Id Exist')
            else:
                user = User(None, f_name, l_name,email_id, pass_word, m_no)
                user_repository.add_user(user)
                messagebox.showinfo('Signup', 'Successfully Sign Up')
                self.master.destroy()
                from login import LoginPage
                LoginPage(Tk())


    def signin(self):
        self.master.destroy()
        from login import LoginPage
        LoginPage(Tk())



       