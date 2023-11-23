from tkinter import *
from tkinter import messagebox
import usuarios


class App:

    def __init__(self, root = None):
        self.frame = Frame(root)
        self.frame.pack()

        self.frame1 = Frame(self.frame)
        self.frame1.pack(padx=(10,0))
        
        self.frame2 = Frame(self.frame)
        self.frame2.pack(pady=10, padx=(0,25))

        self.frame3 = Frame(self.frame)
        self.frame3.pack(padx=(0,60))

        self.frame4 = Frame(self.frame)
        self.frame4.pack(pady=(10,0))
        
        self.label_title = Label(self.frame1, text='LOGIN', font=('Roboto', 25))
        self.label_title.pack()

        self.label_text_entry_user = Label(self.frame2, text='USER')
        self.label_text_entry_user.pack(side='left')

        self.user_entry = Entry(self.frame2, width=25)
        self.user_entry.pack()

        self.label_title_password_entry = Label(self.frame3, text='PASSWORD')
        self.label_title_password_entry.pack(side='left')

        self.entry_password = Entry(self.frame3, width=25)
        self.entry_password.pack()

        self.enter_button = Button(self.frame4, text='ENTER',command=self.message)
        self.enter_button.pack(side=LEFT)

        self.register_button = Button(self.frame4, text='REGISTER', command=self.page_register)
        self.register_button.pack(side=LEFT)


    #eventos
    def page_register(self):

        self.frame.pack_forget()

        self.frame = Frame(root)
        self.frame.pack()

        self.frame1 = Frame(self.frame)
        self.frame1.pack()

        self.frame2 = Frame(self.frame)
        self.frame2.pack()

        self.frame3 = Frame(self.frame)
        self.frame3.pack()
        
        self.frame4 = Frame(self.frame)
        self.frame4.pack()

        self.frame5 = Frame(self.frame)
        self.frame5.pack()

        self.frame6 = Frame(self.frame)
        self.frame6.pack()
        
        self.label_title = Label(self.frame1, text='REGISTER', font=('Roboto', 25))
        self.label_title.pack()

        self.labeltext_entry_firstname = Label(self.frame2, text='FIRST NAME')
        self.labeltext_entry_firstname.pack(side=LEFT)

        self.entry_firstname = Entry(self.frame2, width=30)
        self.entry_firstname.pack(padx=(0,40),pady=(5,5))

        self.label_text_lastname = Label(self.frame3, text='LAST NAME')
        self.label_text_lastname.pack(side=LEFT)

        self.entry_lastname = Entry(self.frame3, width=30)
        self.entry_lastname.pack(padx=(0,37),pady=(5,5))

        self.labeltext_user_pgr = Label(self.frame4, text='USER')
        self.labeltext_user_pgr.pack(side=LEFT)

        self.entry_user_pgr = Entry(self.frame4, width=30)
        self.entry_user_pgr.pack(padx=(0,2),pady=(5,5))

        self.labeltext_password_pgr = Label(self.frame5, text='PASSWORD')
        self.labeltext_password_pgr.pack(side=LEFT)

        self.entry_password_pgr = Entry(self.frame5, width=30)
        self.entry_password_pgr.pack(padx=(0,37),pady=(5,5))

        self.enter_button_pgr = Button(self.frame6, text='ENTER', command=self.insert_user)
        self.enter_button_pgr.pack(side=LEFT, padx=(30,0))
    
        self.homepage = Button(self.frame6, text='HOME PAGE', command=self.home_page)
        self.homepage.pack(side=LEFT)


    def main_page(self):
        self.frame.pack_forget()
        self.frame_main_page = Frame(root)


    def home_page(self):

        self.frame.pack_forget()
        App()
    

    def insert_user(self):

        self.firstname = self.entry_firstname.get()
        self.lastname = self.entry_lastname.get()
        self.user = self.entry_user_pgr.get()
        self.password = self.entry_password_pgr.get()

        response = usuarios.Users()
        response = response.insert_into(self.firstname,self.lastname,self.user,self.password)
    
        if response == False:

            self.warning = messagebox.showinfo(title='', message='Nome de usuario já em uso')

        else:
            self.warning = messagebox.showinfo(title='', message='Você foi registrado com sucesso!')
        
            self.frame.pack_forget()
            self.home_page()
    

    def message(self):

        user = self.user_entry.get()
        password = self.entry_password.get()
        response = usuarios.Users()
        response = response.check(user, password)
        
        if response == True:

            self.warning = messagebox.showinfo(title='', message='Logado com sucesso!')
            self.main_page()
        
        else:

            self.warning = messagebox.showinfo(title='', message='Usuario ou senha incorretos')

if __name__ == '__main__':

    root = Tk()
    App(root)
    root.mainloop()