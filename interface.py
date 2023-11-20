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

        self.frame_pageregister = Frame(root)
        self.frame_pageregister.pack()

        self.frame1_pageregister = Frame(self.frame_pageregister)
        self.frame1_pageregister.pack()

        self.frame2_pageregister = Frame(self.frame_pageregister)
        self.frame2_pageregister.pack()

        self.frame3_pageregister = Frame(self.frame_pageregister)
        self.frame3_pageregister.pack()
        
        self.frame4_pageregister = Frame(self.frame_pageregister)
        self.frame4_pageregister.pack()

        self.frame5_pageregister = Frame(self.frame_pageregister)
        self.frame5_pageregister.pack()

        self.frame6_pageregister = Frame(self.frame_pageregister)
        self.frame6_pageregister.pack()
        

        #widgets
        self.label_title_pgr = Label(self.frame1_pageregister, text='REGISTER', font=('Roboto', 25))
        self.label_title_pgr.pack()

        self.labeltext_entry_firstname_pgr = Label(self.frame2_pageregister, text='FIRST NAME')
        self.labeltext_entry_firstname_pgr.pack(side=LEFT)

        self.entry_firstname_pgr = Entry(self.frame2_pageregister, width=30)
        self.entry_firstname_pgr.pack(padx=(0,40),pady=(5,5))

        self.labeltext_lastname_pgr = Label(self.frame3_pageregister, text='LAST NAME')
        self.labeltext_lastname_pgr.pack(side=LEFT)

        self.entry_lastname_pgr = Entry(self.frame3_pageregister, width=30)
        self.entry_lastname_pgr.pack(padx=(0,37),pady=(5,5))

        self.labeltext_user_pgr = Label(self.frame4_pageregister, text='USER')
        self.labeltext_user_pgr.pack(side=LEFT)

        self.entry_user_pgr = Entry(self.frame4_pageregister, width=30)
        self.entry_user_pgr.pack(padx=(0,2),pady=(5,5))

        self.labeltext_password_pgr = Label(self.frame5_pageregister, text='PASSWORD')
        self.labeltext_password_pgr.pack(side=LEFT)

        self.entry_password_pgr = Entry(self.frame5_pageregister, width=30)
        self.entry_password_pgr.pack(padx=(0,37),pady=(5,5))

        self.enter_button_pgr = Button(self.frame6_pageregister, text='ENTER', command=self.insert_user)
        self.enter_button_pgr.pack(side=LEFT, padx=(30,0))
    
        self.homepage = Button(self.frame6_pageregister, text='HOME PAGE', command=self.home_page)
        self.homepage.pack(side=LEFT)

    

    def home_page(self):

        self.frame_pageregister.pack_forget()
        App()
    

    def insert_user(self):

        self.firstname = self.entry_firstname_pgr.get()
        self.lastname = self.entry_lastname_pgr.get()
        self.user = self.entry_user_pgr.get()
        self.password = self.entry_password_pgr.get()

        i = usuarios.Users()
        i.insert_into(self.firstname,self.lastname,self.user,self.password)

        self.warning = messagebox.showinfo(title='Registrado', message='Você foi registrado com sucesso!')

        self.frame_pageregister.pack_forget()
        #volta para pagina principal
        self.home_page = App()
        self.home_page

    def message(self):

        user = self.user_entry.get()
        password = self.entry_password.get()
        c = usuarios.Users()
        c.check(user, password)
        self.warning = messagebox.showinfo(title='', message='Logado com sucesso!')
        
root = Tk()
root.geometry('300x220')
App(root)
root.mainloop()