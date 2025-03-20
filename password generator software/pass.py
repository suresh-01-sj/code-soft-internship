import random
import string
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("650x445+370+140")

        main_frame = Frame(self.root, bd=5, relief=RIDGE)
        main_frame.place(x=0, y=0, width=650, height=450)

        title_lbl = Label(main_frame, text="PASSWORD GENERATOR SOFTWARE", font=("times new roman", 20, "bold"), fg="red", bg="white")
        title_lbl.place(x=0, y=0, width=650)

        # Ensure the path to your image is correct
        img1 = Image.open(r"C:\Users\DELL\OneDrive\Documents\code soft internship\password generator software\image\Capture.PNG")
        img1 = img1.resize((650, 90), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg = Label(main_frame, image=self.photoimage1)
        lblimg.place(x=0, y=40, width=650)

        # Add password length label and entry
        self.length_label = Label(main_frame, text="Password Length:", font=("times new roman", 15, "bold"), bg="white")
        self.length_label.place(x=10, y=150)
        self.length_entry = Entry(main_frame, font=("times new roman", 15))
        self.length_entry.place(x=200, y=150)

        # Add generate button
        self.generate_btn = Button(main_frame, text="Generate Password", font=("times new roman", 15, "bold"), command=self.generate_password)
        self.generate_btn.place(x=10, y=200)

        # Add password display label
        self.password_display = Label(main_frame, text="", font=("times new roman", 15, "bold"), bg="white", fg="green")
        self.password_display.place(x=10, y=250)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1.")
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_display.config(text=password)
        except ValueError as e:
            self.password_display.config(text=str(e))

if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()
