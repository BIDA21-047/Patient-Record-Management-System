import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import hashlib
import re
import subprocess
import sys
from datetime import date

#validation
def validation():
    if UserName_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input UserName")
    #elif username_exists(UserName_entry.get()) != False:
    #    messagebox.showerror("Error", "Please input a different UserName")
    elif Password_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input Password")
    else:
        login(UserName_entry.get(), Password_entry.get())


# Validate the unique of a username
def login(username, password):
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Logged In Successfully")
        #print(user[1])
        homepage(str(user[0]))
        return True
    else:
        messagebox.showerror("Error", "Invalid username or password")
        return False



# Function to handle view button click
def view_users():
    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Retrieve all rows from User table
    cursor.execute("SELECT * FROM User")
    rows = cursor.fetchall()

    # Clear existing content in text widget
    text.delete(1.0, tk.END)

    # Append retrieved data to text widget
    for row in rows:
        text.insert(tk.END, f"ID: {row[0]}\n")
        text.insert(tk.END, f"Name: {row[1]}\n")
        text.insert(tk.END, f"Surname: {row[2]}\n")
        text.insert(tk.END, f"Email: {row[3]}\n")
        text.insert(tk.END, f"dateofbirth: {row[4]}\n")
        text.insert(tk.END, f"gender: {row[5]}\n")
        text.insert(tk.END, f"contactno: {row[6]}\n")
        text.insert(tk.END, f"physicaladdress: {row[7]}\n")
        text.insert(tk.END, f"UserName: {row[8]}\n")
        text.insert(tk.END, f"Password: {row[9]}\n")

    # Close database connection
    conn.close()

#Password Hashin
def hash_password(password):
    #password = Password_entry.get()
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return hashed_password

# Create main window
root = tk.Tk()
root.title("Patient Sign In")
#root.geometry("800x600")

# Set the root window geometry to fit the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Prevent resizing of the root window
root.resizable(False, True)

#switch to homepage
def homepage(id):
    # Exit the first Python file
    # sys.exit()
    root.destroy()

    #userhm = name + " " + surname

    # Run another Python file using subprocess
    #data_variable = "Hello, World!"
    subprocess.run(["python", "Homepage.py", id, "patient"])

#switch forms
def nextform():
    # Exit the first Python file
    # sys.exit()
    root.destroy()

    # Run another Python file using subprocess
    subprocess.run(["python", "Registration.py"])


# Frame to hold labels and entry fields
frame = tk.Frame(root)
frame.pack(pady=50)

# Heading
heading = tk.Label(frame, text="Patient Sign In", font=("Helvetica", 24, "bold"))
heading.pack(padx=5)

# Labels
UserName_label =  tk.Label(frame,text='UserName: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
Password_label =  tk.Label(frame,text='Password: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )

# Entry fields
UserName_entry = tk.Entry(frame)
Password_entry = tk.Entry(frame, show="*")

# Sign In button
signin_button = tk.Button(root, text="Sign In", command=validation)
signin_button.pack(pady=10)

# View button
view_button = tk.Button(root, text="View Users", command=view_users)
view_button.pack(pady=5)

#  testing: next button
next_button = tk.Button(root, text="New Patient, Registration", command=nextform)
next_button.pack(pady=5)

# Text widget
text = tk.Text(root, height=10, width=30)
text.pack(pady=5)

# Grid layout for labels and entry fields
heading.grid(row=1, column=0, padx=0, pady=5, sticky="e")
UserName_label.grid(row=8, column=0, padx=150, pady=5, sticky="e")
UserName_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")
Password_label.grid(row=9, column=0, padx=150, pady=5, sticky="e")
Password_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")

# Start GUI event loop
root.mainloop()
