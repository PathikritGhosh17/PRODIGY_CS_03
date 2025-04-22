#The Password Complexity Checker Tool
import re
import tkinter as tk
from tkinter import messagebox

def password_complexity_check(password):
    #Function to check the complexity of the password
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least 1 digit."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain an Uppercase Letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must contain a Lowercase Letter."
    
    if not re.search(r'[!@#$%^&*()_+-{};,./<>?:"~`]',password):
        return "Weak: Password must contain a Special Character."
    
    return "Strong: Your Password is strong and secured!!!"

#Function to use GUI
def password_checker_from_gui():
    password=entry.get()
    result=password_complexity_check(password)
    messagebox.showinfo("Result: ",result)

#GUI setup
root=tk.Tk()
root.title("The Password Complexity Checker Tool")
root.geometry("500x150")

#Password Input
lbl=tk.Label(root,text="Enter your Password")
lbl.pack(pady=10)
entry=tk.Entry(root,width=15)
entry.pack(pady=5)


btn=tk.Button(root,text="Check Password",command=password_checker_from_gui)
btn.pack(pady=5)
root.mainloop()