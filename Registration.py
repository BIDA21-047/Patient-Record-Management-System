import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import hashlib
import re
import subprocess
import sys
from datetime import date
import os.path

#validation
def validation():
    if name_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input name")
    elif not name_entry.get().isalpha():
        messagebox.showerror("Error", "Please input text for name")
    elif surname_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input surname")
    elif not surname_entry.get().isalpha():
        messagebox.showerror("Error", "Please input text for surname")
    elif email_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input email")
    elif validate_email(email_entry.get()) == False:
        messagebox.showerror("Error", "Please input correct email")
    elif day_combobox.get().strip() == '' or month_combobox.get().strip() == '' or year_combobox.get().strip() == '':
        messagebox.showerror("Error", "Please input Date Of Birth")
    elif gender_combobox.get().strip() == '':
        messagebox.showerror("Error", "Please input Gender")
    elif contactno_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input Contact Number")
    elif not contactno_entry.get().isdigit():
        messagebox.showerror("Error", "Please input  Contact Number in numeric data type")
    elif physicaladdress_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input Physical Address")
    elif UserName_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input UserName")
    elif username_exists(UserName_entry.get()) != False:
        messagebox.showerror("Error", "Please input a different UserName")
    elif Password_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input Password")
    else:
        register_user()

# Validate for the email
def validate_email(email):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)|^$", email):
        return True
    return False

# Validate the unique of a username
def username_exists(username):

    flag = False

    if os.path.isfile("user_db.db"):
        print('Database exists!')
        # Connect to the database and check if table exists
        conn = sqlite3.connect("user_db.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM User")
        result = cursor.fetchone()
        if result[0] == 0:
            flag = False
        else:
            print(f"Table 'example_table' has {result[0]} rows.")

            #conn = sqlite3.connect("user_db.db")
            #cursor = conn.cursor()

            cursor.execute("SELECT * FROM user WHERE UserName=?", (username,))
            result = cursor.fetchone()

            conn.close()
            # print(result)
            return result is not None
    else:
        return flag



# Function to handle register button click
def register_user():
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    dateofbirth = day_combobox.get() + " " + month_combobox.get() + " " + year_combobox.get()
    #dateofbirth = dateofbirth_entry.get()
    gender = gender_combobox.get()
    contactno = contactno_entry.get()
    physicaladdress = physicaladdress_entry.get()
    UserName = UserName_entry.get()
    Password = hash_password(Password_entry.get())


    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Create User table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            email TEXT,
            dateofbirth TEXT,
            gender TEXT,
            contactno TEXT,
            physicaladdress TEXT,
            UserName TEXT,
            Password TEXT
        )
    """)

    # Insert user data into User table
    cursor.execute("INSERT INTO User (name, surname, email, dateofbirth, gender, contactno, physicaladdress, UserName, Password) VALUES (?, ?, ?, ?, ? , ? , ? , ? , ?)", (name, surname, email, dateofbirth, gender, contactno, physicaladdress, UserName, Password))

    # Commit changes to the database
    conn.commit()

    # Close database connection
    conn.close()

    # Show success message
    messagebox.showinfo("Success", "User registered successfully!")

    # Switch forms from Patient Registration to Patient Login
    nextform()


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
root.title("User Registration")
#root.geometry("800x600")

# Set the root window geometry to fit the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Prevent resizing of the root window
root.resizable(False, True)

#switch forms
def nextform():
    # Exit the first Python file
    # sys.exit()
    root.destroy()

    # Run another Python file using subprocess
    subprocess.run(["python", "Login_patient.py"])


# Frame to hold labels and entry fields
frame = tk.Frame(root)
frame.pack(pady=50)

# Heading
heading = tk.Label(frame, text="Patient Registration", font=("Helvetica", 24, "bold"))
heading.pack(padx=5)

# Labels
name_label = tk.Label(frame, text="Name:", font=("Helvetica", 14, "bold"), foreground="#FF7F50")
surname_label = tk.Label(frame, text='Surname: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
email_label = tk.Label(frame, text='Email: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
dateofbirth_label = tk.Label(frame, text='Date Of Birth: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
gender_label = tk.Label(frame, text='Gender: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
contactno_label = tk.Label(frame, text='Contact Number: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
physicaladdress_label = tk.Label(frame, text='Physical Address: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
UserName_label = tk.Label(frame, text='UserName: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )
Password_label = tk.Label(frame, text='Password: ', font=("Helvetica", 14, "bold"), foreground="#FF7F50" )

# Entry fields
name_entry = tk.Entry(frame)
surname_entry = tk.Entry(frame)
email_entry = tk.Entry(frame)
dateofbirth_entry = tk.Entry(frame)
gender_entry = tk.Entry(frame)
contactno_entry = tk.Entry(frame)
physicaladdress_entry = tk.Entry(frame)
UserName_entry = tk.Entry(frame)
Password_entry = tk.Entry(frame, show="*")

# Register button
register_button = tk.Button(root, text="Register", command=validation)
register_button.pack(pady=10)

# View button
view_button = tk.Button(root, text="View Users", command=view_users)
view_button.pack(pady=5)

#  testing: next button
next_button = tk.Button(root, text="Already have an account, Login", command=nextform)
next_button.pack(pady=5)

# Text widget
text = tk.Text(root, height=10, width=30)
text.pack(pady=5)

# Grid layout for labels and entry fields
heading.grid(row=1, column=0, padx=0, pady=5, sticky="e")
name_label.grid(row=2, column=0, padx=150, pady=5, sticky="e")
name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
surname_label.grid(row=3, column=0, padx=150, pady=5, sticky="e")
surname_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
email_label.grid(row=4, column=0, padx=150, pady=5, sticky="e")
email_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
dateofbirth_label.grid(row=5, column=0, padx=150, pady=5, sticky="e")
#dateofbirth_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
gender_label.grid(row=6, column=0, padx=150, pady=5, sticky="e")
#gender_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
contactno_label.grid(row=7, column=0, padx=150, pady=5, sticky="e")
contactno_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")
physicaladdress_label.grid(row=8, column=0, padx=150, pady=5, sticky="e")
physicaladdress_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")
UserName_label.grid(row=9, column=0, padx=150, pady=5, sticky="e")
UserName_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")
Password_label.grid(row=10, column=0, padx=150, pady=5, sticky="e")
Password_entry.grid(row=10, column=1, padx=10, pady=5, sticky="w")

#For Gender
#Combobox Selection
gender_combobox = ttk.Combobox(frame, values=["Male", "Female"], state='readonly', width=17)
gender_combobox.grid(row=6, column=1, padx=10, sticky="e")

# For the date
# Day selection
day_label = ttk.Label(frame, text="Day:")
day_label.grid(row=5, column=1, padx=0, sticky="e")
day_combobox = ttk.Combobox(frame, values=[str(i) for i in range(1, 32)], state='readonly', width=15)
day_combobox.grid(row=5, column=2, padx=0, sticky="e")

# Month selection
month_label = ttk.Label(frame, text="Month:")
month_label.grid(row=5, column=3, padx=0, sticky="w")
month_combobox = ttk.Combobox(frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state='readonly', width=15)
month_combobox.grid(row=5, column=4, padx=0, sticky="e")

# Year selection
year_label = ttk.Label(frame, text="Year:")
year_label.grid(row=5, column=5, padx=0, sticky="w")
year_combobox = ttk.Combobox(frame, values=[str(i) for i in range(1900, date.today().year + 1)], state='readonly', width=15)
year_combobox.grid(row=5, column=6, padx=0, sticky="e")

frame.columnconfigure(1, weight=1)

# Start GUI event loop
root.mainloop()
