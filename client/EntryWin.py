from tkinter import *
import server.Authentication as Authentication

class entryWin():
    def __init__(self):
        self.root = None
        self.entry_username = None
        self.entry_password = None
        self.password_is_hide = True

    def initialAll(self):
        self.root = self.initialRoot()
        self.initialForm()
        self.root.mainloop()

    def initialRoot(self):
        root = Tk()
        root.minsize(400, 500)
        root.maxsize(400, 500)
        root.title("Войдите в аккаунт")
        return root
    
    def initialForm(self):
        self.initial_username()
        self.initial_username()

        button_login = Button(self.root, text="Войти", command=self.login)
        button_login.pack(pady=(0, 6))
        self.button_login = Button(self.root, text="Показать пароль", command=self.hide_password)
        button_login.pack(pady=(0, 6))

    def initial_username(self):
        label_username = Label(self.root, text="Имя пользователя:", font=('Arial', 12))
        label_username.pack(padx=20, pady=(0, 4))
        self.entry_username = Entry(self.root, width=30)
        self.entry_username.pack(padx=20, pady=(0, 8))

    def initial_username(self):
        label_password = Label(self.root, text="Пароль:", font=('Arial', 12))
        label_password.pack(padx=20, pady=(0, 4))
        self.entry_password = Entry(self.root, show="*", width=30)
        self.entry_password.pack(padx=20, pady=(0, 15))    

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # if Authentication.try_authentication(username, password):
        #     self.root.close()
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)

    def hide_password(self):
        if self.password_is_hide:
            self.password_is_hide = False
            self.entry_password.config(show="")
        else:
            self.password_is_hide = True
            self.entry_password.config(show="*")    


entryWin = entryWin()
entryWin.initialAll()     