from tkinter import *
from server.Authentication import *

class EntryWin():
    def __init__(self):
        self.root = None
        self.entry_username = None
        self.entry_password = None
        self.password_is_hide = True
        self.root = Tk()
        self.username = ""
        self.password = ""
        self.succesful_entry = False


    def initialAll(self):
        self.initialRoot()
        self.initialForm()

    def initialRoot(self):
        self.root.minsize(400, 500)
        self.root.maxsize(400, 500)
        self.root.title("Войдите в аккаунт")
    
    def initialForm(self):
        self.initial_username_form()
        self.initial_password_form()
        button_login = Button(self.root, text="Войти", command=self.get_password)
        button_login.pack(pady=(0, 6))
        self.hide_password_btn = Button(self.root, text="Показать пароль", command=self.hide_password)
        self.hide_password_btn.pack(pady=(0, 6))
        self.exceptions = Label(self.root, text="", font=('Arial', 12), fg="red")
        self.exceptions.pack(pady=(0, 6))


    def initial_username_form(self):
        label_username = Label(self.root, text="Имя пользователя:", font=('Arial', 12))
        label_username.pack(padx=20, pady=(0, 4))
        self.entry_username = Entry(self.root, width=30)
        self.entry_username.pack(padx=20, pady=(0, 8))

    def initial_password_form(self):
        label_password = Label(self.root, text="Пароль:", font=('Arial', 12))
        label_password.pack(padx=20, pady=(0, 4))
        self.entry_password = Entry(self.root, show="*", width=30)
        self.entry_password.pack(padx=20, pady=(0, 15))    

    def get_password(self):
        self.username = self.entry_username.get()
        self.password = self.entry_password.get()
        self.try_login()
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)

    def hide_password(self):
        if self.password_is_hide:
            self.password_is_hide = False
            self.entry_password.config(show="")
        else:
            self.password_is_hide = True
            self.entry_password.config(show="*")    
    
    
    def try_login(self):
        self.exceptions.config(text="")
        if self.username == "" or self.password == "":
            self.exceptions.config(text="Имя или пароль пусты\n")
        else: 
            if self.login_is_succsesful():
                self.succesful_entry = True
                self.root.destroy()
            else:
                self.exceptions.config(text="Имя и пароль не совпадают\n")    


    def login_is_succsesful(self):
        Auth = Password()
        hash = Auth.getHash(self.password)
        print(hash)
        if hash == "$2b$12$cBQ2MOmKZbDrXkEvmiI5NeF6FnNxbJFho6DuI8BicDVryyZdSF3nG":
            return True


