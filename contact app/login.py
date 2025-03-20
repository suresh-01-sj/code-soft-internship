from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class LoginWindow(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        
        self.title("Login")
        self.geometry("400x300")
        
        s = Style()
        s.configure('Header.TFrame', background='blue')
        
        header_frame = Frame(self, style='Header.TFrame')
        header_frame.pack(fill=X)
        
        s.configure('Header.TLabel', background='blue', foreground="white",font=('Arial',25))
        header_label = Label(header_frame, text="My Contact Book", style = 'Header.TLabel')
        header_label.pack(pady=10)
        
        s.configure('Content.TFrame', background = 'white')
        
        content_frame = Frame(self, style = 'Content.TFrame')
        content_frame.pack(fill = BOTH,expand = TRUE)
        
        login_frame = Frame(content_frame, style = 'Content.TFrame')
        login_frame.place(relx = .5, rely = .5, anchor = CENTER)
        
        s.configure('Login.TLabel', background='white', font=('Arial',15))
        
        username_label = Label(login_frame, text = "Username:", style='Login.TLabel')
        username_label.grid(row=0,column=0)
        
        username_entry = Entry(login_frame, font=('Arial',15), width=15)
        username_entry.grid(row=0,column=1, pady=5)
        
        password_label = Label(login_frame, text = "Password:", style='Login.TLabel')
        password_label.grid(row=1,column=0)
        
        password_entry = Entry(login_frame, font=('Arial',15), width=15)
        password_entry.grid(row=1,column=1, pady=5)
        
        s.configure('Login.TButton', font=('Arial',15))
        
        login_button = Button(login_frame, text = "Login", style='Login.TButton', width=15)
        login_button.grid(row=2,column=1, pady=5)
        

lw = LoginWindow()
lw.mainloop()