import tkinter

class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Title')
        self.root.geometry('300x220')

        self.frame = tkinter.Frame(self.root)
        self.frame.pack()

        self.label = tkinter.Label(self.frame, text='LOGIN',font=('Roboto',20) )
        self.label.pack()

        self.entry_user = tkinter.Entry(self.frame)
        self.entry_user.pack()

        self.entry_password = tkinter.Entry(self.frame)
        self.entry_password.pack()

        self.button_enter = tkinter.Button(self.frame, text='ENTER')
        self.button_enter.pack(side='left')

        self.button_cadastrar = tkinter.Button(self.frame, text='CADASTRAR', command= InterfaceCadastramento)
        self.button_cadastrar.pack(side='right')

        self.root.mainloop()
    

class InterfaceCadastramento:
    def __init__(self):

        self.root = tkinter.Tk()
        self.root.geometry('300x220')

        self.frame1 = tkinter.Frame(self.root)
        self.frame2 = tkinter.Frame(self.root)
        self.frame3 = tkinter.Frame(self.root)
        self.frame4 = tkinter.Frame(self.root)
        self.frame5 = tkinter.Frame(self.root)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        
        self.label_title = tkinter.Label(self.frame1, text='REGISTER', font=('Roboto',20))
        self.label_title.pack()

        self.label_text_entrey_user = tkinter.Label(self.frame2, text='USER')
        self.label_text_entrey_user.pack()

        self.entry_user = tkinter.Entry(self.frame3,)
        self.entry_user.pack()

        self.label_text_entrey_password = tkinter.Label(self.frame4, text='PASSWORD')
        self.label_text_entrey_password.pack()

        self.entry_password = tkinter.Entry(self.frame5)
        self.entry_password.pack()

        self.button_cadastrar = tkinter.Button(self.frame5, text='ENTER')
        self.button_cadastrar.pack()
        
        self.root.mainloop()




interface = App()