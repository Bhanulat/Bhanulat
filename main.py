from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
from Utill.validation import is_valid_email
from login import LoginPage
if __name__ == "__main__":
    root = Tk()
    login_page =LoginPage(root)
    root.mainloop()
