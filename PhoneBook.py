import tkinter as tk
from tkinter import messagebox
import sqlite3

def save():
    connection = sqlite3.connect("phoneBook.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO contact(FirstName,LastName,PhoneNumber) VALUES(?,?)",(txtFirstName.get(),txtLastName.get(),txtPhoneNumber.get()))
    connection.commit()
    messagebox.showinfo("message","save successfuly")
    
form = tk.Tk()
lblFirstName = tk.Label(text="Firt Name")
lblLastName = tk.Label(text="Last Name")
lblPhoneNumber = tk.Label(text="Phone Number")
txtFirstName = tk.Entry()
txtLastName = tk.Entry()
txtPhoneNumber = tk.Entry()
btnsave = tk.Button(text="save contact", command=save)
lblFirstName.place(x="100",y="50")
lblLastName.place(x="100",y="70")
lblPhoneNumber.place(x="100",y="90")
txtFirstName.place(x="250",y="50")
txtLastName.place(x="250",y="70")
txtPhoneNumber.place(x="250",y="90")
btnsave.place(x="175",y="130")
form.geometry("500x500")
form.mainloop()

