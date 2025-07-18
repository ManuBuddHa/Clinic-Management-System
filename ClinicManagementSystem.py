import sqlite3
import tkinter as tk
from tkinter import messagebox
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
    def __init__(self, window):
        self.root = window
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

        self.loginButton = tk.Button(self.root,text="Login",command=self.login,width=12,bg="#0000CC",fg="#FFFFFF",font=("arial",12,"bold"),bd=5)
        self.loginButton.grid(row=2, column=0, columnspan=2,pady=20)
        self.signupButton = tk.Button(self.root, text="Sign Up", command=self.signup, width=12, bg="#00CC00", fg="#FFFFFF",
                                     font=("arial", 12,"bold"), bd=5)
        self.signupButton.grid(row=3, column=0,columnspan=2)

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username == "" or password == "":
            messagebox.showerror("Error","No username or password")
        else:
            pwd=db.execute("SELECT PASSWORD FROM users WHERE USERNAME=?", (username,)).fetchone()
            if pwd is None:
                messagebox.showerror("Error", "User Doesn't exist")
            elif pwd[0]!=password:
                messagebox.showerror("Error", "Incorrect username or password")
            else:
                if username=="admin":
                    self.admin_window()
                else:
                    messagebox.showinfo("Success", "Login successful")
                    self.user_window()

    def signup(self):
        self.clear_window()
        self.usernameLabel = tk.Label(self.root, text="Username : ", font=("arial", 18))
        self.passwordLabel = tk.Label(self.root, text="Password : ", font=("arial", 18))
        self.usernameEntry = tk.Entry(self.root, font=("arial", 14), width=20)
        self.passwordEntry = tk.Entry(self.root, show="*", font=("arial", 14), width=20)
        self.confirmPasswordLabel = tk.Label(self.root, text="Confirm Password : ", font=("arial", 18))
        self.confirmPasswordEntry = tk.Entry(self.root, show="*", font=("arial", 14), width=20)
        self.phoneNumberLabel = tk.Label(self.root, text="Phone Number: ", font=("arial", 18))
        self.phoneNumberEntry = tk.Entry(self.root, font=("arial", 14), width=20)
        self.emailLabel = tk.Label(self.root, text="Email : ", font=("arial", 18))
        self.emailEntry = tk.Entry(self.root, font=("arial", 14), width=20)
        self.usernameLabel.grid(row=0, column=0, pady=10)
        self.usernameEntry.grid(row=0, column=1, pady=10)
        self.passwordLabel.grid(row=1, column=0, pady=10)
        self.passwordEntry.grid(row=1, column=1, pady=10)
        self.confirmPasswordLabel.grid(row=2, column=0, pady=10)
        self.confirmPasswordEntry.grid(row=2, column=1, pady=10)
        self.phoneNumberLabel.grid(row=3, column=0, pady=10)
        self.phoneNumberEntry.grid(row=3, column=1, pady=10)
        self.emailLabel.grid(row=4, column=0, pady=10)
        self.emailEntry.grid(row=4, column=1, pady=10)
        def passCheck():
            cpwd = self.confirmPasswordEntry.get()
            pwd = self.passwordEntry.get()
            username = db.execute("SELECT * FROM users WHERE USERNAME=?", (self.usernameEntry.get(),)).fetchone()
            if pwd!=cpwd:
                messagebox.showerror("Error","Passwords Do Not Match")
            elif username:
                messagebox.showerror("Error","Username already exists")
            elif self.phoneNumberEntry.get()=="" or self.usernameEntry.get()=="" or self.passwordEntry.get()=="" or self.emailEntry.get()=="":
                messagebox.showerror("Error","Please Enter All Fields")
            else:
                db.execute("INSERT INTO users(USERNAME,PASSWORD,PHONE,MAIL) VALUES(?,?,?,?)",(self.usernameEntry.get(), self.passwordEntry.get(), self.phoneNumberEntry.get(), self.emailEntry.get()))
                conn.commit()
                messagebox.showinfo("Success","User Created!")
                self.createLogin()
        self.submitButton = tk.Button(self.root, text="Sign Up", command=passCheck, width=12, bg="#00CC00", fg="#FFFFFF", font=("arial", 12, "bold"), bd=5)
        self.submitButton.grid(row=5, column=0, pady=10)

    def admin_window(self):
        messagebox.showinfo("Admin","Welcome to Clinic Management System")
        self.clear_window()

        def add_med():
            messagebox.showinfo("Working on it", "Medicine Import Working")

        def view_appointments():
            messagebox.showinfo("Working on it", "Appointments")

        self.add_medicine_button = tk.Button(self.root, text="Medicine Inventory", font=("Ubuntu", 16), bd=2,command=add_med)
        self.add_medicine_button.grid(row=2, column=1)
        self.view_appointment = tk.Button(self.root, text="View Appointments", font=("Ubuntu", 16), bg="blue", fg="white", bd=2,command=view_appointments)
        self.view_appointment.grid(row=2, column=2)
        self.logout = tk.Button(self.root, text="Log Out", font=("Ubuntu",16),bg="red", fg="white", bd=2, command=self.createLogin)
        self.logout.grid(row=1,column=5)

    def user_window(self):
        username = self.usernameEntry.get()
        self.clear_window()
        self.username = tk.Label(self.root, text=f"Hello, {username}", font=("arial", 18))
        self.username.grid(row=0, column=0, pady=10)
        self.logout = tk.Button(self.root, text="Log Out", font=("Ubuntu", 16), bg="red", fg="white", bd=2,command=self.createLogin)
        self.logout.grid(row=1, column=5)



root = tk.Tk()
app = Main(root)
root.mainloop()
conn.close()