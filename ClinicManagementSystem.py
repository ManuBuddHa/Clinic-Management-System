import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
conn = sqlite3.connect('clinic.db')
db = conn.cursor()
db.execute("""
CREATE TABLE IF NOT EXISTS users (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
USERNAME TEXT,
PASSWORD TEXT,
PHONE NUMERIC,
MAIL TEXT
)
""")
class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinic Management System")
        self.root.geometry("800x800")
        self.createLogin()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def createLogin(self):
        self.clear_window()
        self.usernameLabel = tk.Label(self.root, text="Username : ",font=("arial",18))
        self.usernameLabel.grid(row=0, column=0,padx=10, pady=10)
        self.usernameEntry = tk.Entry(self.root, font=("arial",14), width=20)
        self.usernameEntry.grid(row=0, column=1,padx=10, pady=10)
        self.passwordLabel = tk.Label(self.root, text="Password : ",font=("arial",18))
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry = tk.Entry(self.root,show="*", font=("arial",14),width=20)
        self.passwordEntry.grid(row=1, column=1)
        def login():
            pass
        def signup():
            self.clear_window()
            self.usernameLabel = tk.Label(self.root, text="Username : ",font=("arial",18))
            self.usernameLabel.grid(row=0, column=0,padx=10, pady=10)
        self.loginButton = tk.Button(self.root,text="Login",command=login,width=12,bg="#0000CC",fg="#FFFFFF",font=("arial",12,"bold"),border=(5))
        self.loginButton.grid(row=2, column=0, columnspan=2,pady=20)
        self.signupButton = tk.Button(self.root, text="Sign Up", command=signup, width=12, bg="#00CC00", fg="#FFFFFF",
                                     font=("arial", 12,"bold"), border=(5))
        self.signupButton.grid(row=3, column=0,columnspan=2)
root = tk.Tk()
app = Main(root)
root.mainloop()
conn.close()