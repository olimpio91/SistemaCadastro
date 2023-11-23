from tkinter import *
from tkinter import messagebox
import usuarios


class App:

    def __init__(self, root = None):
        self.frame = Frame(root)
        self.frame.pack(padx=50)

        self.frame1 = Frame(self.frame)
        self.frame1.pack()
        
        self.frame2 = Frame(self.frame)
        self.frame2.pack()

        self.frame3 = Frame(self.frame)
        self.frame3.pack()

        self.frame4 = Frame(self.frame)
        self.frame4.pack()
        
        self.label_title = Label(self.frame1, text='LOGIN', font=('Roboto', 25))
        self.label_title.pack()

        self.label_text_entry_user = Label(self.frame2, text='USUÁRIO')
        self.label_text_entry_user.pack()

        self.user_entry = Entry(self.frame2, width=25)
        self.user_entry.pack()

        self.label_text_password_entry = Label(self.frame3, text='SENHA')
        self.label_text_password_entry.pack()

        self.entry_password = Entry(self.frame3, width=25, show='*')
        self.entry_password.pack()

        self.enter_button = Button(self.frame4, text='ENTRAR',command=self.message)
        self.enter_button.pack(side=LEFT, pady=5)

        self.register_button = Button(self.frame4, text='REGISTRAR-SE', command=self.page_register)
        self.register_button.pack(side=LEFT)


    def page_register(self):

        self.frame.pack_forget()

        self.frame = Frame(root)
        self.frame.pack(padx=50)

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
        self.frame6.pack(pady=5)
        
        self.label_title = Label(self.frame1, text='REGISTER', font=('Roboto', 25))
        self.label_title.pack()

        self.labeltext_entry_firstname = Label(self.frame2, text='NOME')
        self.labeltext_entry_firstname.pack()

        self.entry_firstname = Entry(self.frame2, width=30)
        self.entry_firstname.pack(pady=5)

        self.label_text_lastname = Label(self.frame3, text='SOBRENOME')
        self.label_text_lastname.pack()

        self.entry_lastname = Entry(self.frame3, width=30)
        self.entry_lastname.pack(pady=5)

        self.labeltext_user_pgr = Label(self.frame4, text='USUÁRIO')
        self.labeltext_user_pgr.pack()

        self.entry_user_pgr = Entry(self.frame4, width=30)
        self.entry_user_pgr.pack(pady=5)

        self.labeltext_password_pgr = Label(self.frame5, text='SENHA')
        self.labeltext_password_pgr.pack()

        self.entry_password_pgr = Entry(self.frame5, width=30, show='*')
        self.entry_password_pgr.pack(pady=5)

        self.enter_button_pgr = Button(self.frame6, text='REGISTRAR', command=self.insert_user)
        self.enter_button_pgr.pack(side=LEFT)
    
        self.homepage = Button(self.frame6, text='VOLTAR', command=self.home_page)
        self.homepage.pack(side=LEFT)

    #eventos
    def main_page(self):
        self.frame.pack_forget()
        self.frame_main_page = Frame(root)


    def home_page(self):

        self.frame.pack_forget()
        App()
    

    def insert_user(self):

        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        user = self.entry_user_pgr.get()
        password = self.entry_password_pgr.get()

        if firstname == '' or  lastname == '' or user == '' or password == '':

            self.warning = messagebox.showinfo(title='', message='Campo de entradas em branco')


        else:

            response = usuarios.Users()
            response = response.insert_into(firstname, lastname, user, password)
            

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
    root.title('sistemaCadastro')
    App(root)
    root.mainloop()