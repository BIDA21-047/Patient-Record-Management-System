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
        messagebox.showerror("Error", "Please input Contact Number in numeric data type")
    elif physicaladdress_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input Physical Address")
    elif UserName_entry.get().strip() == '':
        messagebox.showerror("Error", "Please input UserName")
    #elif username_exists(UserName_entry.get()) != False:
        #messagebox.showerror("Error", "Please input a different UserName")
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
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Administrator WHERE UserName=?", (username,))
    result = cursor.fetchone()

    conn.close()
    print(result)
    return result is not None

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
        CREATE TABLE IF NOT EXISTS Administrator (
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
    cursor.execute("INSERT INTO Administrator (name, surname, email, dateofbirth, gender, contactno, physicaladdress, UserName, Password) VALUES (?, ?, ?, ?, ? , ? , ? , ? , ?)", (name, surname, email, dateofbirth, gender, contactno, physicaladdress, UserName, Password))

    # Commit changes to the database
    conn.commit()

    # Close database connection
    conn.close()

    # Show success message
    messagebox.showinfo("Success", "Administrator registered successfully!")

    # Switch forms from Patient Registration to Patient Login
    nextform()


# Function to handle view button click
def view_users():
    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Retrieve all rows from User table
    cursor.execute("SELECT * FROM Administrator")
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
root.title("Administrator Registration")
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
    subprocess.run(["python", "Login_administrator.py"])


# Frame to hold labels and entry fields
frame = tk.Frame(root)
frame.pack(pady=50)

# Heading
heading = tk.Label(frame, text="Administrator Registration", font=("Helvetica", 24, "bold"))
heading.pack(padx=5)

# Labels
name_label = tk.Label(frame, text="Name:", font=("Helvetica", 10, "bold"), foreground="#FF7F50")
surname_label = tk.Label(frame, text='Surname: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")
email_label = tk.Label(frame, text='Email: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")
dateofbirth_label = tk.Label(frame, text='Date Of Birth: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")
gender_label = tk.Label(frame, text='Gender: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")
contactno_label = tk.Label(frame, text='Contact Number: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")
physicaladdress_label = tk.Label(frame, text='Physical Address: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")
UserName_label = tk.Label(frame, text='UserName: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")
Password_label = tk.Label(frame, text='Password: ', font=("Helvetica", 10, "bold"), foreground="#FF7F50")

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
register_button = tk.Button(root, text="Register", command=validation, pady=5, padx=25)
register_button.pack(pady=(5, 80), side=tk.LEFT, padx=(710, 10))

# View button
view_button = tk.Button(root, text="View Users", command=view_users)
view_button.pack(pady=5, side=tk.LEFT, padx=5)

#  testing: next button
next_button = tk.Button(root, text="Already have an account, Login", command=nextform)
next_button.pack(pady=5, side=tk.LEFT, padx=5)

# Text widget
text = tk.Text(root, height=10, width=30)
text.pack(pady=5, side=tk.LEFT, padx=5)

# Grid layout for labels and entry fields
heading.grid(row=1, column=0, padx=10, pady=5, sticky="w", columnspan=2)
name_label.grid(row=2, column=1, padx=0, pady=5, sticky="ew")
name_entry.grid(row=3, column=1, padx=0, pady=5, sticky="ew")
surname_label.grid(row=4, column=1, padx=0, pady=5, sticky="ew")
surname_entry.grid(row=5, column=1, padx=0, pady=5, sticky="ew")
email_label.grid(row=6, column=1, padx=0, pady=5, sticky="ew")
email_entry.grid(row=7, column=1, padx=0, pady=5, sticky="ew")
dateofbirth_label.grid(row=8, column=1, padx=0, pady=5, sticky="ew")
#dateofbirth_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
gender_label.grid(row=10, column=1, padx=0, pady=5, sticky="ew")
contactno_label.grid(row=12, column=1, padx=0, pady=5, sticky="ew")
contactno_entry.grid(row=13, column=1, padx=0, pady=5, sticky="ew")
physicaladdress_label.grid(row=14, column=1, padx=0, pady=5, sticky="ew")
physicaladdress_entry.grid(row=15, column=1, padx=0, pady=5, sticky="ew")
UserName_label.grid(row=16, column=1, padx=0, pady=5, sticky="ew")
UserName_entry.grid(row=17, column=1, padx=0, pady=5, sticky="ew")
Password_label.grid(row=18, column=1, padx=0, pady=5, sticky="ew")
Password_entry.grid(row=19, column=1, padx=0, pady=5, sticky="ew")

#For Gender
#Combobox Selection
gender_combobox = ttk.Combobox(frame, values=["Male", "Female"], state='readonly', width=17)
gender_combobox.grid(row=11, column=1, padx=10, sticky="ew")

# For the date
# Day selection
day_combobox = ttk.Combobox(frame, values=[str(i) for i in range(1, 32)], state='readonly', width=30)
day_combobox.grid(row=9, column=0, padx=0, sticky="ew")
day_combobox.set('Day')

# Month selection
month_combobox = ttk.Combobox(frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state='readonly', width=15)
month_combobox.grid(row=9, column=1, padx=0, sticky="ew")
month_combobox.set('Month')

# Year selection
year_combobox = ttk.Combobox(frame, values=[str(i) for i in range(1900, date.today().year + 1)], state='readonly', width=30)
year_combobox.grid(row=9, column=2, padx=0, sticky="ew")
year_combobox.set('Year')

frame.columnconfigure(1, weight=1)



# Start GUI event loop
root.mainloop()
