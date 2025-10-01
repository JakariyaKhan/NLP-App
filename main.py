from tkinter import *
from tkinter import messagebox

class NLP:
    def __init__(self):
        self.root = Tk()

        self.root.title("NLP App")
        self.root.configure(bg="#d9d9d9")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        # self.clear()
        heading = Label(self.root, text="NLP App", fg="black", bg="#d9d9d9", font=('Verdana', 20, 'bold'))
        heading.pack(pady=(20, 10))

        label1 = Label(self.root, text="Enter Email:", bg="#d9d9d9", font=('Verdana', 10))
        label1.pack(pady=(10, 0))
        self.email_input = Entry(self.root, width=40, fg="black")
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password:", bg="#d9d9d9", font=('Verdana', 10))
        label2.pack(pady=(10, 0))
        self.password_input = Entry(self.root, width=40, fg="black", show="*")
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text="Login", bg="green", fg="white", width=20, command=self.login)
        login_btn.pack(pady=(10, 10), ipady=4)

        label4 = Label(self.root, text="Not a member?", bg="#d9d9d9", font=('Verdana', 10))
        label4.pack(pady=(10, 0))
        register_btn = Button(self.root, text="Register here", bg="blue", fg="white", width=20, command=self.register_gui)
        register_btn.pack(pady=(5, 10), ipady=4)
