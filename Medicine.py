import sqlite3
import tkinter as tk
from tkinter import ttk,messagebox
db = sqlite3.connect('medicine.db')
meds = db.cursor()
meds.execute("""CREATE TABLE IF NOT EXISTS
medicines (med_id INTEGER PRIMARY KEY AUTOINCREMENT, 
med_name TEXT,
med_price FLOAT) 
""")


class Main:
    def __init__(self, root):
        self.tree = None
        self.root=root
        self.root.title("Medicines")
        self.root.geometry("600x600")
        self.med_manage()

    def med_manage(self):
        self.clear_window()
        self.name_label = tk.Label(self.root, text="Medicine Name : ",font=("Ubuntu", 16))
        self.name_input = tk.Entry(self.root, width=40,font=("Ubuntu", 16))
        self.price_label = tk.Label(self.root, text="Price : ",font=("Ubuntu", 16))
        self.price_input = tk.Entry(self.root, width=40,font=("Ubuntu", 16))
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_input.grid(row=0, column=1, padx=10, pady=10)
        self.price_label.grid(row=1, column=0, padx=10, pady=10)
        self.price_input.grid(row=1, column=1, padx=10, pady=10)

        def add_medicine():
            self.med_name = self.name_input.get()
            self.med_price = self.price_input.get()
            if meds.execute("INSERT INTO medicines(med_name,med_price) VALUES(?,?)",(self.med_name,self.med_price)):
                messagebox.showinfo("Success","Medicine Added")
                self.name_input.delete(0,tk.END)
                self.price_input.delete(0,tk.END)
            else:
                messagebox.showerror("Error","Medicine Not Added")

        def show_medicine():
            self.tree = (ttk.Treeview(self.root, columns=("ID", "Name", "Price"), show="headings"))
            self.tree.heading("ID", text="ID")
            self.tree.heading("Name", text="Name")
            self.tree.heading("Price", text="Price")
            self.tree.grid(row=4, column=1)
            self.populate_tree()
            self.tree.bind("<<TreeviewSelect>>",self.view_details)

        self.add_button = tk.Button(self.root, text="Add Medicine", font=("Ubuntu", 16), foreground="#FFFFFF",background="#00FF00", bd=3, command=add_medicine)
        self.add_button.grid(row=2, column=1, padx=10, pady=10)
        self.show_button = tk.Button(self.root, text="Show Medicines", foreground="#FFFFFF", background="#0000FF",font=("Ubuntu", 16), bd=3, command=show_medicine)
        self.show_button.grid(row=3, column=1, padx=10, pady=10)

    def populate_tree(self):
        medicines = meds.execute('SELECT * FROM medicines').fetchall()
        for i in medicines:
            self.tree.insert("", "end", values=i)

    def view_details(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            print(self.tree.item(selected_item[0],"values"))

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


root = tk.Tk()
app=Main(root)
root.mainloop()
meds.close()
db.commit()