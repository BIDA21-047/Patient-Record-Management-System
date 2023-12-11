import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import subprocess
import sys
from datetime import date


# Define the main window
root = tk.Tk()
root.title("Patient Management System")

frame = tk.Frame(root)
frame.grid(pady=50)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Prevent resizing of the root window
root.resizable(False, True)
root.configure(background="#F0F0F0")

#retrieve data variable from previous python
data_variable = sys.argv[1]
initial_tile = sys.argv[2]
admin_variable = ""
#messagebox.showerror("Error", data_variable)

def hide_objects():
    diagnosis_select_patient_label.grid_forget()
    combo_box.grid_forget()
    name_entry.grid_forget()
    surname_entry.grid_forget()
    email_entry.grid_forget()
    dateofbirth_entry.grid_forget()
    gender_entry.grid_forget()
    contactno_entry.grid_forget()
    physicaladdress_entry.grid_forget()
    btn.grid_forget()
    name_label.grid_forget()
    surname_label.grid_forget()
    email_label.grid_forget()
    dateofbirth_label.grid_forget()
    gender_label.grid_forget()
    contactno_label.grid_forget()
    physicaladdress_label.grid_forget()

    diagnosis_date_label.grid_forget()
    diagnosis_dates_combobox.grid_forget()
    diagnosis_date_check_btn.grid_forget()
    diagnosis_heartbeat_label.grid_forget()
    diagnosis_heartbeat_entry.grid_forget()
    diagnosis_heartpressure_label.grid_forget()
    diagnosis_heartpressure_entry.grid_forget()
    diagnosis_height_label.grid_forget()
    diagnosis_height_entry.grid_forget()
    diagnosis_weight_label.grid_forget()
    diagnosis_weight_entry.grid_forget()
    diagnosis_bloodsugar_label.grid_forget()
    diagnosis_bloodsugar_entry.grid_forget()
    diagnosis_cholesterol_label.grid_forget()
    diagnosis_cholesterol_entry.grid_forget()
    diagnosis_info_label.grid_forget()
    diagnosis_info_entry.grid_forget()
    diagnosis_doctor_feedback_label.grid_forget()
    diagnosis_doctor_feedback_entry.grid_forget()
    day_combobox.grid_forget()
    month_combobox.grid_forget()
    year_combobox.grid_forget()
    diagnosis_btn.grid_forget()

    #For the Medication tab
    add_medication_btn.grid_forget()
    add_medication_diagnosis_btn.grid_forget()

    medicine_name_label.grid_forget()
    medicine_name_entry.grid_forget()
    medicine_details_label.grid_forget()
    medicine_details_entry.grid_forget()
    medicine_type_label.grid_forget()
    medicine_type_combobox.grid_forget()
    medicine_size_label.grid_forget()
    medicine_size_entry.grid_forget()
    medicine_infants_label.grid_forget()
    medicine_infants_combobox.grid_forget()
    medicine_children_label.grid_forget()
    medicine_children_combobox.grid_forget()
    medicine_cures_label.grid_forget()
    medicine_cures_entry.grid_forget()
    medicine_side_effects_label.grid_forget()
    medicine_side_effects_entry.grid_forget()
    add_medicine_btn.grid_forget()
    view_medicine_btn.grid_forget()
    add_medicine_diagnosis_btn.grid_forget()
    open_medicine_diagnosis_btn.grid_forget()
    medicine_combo_box_label.grid_forget()
    medicine_combo_box.grid_forget()
    medicine_add_btn.grid_forget()
    listbox.grid_forget()
    medicine_clear_btn.grid_forget()
    medicine_quantity_label.grid_forget()
    medicine_quantity_entry.grid_forget()
    medicine_usage_label.grid_forget()
    medicine_usage_entry.grid_forget()
    add_medicine_prescription_btn.grid_forget()
    view_medicine_prescription_btn.grid_forget()

    view_patient_prescription_btn.grid_forget()
    prescription_text.grid_forget()

    add_lab_test_btn.grid_forget()
    add_lab_report_btn.grid_forget()

    lab_test_label.grid_forget()
    lab_test_entry.grid_forget()
    lab_test_details_label.grid_forget()
    lab_test_details_entry.grid_forget()
    lab_test_data_entry.grid_forget()
    lab_test_listbox_label.grid_forget()
    lab_test_unit_label.grid_forget()
    lab_test_unit_entry.grid_forget()
    lab_test_listbox.grid_forget()
    lab_test_add_btn.grid_forget()
    lab_test_clear_btn.grid_forget()
    lab_test_create_btn.grid_forget()
    lab_test_view_btn.grid_forget()

    view_patient_lab_report_btn.grid_forget()
    lab_report_text.grid_forget()

    open_lab_test_diagnosis_btn.grid_forget()
    add_lab_test_diagnosis_btn.grid_forget()
    lab_test_combo_box_label.grid_forget()
    lab_test_combo_box.grid_forget()
    choose_lab_test_btn.grid_forget()
    lab_report_listbox.grid_forget()
    lab_report_listbox_label.grid_forget()
    framelabreport.grid_forget()
    save_lab_report_btn.grid_forget()
    lab_report_comments_label.grid_forget()
    lab_report_comments_entry.grid_forget()
    view_report_btn.grid_forget()

    #for treatment
    diagnosis_select_patient_label.grid_forget()
    combo_box.grid_forget()
    treatment_name_label.grid_forget()
    treatment_name_entry.grid_forget()
    treatment_combo_box_label.grid_forget()
    treatment_combobox.grid_forget()
    treatment_start_date_label.grid_forget()
    treatment_start_day_combobox.grid_forget()
    treatment_start_month_combobox.grid_forget()
    treatment_start_year_combobox.grid_forget()
    treatment_end_date_label.grid_forget()
    treatment_end_day_combobox.grid_forget()
    treatment_end_month_combobox.grid_forget()
    treatment_end_year_combobox.grid_forget()
    treatment_doctor_label.grid_forget()
    treatment_doctor_combobox.grid_forget()
    save_treatment_btn.grid_forget()
    view_treatment_btn.grid_forget()

    treatment_combobox_label.grid_forget()
    treatment_combobox.grid_forget()
    view_patient_treatment_btn.grid_forget()
    treatment_text.grid_forget()
    treatment_patient_combobox.grid_forget()

    #admin widgets
    view_admin_details_btn.grid_forget()
    view_doctor_details_btn.grid_forget()
    view_patient_details_btn.grid_forget()
    admin_patients_combo_box.grid_forget()
    admin_doctors_combo_box.grid_forget()
    btn_save_doctor_details.grid_forget()
    btn_save_admin_details.grid_forget()
    btn_save_patient_details.grid_forget()
    admin_check_diagnosis_dates_btn.grid_forget()
    admin_check_patient_btn.grid_forget()
    admin_check_diagnosis_dates_btn.grid_forget()
    btn_save_diagnosis_details.grid_forget()
    admin_treatment_check_patient_btn.grid_forget()

    admin_alter_treatment_patient_btn.grid_forget()

    admin_medication_label.grid_forget()
    admin_medication_combobox.grid_forget()
    admin_medication_btn.grid_forget()
    save_admin_medicine_btn.grid_forget()

    #debug buttons
    debug_btn.grid_forget()

def type_diagnosis():
    if initial_tile == "Dr. ":
        input_diagnosis()
    elif initial_tile == "Admin":
        admin_diagnosis()
    else:
        diagnosis()

def admin_diagnosis():
    hide_objects()

    diagnosis_select_patient_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    combo_box.grid(row=1, column=2, padx=0, pady=10, sticky="ew")
    admin_check_patient_btn.grid(row=1, column=3, padx=10, pady=10, sticky="w")

def admin_diagnosis_ui():
    global admin_variable
    admin_variable = combo_box.get().strip(":")[0]
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Retrieve all rows from User table
    cursor.execute("SELECT id, dateofdiagnosis FROM PatientDiagnosis WHERE patientid = ?", admin_variable)
    rows = cursor.fetchall()

    choices = []

    for row in rows:
        str1 = str(row[0]) + ": " + str(row[1])
        choices.append(str1)

    diagnosis_dates_combobox["values"] = choices

    conn.close()

    diagnosis_date_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    diagnosis_dates_combobox.grid(row=2, column=2, padx=0, sticky="ew")
    admin_check_diagnosis_dates_btn.grid(row=2, column=3, padx=10, pady=10, sticky="w")

def admin_diagnosis_patient():
    global admin_variable
    admin_variable = diagnosis_dates_combobox.get().strip(":")[0]
    hide_objects()

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Retrieve all rows from User table
    cursor.execute("SELECT * FROM PatientDiagnosis WHERE id = ?", admin_variable)
    rows = cursor.fetchone()


    diagnosis_heartbeat_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    diagnosis_heartbeat_entry.grid(row=1, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_heartpressure_label.grid(row=1, column=3, padx=0, pady=0, sticky="e")
    diagnosis_heartpressure_entry.grid(row=1, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_height_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    diagnosis_height_entry.grid(row=2, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_weight_label.grid(row=2, column=3, padx=0, pady=0, sticky="e")
    diagnosis_weight_entry.grid(row=2, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_bloodsugar_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    diagnosis_bloodsugar_entry.grid(row=3, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_cholesterol_label.grid(row=3, column=3, padx=0, pady=0, sticky="e")
    diagnosis_cholesterol_entry.grid(row=3, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_info_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    diagnosis_info_entry.grid(row=4, column=2, padx=0, pady=0, sticky="ew", columnspan=2)
    diagnosis_doctor_feedback_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    diagnosis_doctor_feedback_entry.grid(row=5, column=2, padx=0, pady=0, sticky="ew", columnspan=2)

    diagnosis_heartbeat_entry.delete(0, "end")
    diagnosis_heartpressure_entry.delete(0, "end")
    diagnosis_height_entry.delete(0, "end")
    diagnosis_weight_entry.delete(0, "end")
    diagnosis_bloodsugar_entry.delete(0, "end")
    diagnosis_cholesterol_entry.delete(0, "end")
    diagnosis_info_entry.delete(0, "end")
    diagnosis_doctor_feedback_entry.delete(0, "end")


    diagnosis_heartbeat_entry.insert(0, str(rows[2]))
    diagnosis_heartpressure_entry.insert(0, str(rows[3]))
    diagnosis_height_entry.insert(0, str(rows[4]))
    diagnosis_weight_entry.insert(0, str(rows[5]))
    diagnosis_bloodsugar_entry.insert(0, str(rows[6]))
    diagnosis_cholesterol_entry.insert(0, str(rows[7]))
    diagnosis_info_entry.insert(0, str(rows[8]))
    diagnosis_doctor_feedback_entry.insert(0, str(rows[9]))

    if initial_tile == "Admin":
        btn_save_diagnosis_details.grid(row=6, column=2, padx=(150, 0), pady=0, sticky="w")

    conn.close()

def alter_admin_diagnosis_details():
    global admin_variable

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()


    # Example UPDATE statement with multiple column updates
    sql = "UPDATE PatientDiagnosis SET heartbeat = ?, heartpressure = ?, height = ?, weight = ?, bloodsugar = ?, cholesterol = ?, diagnosisinfo = ?, feedback = ? WHERE id = ?"

    # Example values for the column updates
    heartbeat = diagnosis_heartbeat_entry.get()
    heartpressure = diagnosis_heartpressure_entry.get()
    height = diagnosis_height_entry.get()
    weight = diagnosis_weight_entry.get()
    bloodsugar = diagnosis_bloodsugar_entry.get()
    cholesterol = diagnosis_cholesterol_entry.get()
    info = diagnosis_info_entry.get()
    feedback = diagnosis_doctor_feedback_entry.get()


    # Execute the UPDATE statement with multiple column updates
    cursor.execute(sql, (heartbeat, heartpressure, height, weight, bloodsugar, cholesterol, info, feedback, admin_variable))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Diagnosis Data Changed")

def diagnosis(): #for patient
    hide_objects()

    diagnosis_date_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    diagnosis_dates_combobox.grid(row=1, column=2, padx=0, sticky="ew")
    diagnosis_date_check_btn.grid(row=1, column=3, padx=25, pady=0, sticky="e")
    diagnosis_heartbeat_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    diagnosis_heartbeat_entry.grid(row=2, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_heartpressure_label.grid(row=2, column=3, padx=0, pady=0, sticky="e")
    diagnosis_heartpressure_entry.grid(row=2, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_height_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    diagnosis_height_entry.grid(row=3, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_weight_label.grid(row=3, column=3, padx=0, pady=0, sticky="e")
    diagnosis_weight_entry.grid(row=3, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_bloodsugar_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    diagnosis_bloodsugar_entry.grid(row=4, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_cholesterol_label.grid(row=4, column=3, padx=0, pady=0, sticky="e")
    diagnosis_cholesterol_entry.grid(row=4, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_info_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    diagnosis_info_entry.grid(row=5, column=2, padx=0, pady=0, sticky="ew", columnspan=2)
    diagnosis_doctor_feedback_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    diagnosis_doctor_feedback_entry.grid(row=6, column=2, padx=0, pady=0, sticky="ew", columnspan=2)

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM PatientDiagnosis WHERE patientid = ?", ((data_variable)))
    rows = cursor.fetchone()

    name_entry.insert(0, rows[1])
    surname_entry.insert(0, rows[2])
    email_entry.insert(0, rows[3])
    dateofbirth_entry.insert(0, rows[4])
    gender_entry.insert(0, rows[5])
    contactno_entry.insert(0, rows[6])
    physicaladdress_entry.insert(0, rows[7])

    # def disable_entries():
    if initial_tile == "patient":
        name_entry.config(state="disabled")
        surname_entry.config(state="disabled")
        email_entry.config(state="disabled")
        dateofbirth_entry.config(state="disabled")
        gender_entry.config(state="disabled")
        contactno_entry.config(state="disabled")
        physicaladdress_entry.config(state="disabled")

    # Request button to request for data change
    #btn.grid(row=8, column=2, padx=10, pady=10)

    conn.close()

def update_options(*args):
    search_term = search_var.get()
    filtered_values = [value for value in values if search_term.lower() in value.lower()]
    combo_box['values'] = filtered_values

def get_diagnosis(s):
    s = s.split(":")[0]

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM PatientDiagnosis WHERE ID = ?", ((str(s),)))
    rows = cursor.fetchone()

    diagnosis_heartbeat_entry.config(state="enable")
    diagnosis_heartpressure_entry.config(state="enable")
    diagnosis_height_entry.config(state="enable")
    diagnosis_weight_entry.config(state="enable")
    diagnosis_bloodsugar_entry.config(state="enable")
    diagnosis_cholesterol_entry.config(state="enable")
    diagnosis_info_entry.config(state="enable")
    diagnosis_doctor_feedback_entry.config(state="enable")

    #delete existing text
    diagnosis_heartbeat_entry.delete(0, "end")
    diagnosis_heartpressure_entry.delete(0, "end")
    diagnosis_height_entry.delete(0, "end")
    diagnosis_weight_entry.delete(0, "end")
    diagnosis_bloodsugar_entry.delete(0, "end")
    diagnosis_cholesterol_entry.delete(0, "end")
    diagnosis_info_entry.delete(0, "end")
    diagnosis_doctor_feedback_entry.delete(0, "end")

    #insert database data into text entries
    diagnosis_heartbeat_entry.insert(0, rows[2])
    diagnosis_heartpressure_entry.insert(0, rows[3])
    diagnosis_height_entry.insert(0, rows[4])
    diagnosis_weight_entry.insert(0, rows[5])
    diagnosis_bloodsugar_entry.insert(0, rows[6])
    diagnosis_cholesterol_entry.insert(0, rows[7])
    diagnosis_info_entry.insert(0, rows[8])
    diagnosis_doctor_feedback_entry.insert(0, rows[9])

    # def disable_entries():
    diagnosis_heartbeat_entry.config(state="disabled")
    diagnosis_heartpressure_entry.config(state="disabled")
    diagnosis_height_entry.config(state="disabled")
    diagnosis_weight_entry.config(state="disabled")
    diagnosis_bloodsugar_entry.config(state="disabled")
    diagnosis_cholesterol_entry.config(state="disabled")
    diagnosis_info_entry.config(state="disabled")
    diagnosis_doctor_feedback_entry.config(state="disabled")

    # Request button to request for data change
    #btn.grid(row=8, column=2, padx=10, pady=10)

    conn.close()

# Function to insert diagnosis of patient by doctor
def add_patient_diagnosis():
    dateofdiagnosis = day_combobox.get() + " " + month_combobox.get() + " " + year_combobox.get()
    heartbeat = diagnosis_heartbeat_entry.get()
    heartpressure = diagnosis_heartpressure_entry.get()
    height = diagnosis_height_entry.get()
    weight = diagnosis_weight_entry.get()
    bloodsugar = diagnosis_bloodsugar_entry.get()
    cholesterol = diagnosis_cholesterol_entry.get()
    diagnosisinfo = diagnosis_info_entry.get()
    feedback = diagnosis_doctor_feedback_entry.get()
    patientid = combo_box.get().split(":")[0]

    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Create User table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PatientDiagnosis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dateofdiagnosis TEXT,
            heartbeat TEXT,
            heartpressure TEXT,
            height TEXT,
            weight TEXT,
            bloodsugar TEXT,
            cholesterol TEXT,
            diagnosisinfo TEXT,
            feedback TEXT,
            patientid INTEGER
        )
    """)

    # Insert user data into User table
    cursor.execute("INSERT INTO PatientDiagnosis (dateofdiagnosis, heartbeat, heartpressure, height, weight, bloodsugar, cholesterol, diagnosisinfo, feedback, patientid) VALUES (?, ?, ?, ?, ? , ? , ? , ? , ?, ?)", (dateofdiagnosis, heartbeat, heartpressure, height, weight, bloodsugar, cholesterol, diagnosisinfo, feedback, int(patientid)))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patients diagnosis created successfully!")

# Function to handle view button click
def view_diagnosis():
    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Retrieve all rows from User table
    cursor.execute("SELECT * FROM PatientDiagnosis")
    rows = cursor.fetchall()

    # Clear existing content in text widget
    text.delete(1.0, tk.END)

    # Append retrieved data to text widget
    for row in rows:
        text.insert(tk.END, f"ID: {row[0]}\n")
        text.insert(tk.END, f"diagnosis_date: {row[1]}\n")
        text.insert(tk.END, f"heartbeat: {row[2]}\n")
        text.insert(tk.END, f"heartpressure: {row[3]}\n")
        text.insert(tk.END, f"hieght: {row[4]}\n")
        text.insert(tk.END, f"weight: {row[5]}\n")
        text.insert(tk.END, f"bloodsugar: {row[6]}\n")
        text.insert(tk.END, f"cholesterol: {row[7]}\n")
        text.insert(tk.END, f"diainfo: {row[8]}\n")
        text.insert(tk.END, f"feedback: {row[9]}\n")
        text.insert(tk.END, f"patientId: {row[10]}\n")

    # Close database connection
    conn.close()

def validation_input_diagnosis():
    if combo_box.get().strip() == '':
        messagebox.showerror("Error", "Please choose patient name")
    elif day_combobox.get() == "Day" or month_combobox.get() == "Month" or year_combobox.get() == "Year":
        messagebox.showerror("Error", "Please choose date of diagnosis")
    elif diagnosis_heartbeat_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter patients heartbeat")
    elif diagnosis_heartpressure_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter patients heartpressure")
    elif diagnosis_height_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter patients height")
    elif diagnosis_weight_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter patients weight")
    elif diagnosis_bloodsugar_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter patients blood sugar level")
    elif diagnosis_cholesterol_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter patients cholesterol level")
    elif diagnosis_info_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter diagnosis information")
    elif diagnosis_doctor_feedback_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter doctors feedback")
    else:
        add_patient_diagnosis()

def input_diagnosis(): # for doctor
    hide_objects()

    diagnosis_select_patient_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    
    combo_box.grid(row=1, column=2, padx=0, pady=10, sticky="w")

    diagnosis_date_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    diagnosis_date_label.configure(text="Please enter diagnosis date: ")
    #diagnosis_dates_combobox.grid(row=1, column=2, padx=0, sticky="ew")
    #diagnosis_date_check_btn.grid(row=1, column=3, padx=25, pady=0, sticky="e")
    diagnosis_heartbeat_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    diagnosis_heartbeat_entry.grid(row=3, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_heartpressure_label.grid(row=3, column=3, padx=0, pady=0, sticky="e")
    diagnosis_heartpressure_entry.grid(row=3, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_height_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    diagnosis_height_entry.grid(row=4, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_weight_label.grid(row=4, column=3, padx=0, pady=0, sticky="e")
    diagnosis_weight_entry.grid(row=4, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_bloodsugar_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    diagnosis_bloodsugar_entry.grid(row=5, column=2, padx=0, pady=0, sticky="ew")
    diagnosis_cholesterol_label.grid(row=5, column=3, padx=0, pady=0, sticky="e")
    diagnosis_cholesterol_entry.grid(row=5, column=4, padx=0, pady=0, sticky="ew")
    diagnosis_info_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    diagnosis_info_entry.grid(row=6, column=2, padx=0, pady=0, sticky="ew", columnspan=2)
    diagnosis_doctor_feedback_label.grid(row=7, column=1, padx=0, pady=0, sticky="e")
    diagnosis_doctor_feedback_entry.grid(row=7, column=2, padx=0, pady=0, sticky="ew", columnspan=2)

    # For the date
    # Day selection
    day_combobox.grid(row=2, column=2, padx=0, sticky="w")
    day_combobox.set('Day')

    # Month selection
    month_combobox.grid(row=2, column=2, padx=(120, 0), sticky="w")
    month_combobox.set('Month')

    # Year selection
    year_combobox.grid(row=2, column=2, padx=(240, 0), sticky="w")
    year_combobox.set('Year')

    #button to add tje diagnosis to database
    diagnosis_btn.grid(row=8, column=2, padx=10, pady=10, sticky="w")

    #View diagnosis
    debug_btn.grid(row=8, column=2, padx=(300, 0), pady=10, sticky="w")


def view_details():
    if initial_tile == "Dr. ":
        view_doctor_details()
    elif initial_tile == "Admin":
        clear_details_entries()
        admin_view_detail_buttons()
    else:
        view_patient_details()

def admin_view_detail_buttons():
    hide_objects()

    view_admin_details_btn.grid(row=1, column=1, padx=0, sticky="w")
    view_doctor_details_btn.grid(row=2, column=1, padx=0, sticky="w")
    view_patient_details_btn.grid(row=3, column=1, padx=0, sticky="w")
    admin_patients_combo_box.grid(row=3, column=2, padx=10, sticky="w")
    admin_doctors_combo_box.grid(row=2, column=2, padx=10, sticky="w")

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()

    choices = []

    for row in rows:
        str1 = str(row[0]) + ": " + str(row[1] + " " + str(row[2]))
        choices.append(str1)

    admin_patients_combo_box['values'] = choices

    cursor.execute("SELECT * FROM Doctor")
    rows = cursor.fetchall()

    choices.clear()
    for row in rows:
        str1 = str(row[0]) + ": " + str(row[1] + " " + str(row[2]))
        choices.append(str1)

    admin_doctors_combo_box['values'] = choices

    conn.close()

def clear_details_entries():
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    dateofbirth_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    contactno_entry.delete(0, tk.END)
    physicaladdress_entry.delete(0, tk.END)

def admin_view_doctors_details_validation():
    if admin_doctors_combo_box.get() == "":
        messagebox.showerror("Error", "Please Choose A Doctor")
    else:
        global admin_variable
        admin_variable = str(admin_doctors_combo_box.get().strip(":")[0])
        view_doctor_details()

def admin_view_patients_details_validation():
    if admin_patients_combo_box.get() == "":
        messagebox.showerror("Error", "Please Choose A Patient")
    else:
        global admin_variable
        admin_variable = str(admin_patients_combo_box.get().strip(":")[0])
        view_patient_details()

def view_admin_details():
    hide_objects()

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Administrator WHERE ID = ?", ((data_variable)))
    rows = cursor.fetchone()

    name_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    name_entry.grid(row=1, column=2, padx=0, pady=0, sticky="ew")
    surname_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    surname_entry.grid(row=2, column=2, padx=0, pady=10, sticky="ew")
    email_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    email_entry.grid(row=3, column=2, padx=0, pady=10, sticky="ew")
    dateofbirth_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    dateofbirth_entry.grid(row=4, column=2, padx=0, pady=10, sticky="ew")
    gender_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    gender_entry.grid(row=5, column=2, padx=0, pady=10, sticky="ew")
    contactno_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    contactno_entry.grid(row=6, column=2, padx=0, pady=10, sticky="ew")
    physicaladdress_label.grid(row=7, column=1, padx=0, pady=0, sticky="e")
    physicaladdress_entry.grid(row=7, column=2, padx=0, pady=10, sticky="ew")

    name_entry.insert(0, rows[1])
    surname_entry.insert(0, rows[2])
    email_entry.insert(0, rows[3])
    dateofbirth_entry.insert(0, rows[4])
    gender_entry.insert(0, rows[5])
    contactno_entry.insert(0, rows[6])
    physicaladdress_entry.insert(0, rows[7])

    # def disable_entries():
    #name_entry.config(state="disabled")
    #surname_entry.config(state="disabled")
    #email_entry.config(state="disabled")
    #dateofbirth_entry.config(state="disabled")
    #gender_entry.config(state="disabled")
    #contactno_entry.config(state="disabled")
    #physicaladdress_entry.config(state="disabled")

    # Request button to request for data change
    #btn.configure(text="Save Data")
    btn_save_admin_details.grid(row=8, column=2, padx=10, pady=10)

    conn.close()

def view_doctor_details():
    hide_objects()

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    global admin_variable

    if initial_tile == "Dr. ":
        cursor.execute("SELECT * FROM Doctor WHERE ID = ?", ((data_variable)))
    elif initial_tile == "Admin":
        cursor.execute("SELECT * FROM Doctor WHERE ID = ?", ((admin_variable)))
    rows = cursor.fetchone()

    name_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    name_entry.grid(row=1, column=2, padx=0, pady=0, sticky="ew")
    surname_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    surname_entry.grid(row=2, column=2, padx=0, pady=10, sticky="ew")
    email_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    email_entry.grid(row=3, column=2, padx=0, pady=10, sticky="ew")
    dateofbirth_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    dateofbirth_entry.grid(row=4, column=2, padx=0, pady=10, sticky="ew")
    gender_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    gender_entry.grid(row=5, column=2, padx=0, pady=10, sticky="ew")
    contactno_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    contactno_entry.grid(row=6, column=2, padx=0, pady=10, sticky="ew")
    physicaladdress_label.grid(row=7, column=1, padx=0, pady=0, sticky="e")
    physicaladdress_entry.grid(row=7, column=2, padx=0, pady=10, sticky="ew")

    name_entry.insert(0, rows[1])
    surname_entry.insert(0, rows[2])
    email_entry.insert(0, rows[3])
    dateofbirth_entry.insert(0, rows[4])
    gender_entry.insert(0, rows[5])
    contactno_entry.insert(0, rows[6])
    physicaladdress_entry.insert(0, rows[7])

    # def disable_entries():
    if initial_tile == "Dr. ":
        name_entry.config(state="disabled")
        surname_entry.config(state="disabled")
        email_entry.config(state="disabled")
        dateofbirth_entry.config(state="disabled")
        gender_entry.config(state="disabled")
        contactno_entry.config(state="disabled")
        physicaladdress_entry.config(state="disabled")

    # Request button to request for data change
    #btn.configure(text="Request for data change")
    #btn.grid(row=8, column=2, padx=10, pady=10)
    if initial_tile == "Admin":
        btn_save_doctor_details.grid(row=8, column=2, padx=(200, 0), pady=10, sticky="w")

    conn.close()

def alter_doctor_details():
    global admin_variable

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Example UPDATE statement with multiple column updates
    sql = "UPDATE Doctor SET name = ?, surname = ?, email = ?, dateofbirth = ?, gender = ?, contactno = ?, physicaladdress = ? WHERE id = ?"

    # Example values for the column updates
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    dateofbirth = dateofbirth_entry.get()
    gender = gender_entry.get()
    contactno = contactno_entry.get()
    physicaladdress = physicaladdress_entry.get()

    # Execute the UPDATE statement with multiple column updates
    cursor.execute(sql, (name, surname, email, dateofbirth, gender, contactno, physicaladdress, admin_variable))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Doctor Data Changed")

def alter_admin_details():
    global admin_variable

    admin_variable = str(data_variable)

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Example UPDATE statement with multiple column updates
    sql = "UPDATE Administrator SET name = ?, surname = ?, email = ?, dateofbirth = ?, gender = ?, contactno = ?, physicaladdress = ? WHERE id = ?"

    # Example values for the column updates
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    dateofbirth = dateofbirth_entry.get()
    gender = gender_entry.get()
    contactno = contactno_entry.get()
    physicaladdress = physicaladdress_entry.get()

    # Execute the UPDATE statement with multiple column updates
    cursor.execute(sql, (name, surname, email, dateofbirth, gender, contactno, physicaladdress, admin_variable))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Admin Data Changed")

def alter_patient_details():
    global admin_variable

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Example UPDATE statement with multiple column updates
    sql = "UPDATE user SET name = ?, surname = ?, email = ?, dateofbirth = ?, gender = ?, contactno = ?, physicaladdress = ? WHERE id = ?"

    # Example values for the column updates
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    dateofbirth = dateofbirth_entry.get()
    gender = gender_entry.get()
    contactno = contactno_entry.get()
    physicaladdress = physicaladdress_entry.get()

    # Execute the UPDATE statement with multiple column updates
    cursor.execute(sql, (name, surname, email, dateofbirth, gender, contactno, physicaladdress, admin_variable))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Patient Data Changed")

def view_patient_details():
    hide_objects()

    global admin_variable

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    if initial_tile == "patient":
        cursor.execute("SELECT * FROM User WHERE ID = ?", ((data_variable)))
    elif initial_tile == "Admin":
        cursor.execute("SELECT * FROM User WHERE ID = ?", ((admin_variable)))
    rows = cursor.fetchone()

    name_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    name_entry.grid(row=1, column=2, padx=0, pady=0, sticky="ew")
    surname_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    surname_entry.grid(row=2, column=2, padx=0, pady=10, sticky="ew")
    email_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    email_entry.grid(row=3, column=2, padx=0, pady=10, sticky="ew")
    dateofbirth_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    dateofbirth_entry.grid(row=4, column=2, padx=0, pady=10, sticky="ew")
    gender_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    gender_entry.grid(row=5, column=2, padx=0, pady=10, sticky="ew")
    contactno_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    contactno_entry.grid(row=6, column=2, padx=0, pady=10, sticky="ew")
    physicaladdress_label.grid(row=7, column=1, padx=0, pady=0, sticky="e")
    physicaladdress_entry.grid(row=7, column=2, padx=0, pady=10, sticky="ew")

    name_entry.insert(0, rows[1])
    surname_entry.insert(0, rows[2])
    email_entry.insert(0, rows[3])
    dateofbirth_entry.insert(0, rows[4])
    gender_entry.insert(0, rows[5])
    contactno_entry.insert(0, rows[6])
    physicaladdress_entry.insert(0, rows[7])

    # def disable_entries():
    if initial_tile == "patient":
        name_entry.config(state="disabled")
        surname_entry.config(state="disabled")
        email_entry.config(state="disabled")
        dateofbirth_entry.config(state="disabled")
        gender_entry.config(state="disabled")
        contactno_entry.config(state="disabled")
        physicaladdress_entry.config(state="disabled")

    # Request button to request for data change
    #btn.configure(text="Request for data change")
    if initial_tile == "Admin":
        btn_save_patient_details.grid(row=8, column=2, padx=10, pady=10)

    conn.close()

def type_medication():
    combo_box.config(state="enabled")
    combo_box.set("")
    if initial_tile == "Dr. ":
        doctor_medication()
    elif initial_tile == "Admin":
        admin_medication()
    else:
        patient_medication()

def admin_medication():
    hide_objects()

    admin_medication_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    admin_medication_combobox.grid(row=1, column=2, padx=0, sticky="ew")
    admin_medication_btn.grid(row=1, column=3, padx=10, sticky="w")

    choices = []
    str1 = ""
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medicine")
    rows = cursor.fetchall()

    for row in rows:
        str1 = str(row[0]) + ": " + str(row[1])
        choices.append(str1)

    admin_medication_combobox['values'] = choices

    conn.close()

def alter_admin_medication():
    if admin_medication_combobox.get() == "":
        messagebox.showerror("Error", "Please choose medication")
    else:
        alter_admin_medication_ui()

def alter_admin_medication_ui():
    global admin_variable
    admin_variable = admin_medication_combobox.get().split(":")[0]

    hide_objects()

    medicine_name_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    medicine_name_entry.grid(row=1, column=2, padx=0, pady=0, sticky="ew")
    medicine_details_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    medicine_details_entry.grid(row=2, column=2, padx=0, pady=0, sticky="ew")
    medicine_type_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    medicine_type_combobox.grid(row=3, column=2, padx=0, pady=0, sticky="ew")
    medicine_size_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    medicine_size_entry.grid(row=4, column=2, padx=0, pady=0, sticky="ew")
    medicine_infants_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    medicine_infants_combobox.grid(row=5, column=2, padx=0, pady=0, sticky="ew")
    medicine_children_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    medicine_children_combobox.grid(row=6, column=2, padx=0, pady=0, sticky="ew")
    medicine_cures_label.grid(row=7, column=1, padx=0, pady=0, sticky="e")
    medicine_cures_entry.grid(row=7, column=2, padx=0, pady=0, sticky="ew")
    medicine_side_effects_label.grid(row=8, column=1, padx=0, pady=(20, 20), sticky="e")
    medicine_side_effects_entry.grid(row=8, column=2, padx=0, pady=0, sticky="ew")
    #add_medicine_btn.grid(row=9, column=2, padx=0, pady=0, sticky="w")
    #view_medicine_btn.grid(row=9, column=2, padx=0, pady=0, sticky="e")
    save_admin_medicine_btn.grid(row=9, column=2, padx=0, pady=0, sticky="w")

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medicine WHERE id = ?", ((admin_variable)))
    rows = cursor.fetchone()

    # Example values for the column updates
    medicine_name_entry.delete(0, tk.END)
    medicine_details_entry.delete(0, tk.END)
    medicine_type_combobox.delete(0, tk.END)
    medicine_size_entry.delete(0, tk.END)
    #medicine_infants_combobox.get()
    #medicine_children_combobox.get()
    medicine_cures_entry.delete(0, tk.END)
    medicine_side_effects_entry.delete(0, tk.END)

    medicine_name_entry.insert(0, rows[1])
    medicine_details_entry.insert(0, rows[2])
    medicine_type_combobox.set(rows[3])
    medicine_size_entry.insert(0, rows[4])
    medicine_infants_combobox.set(rows[5])
    medicine_children_combobox.set(rows[6])
    medicine_cures_entry.insert(0, rows[7])
    medicine_side_effects_entry.insert(0, rows[8])

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    #messagebox.showinfo("Success", "Patient Data Changed")

def save_alter_admin_medication():
    global admin_variable

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Example UPDATE statement with multiple column updates
    sql = "UPDATE Medicine SET medicine_name = ?, medicine_details = ?, medicine_type = ?, medicine_size = ?, medicine_infants = ?, medicine_children = ?, medicine_cures = ?, medicine_side_effects = ? WHERE id = ?"

    # Example values for the column updates
    medicine_name = medicine_name_entry.get()
    medicine_details = medicine_details_entry.get()
    medicine_type = medicine_type_combobox.get()
    medicine_size = medicine_size_entry.get()
    medicine_infants = medicine_infants_combobox.get()
    medicine_children = medicine_children_combobox.get()
    medicine_cures = medicine_cures_entry.get()
    medicine_side_effects = medicine_side_effects_entry.get()

    # Execute the UPDATE statement with multiple column updates
    cursor.execute(sql, (medicine_name, medicine_details, medicine_type, medicine_size, medicine_infants, medicine_children, medicine_cures, medicine_side_effects, admin_variable))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Medicine Data Changed")


def patient_medication():
    hide_objects()

    diagnosis_date_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    diagnosis_dates_combobox.grid(row=1, column=2, padx=0, sticky="ew")
    view_patient_prescription_btn.grid(row=1, column=3, padx=10, sticky="w")

def view_patient_prescription_validation():
    if diagnosis_dates_combobox.get().strip() == '':
        messagebox.showerror("Error", "Please choose diagnosis date")
    else:
        view_patient_prescription()

def view_patient_prescription():
    prescription_text.grid(row=2, column=2, padx=0, sticky="w", columnspan=2)
    s = diagnosis_dates_combobox.get().split(":")[0]

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Prescription WHERE patient_diagnosis_id = ?", ((s)))
    rows = cursor.fetchall()
    prescription_text.delete(1.0, tk.END)

    for row in rows:
        prescription_text.insert(tk.END, f"Medicine Name: {row[1]}    Quantity: {row[2]}     Dosage: {row[3]} per day\n")

    conn.close()

def doctor_medication():
    hide_objects()

    add_medication_btn.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    add_medication_diagnosis_btn.grid(row=2, column=2, padx=10, pady=10, sticky="w")

def add_medication():
    hide_objects()

    medicine_name_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    medicine_name_entry.grid(row=1, column=2, padx=0, pady=0, sticky="ew")
    medicine_details_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    medicine_details_entry.grid(row=2, column=2, padx=0, pady=0, sticky="ew")
    medicine_type_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    medicine_type_combobox.grid(row=3, column=2, padx=0, pady=0, sticky="ew")
    medicine_size_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    medicine_size_entry.grid(row=4, column=2, padx=0, pady=0, sticky="ew")
    medicine_infants_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    medicine_infants_combobox.grid(row=5, column=2, padx=0, pady=0, sticky="ew")
    medicine_children_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    medicine_children_combobox.grid(row=6, column=2, padx=0, pady=0, sticky="ew")
    medicine_cures_label.grid(row=7, column=1, padx=0, pady=0, sticky="e")
    medicine_cures_entry.grid(row=7, column=2, padx=0, pady=0, sticky="ew")
    medicine_side_effects_label.grid(row=8, column=1, padx=0, pady=(20, 20), sticky="e")
    medicine_side_effects_entry.grid(row=8, column=2, padx=0, pady=0, sticky="ew")
    add_medicine_btn.grid(row=9, column=2, padx=0, pady=0, sticky="w")
    view_medicine_btn.grid(row=9, column=2, padx=0, pady=0, sticky="e")

def add_medicine_validation():
    if medicine_name_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter medicine name")
    elif medicine_details_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter medicine details")
    elif medicine_type_combobox.get().strip() == '':
        messagebox.showerror("Error", "Please choose medicine type")
    elif medicine_size_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter medicine size")
    elif medicine_infants_combobox.get().strip() == '':
        messagebox.showerror("Error", "Please choose if its suitable for infants")
    elif medicine_children_combobox.get().strip() == '':
        messagebox.showerror("Error", "Please choose if its suitable for children")
    elif medicine_cures_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter the medicine cures")
    elif medicine_side_effects_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter medicine side effects")
    else:
        add_medicine()

def add_medicine():
    medicine_name = medicine_name_entry.get()
    medicine_details = medicine_details_entry.get()
    medicine_type = medicine_type_combobox.get()
    medicine_size = medicine_size_entry.get()
    medicine_infants = medicine_infants_combobox.get()
    medicine_children = medicine_children_combobox.get()
    medicine_cures = medicine_cures_entry.get()
    medicine_side_effects = medicine_side_effects_entry.get()

    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Create User table if not exists
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Medicine (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_name TEXT,
                medicine_details TEXT,
                medicine_type TEXT,
                medicine_size TEXT,
                medicine_infants TEXT,
                medicine_children TEXT,
                medicine_cures TEXT,
                medicine_side_effects TEXT
            )
        """)

    # Insert user data into User table
    cursor.execute(
        "INSERT INTO Medicine (medicine_name, medicine_details, medicine_type, medicine_size, medicine_infants, medicine_children, medicine_cures, medicine_side_effects) VALUES (?, ?, ?, ?, ? , ? , ? , ? )",
        (medicine_name, medicine_details, medicine_type, medicine_size, medicine_infants, medicine_children, medicine_cures, medicine_side_effects))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Medicine Added Successfully!")

def view_medicine():
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medicine")
    rows = cursor.fetchall()
    text.delete(1.0, tk.END)

    for row in rows:
        text.insert(tk.END, f"ID: {row[0]}\n")
        text.insert(tk.END, f"medicine_name: {row[1]}\n")
        text.insert(tk.END, f"medicine_details: {row[2]}\n")
        text.insert(tk.END, f"medicine_type: {row[3]}\n")
        text.insert(tk.END, f"medicine_size: {row[4]}\n")
        text.insert(tk.END, f"medicine_infants: {row[5]}\n")
        text.insert(tk.END, f"medicine_children: {row[6]}\n")
        text.insert(tk.END, f"medicine_cures: {row[7]}\n")
        text.insert(tk.END, f"medicine_side_effects: {row[8]}\n")

    conn.close()

def medication_diagnosis():
    hide_objects()

    diagnosis_select_patient_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    combo_box.grid(row=1, column=2, padx=0, sticky="ew")
    open_medicine_diagnosis_btn.grid(row=1, column=3, padx=10, sticky="w")

def view_date_medication_diagnosis_check_empty():
    if combo_box.get().strip() == '':
        messagebox.showerror("Error", "Please choose a patient")
    else:
        view_date_medication_diagnosis()

def view_date_medication_diagnosis():
    s = combo_box.get().split(":")[0]
    combo_box.config(state="disabled")
    valuesdate = []
    try:
        conn = sqlite3.connect('user_db.db')
        cur = conn.cursor()
        cur.execute("SELECT id, dateofdiagnosis FROM PatientDiagnosis WHERE patientid = ?", ((s)))

        for row in cur.fetchall():
            valuesdate.append(str(row[0]) + ": " + str(row[1]))
    except sqlite3.OperationalError as e:
        print("patient diagnosis table does not exist")

    finally:
        cur.close()
        conn.close()

    diagnosis_dates_combobox['values'] = valuesdate
    diagnosis_date_label.grid(row=2, column=1, padx=0, sticky="e")
    diagnosis_dates_combobox.grid(row=2, column=2, padx=0, sticky="ew")
    add_medicine_diagnosis_btn.grid(row=2, column=3, padx=10, sticky="w")

def get_medication_diagnosis_check_empty():
    if diagnosis_dates_combobox.get().strip() == '':
        messagebox.showerror("Error", "Please choose a date of diagnosis")
    else:
        get_medication_diagnosis()

def get_medication_diagnosis():
    valuesmed = []
    try:
        conn = sqlite3.connect('user_db.db')
        cur = conn.cursor()
        cur.execute("SELECT medicine_name FROM Medicine")

        for row in cur.fetchall():
            valuesmed.append(str(row[0]))
    except sqlite3.OperationalError as e:
        print("Medicine Table does not exist")

    finally:
        cur.close()
        conn.close()

    medicine_combo_box_label.grid(row=3, column=1, padx=0, sticky="e")
    medicine_combo_box.grid(row=3, column=2, padx=0, sticky="ew")
    medicine_combo_box['values'] = valuesmed
    medicine_quantity_label.grid(row=4, column=1, padx=10, sticky="e")
    medicine_quantity_entry.grid(row=4, column=2, padx=10, sticky="ew")
    medicine_usage_label.grid(row=5, column=1, padx=10, sticky="e")
    medicine_usage_entry.grid(row=5, column=2, padx=10, sticky="ew")
    medicine_add_btn.grid(row=5, column=3, padx=10, sticky="w")
    listbox.grid(row=6, column=2, padx=0, sticky="ew", rowspan=1)
    medicine_clear_btn.grid(row=6, column=3, padx=10, sticky="w")
    add_medicine_prescription_btn.grid(row=7, column=2, padx=10, sticky="w")
    view_medicine_prescription_btn.grid(row=7, column=2, padx=10, sticky="e")

def add_medicine_listbox():
    if medicine_combo_box.get().strip() == '':
        messagebox.showerror("Error", "Please choose medicine name")
    elif medicine_quantity_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter medicine quantity")
    elif medicine_usage_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter dosage per day")
    else:
        item = medicine_combo_box.get() + " With" + " Quantity: " + medicine_quantity_entry.get() + " ,Take " + medicine_usage_entry.get() + " doses per day"
        if item:
            listbox.insert(tk.END, item)

def clear_medicine_listbox():
    listbox.delete(0, tk.END)

def add_prescription_validation():
    if listbox.size() == 0:
        messagebox.showerror("Error", "Please add medication to list")
    else:
        add_prescription()

def add_prescription():
    lines = listbox.get(0, tk.END)
    for line in lines:
        #print(line)
        myline = line.split()
        medicine_name = myline[0]
        medicine_quantity = myline[3]
        medicine_dosage = myline[5]
        patient_diagnosis_id = diagnosis_dates_combobox.get().split(":")[0]

        # Connect to SQLite3 database
        conn = sqlite3.connect("user_db.db")
        cursor = conn.cursor()

        # Create User table if not exists
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Prescription (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        medicine_name TEXT,
                        medicine_quantity TEXT,
                        medicine_dosage TEXT,
                        patient_diagnosis_id INTEGER
                    )
                """)

        # Insert user data into User table
        cursor.execute(
            "INSERT INTO Prescription (medicine_name, medicine_quantity, medicine_dosage, patient_diagnosis_id) VALUES (?, ?, ?, ?)",
            (medicine_name, medicine_quantity, medicine_dosage, patient_diagnosis_id))
        conn.commit()
        conn.close()

    messagebox.showinfo("Success", "Prescription Added Successfully!")

def view_prescription():

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Prescription")
    rows = cursor.fetchall()
    text.delete(1.0, tk.END)

    for row in rows:
        text.insert(tk.END, f"ID: {row[0]}\n")
        text.insert(tk.END, f"medicine_name: {row[1]}\n")
        text.insert(tk.END, f"medicine_quantity: {row[2]}\n")
        text.insert(tk.END, f"medicine_dosage: {row[3]}\n")
        text.insert(tk.END, f"patient_diagnosis_id: {row[4]}\n")

    conn.close()

def type_lab():
    if initial_tile == "Dr. ":
        doctor_lab()
    else:
        patient_lab()

def patient_lab(): #check 1132
    hide_objects()

    diagnosis_dates_combobox.set("")
    diagnosis_date_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    diagnosis_dates_combobox.grid(row=1, column=2, padx=0, sticky="ew")
    view_patient_lab_report_btn.grid(row=1, column=3, padx=10, sticky="w")
    lab_report_text.grid(row=2, column=2, padx=0, sticky="w", rowspan=4, columnspan=2)


def view_patient_lab_report():  # check code
    did = diagnosis_dates_combobox.get().split(":")[0]
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Labreports WHERE patientid = ? AND diagnosis_id = ?", ((data_variable), did))
    labrow = cursor.fetchone()
    lab_report_text.delete(1.0, tk.END)

    labid = (labrow[5])

    cursor.execute("SELECT * FROM Labtests WHERE id = ?", ((str(labid))))
    labrow1 = cursor.fetchone()

    print(data_variable + " id " + did + " diagid")
    print(labrow)
    print(labrow1)


    lab_report_text.insert(tk.END, f"The Lab Report:  {labrow1[1]}\n")
    lab_report_text.insert(tk.END, f"At Date Of :  {diagnosis_dates_combobox.get()}\n")

    var1 = labrow1[3].split(";")
    var2 = labrow[2].split(";")

    for row, row1 in zip(var1, var2):
        lab_report_text.insert(tk.END, f"{row}  :  {row1}\n")

    lab_report_text.insert(tk.END, f"Doctor's Notes :  {labrow[1]}\n")
    conn.close()

def doctor_lab():
    hide_objects()

    add_lab_test_btn.grid(row=1, column=2, padx=0, sticky="w")
    add_lab_report_btn.grid(row=2, column=2, padx=0, sticky="w")

def add_lab_test_ui():
    hide_objects()

    lab_test_label.grid(row=1, column=1, padx=10, sticky="w")
    lab_test_entry.grid(row=1, column=2, padx=10, sticky="ew")
    lab_test_details_label.grid(row=2, column=1, padx=10, sticky="w")
    lab_test_details_entry.grid(row=2, column=2, padx=10, sticky="ew")
    lab_test_data_entry.grid(row=3, column=2, padx=10, sticky="ew")
    lab_test_listbox_label.grid(row=3, column=1, padx=10, sticky="w")
    lab_test_unit_label.grid(row=3, column=3, padx=10, sticky="w")
    lab_test_unit_entry.grid(row=3, column=4, padx=10, sticky="w")
    lab_test_listbox.grid(row=4, column=2, padx=0, sticky="ew", rowspan=1)
    lab_test_add_btn.grid(row=4, column=3, padx=10, sticky="w")
    lab_test_clear_btn.grid(row=4, column=4, padx=10, sticky="w")
    lab_test_create_btn.grid(row=5, column=2, padx=10, sticky="w")
    lab_test_view_btn.grid(row=5, column=2, padx=10, sticky="e")

def add_lab_test_listbox():
    item = lab_test_data_entry.get() + "(" + lab_test_unit_entry.get() + ")"
    if item.strip() == "":
        messagebox.showerror("Error", "Please enter data about the lab test")
    elif lab_test_unit_entry.get().strip() == "":
        messagebox.showerror("Error", "Please enter the unit for the lab test data")
    else:
        lab_test_listbox.insert(tk.END, item)

def clear_lab_test_listbox():
    lab_test_listbox.delete(0, tk.END)

def create_lab_test_validation():
    if lab_test_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter lab test name")
    elif lab_test_details_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter lab test details")
    elif lab_test_listbox.size() == 0:
        messagebox.showerror("Error", "Please enter lab test data/variables")
    else:
        create_lab_test()

def create_lab_test():
    lab_test_name = lab_test_entry.get()
    lab_test_details = lab_test_details_entry.get()
    lab_test_string = ""
    for i in range(lab_test_listbox.size()):
        lab_test_string += lab_test_listbox.get(i) + ";"

    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Create User table if not exists
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS Labtests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lab_test_name TEXT,
                    lab_test_details TEXT,
                    lab_test_data TEXT
                )
            """)

    # Insert user data into User table
    cursor.execute(
        "INSERT INTO Labtests(lab_test_name, lab_test_details, lab_test_data) VALUES (?, ?, ?)",
        (lab_test_name, lab_test_details, lab_test_string))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Lab Test Created Successfully!")

def view_lab_test_validation():
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Labtests")
    rows = cursor.fetchall()
    text.delete(1.0, tk.END)

    for row in rows:
        text.insert(tk.END, f"ID: {row[0]}\n")
        text.insert(tk.END, f"lab_test_name: {row[1]}\n")
        text.insert(tk.END, f"lab_test_details: {row[2]}\n")
        text.insert(tk.END, f"lab_test_data: {row[3]}\n")

    conn.close()

def add_lab_report_ui():
    hide_objects()

    combo_box.config(state="enabled")
    combo_box.set("")
    diagnosis_select_patient_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    combo_box.grid(row=1, column=2, padx=0, sticky="ew")
    open_lab_test_diagnosis_btn.grid(row=1, column=3, padx=10, sticky="w")


def validate_lab_test_diagnosis_date():
    if combo_box.get() == "":
        messagebox.showerror("Error", "Please choose patient name")
    else:
        add_lab_report_ui_diagnosis()

def add_lab_report_ui_diagnosis():
    s = combo_box.get().split(":")[0]
    combo_box.config(state="disabled")
    valuesdate = []
    try:
        conn = sqlite3.connect('user_db.db')
        cur = conn.cursor()
        cur.execute("SELECT id, dateofdiagnosis FROM PatientDiagnosis WHERE patientid = ?", ((s)))

        for row in cur.fetchall():
            valuesdate.append(str(row[0]) + ": " + str(row[1]))
    except sqlite3.OperationalError as e:
        print("patient diagnosis table does not exist")

    finally:
        cur.close()
        conn.close()

    diagnosis_dates_combobox['values'] = valuesdate
    diagnosis_date_label.grid(row=2, column=1, padx=0, sticky="e")
    diagnosis_dates_combobox.grid(row=2, column=2, padx=0, sticky="ew")
    add_lab_test_diagnosis_btn.grid(row=2, column=3, padx=10, sticky="w")

def validate_lab_test_lab_test_ui():
    valuesmed = []
    try:
        conn = sqlite3.connect('user_db.db')
        cur = conn.cursor()
        cur.execute("SELECT id, lab_test_name FROM Labtests")

        for row in cur.fetchall():
            valuesmed.append(str(row[0]) + ": " + str(row[1]))
    except sqlite3.OperationalError as e:
        print("Medicine Table does not exist")

    finally:
        cur.close()
        conn.close()

    lab_test_combo_box_label.grid(row=3, column=1, padx=0, sticky="e")
    lab_test_combo_box.grid(row=3, column=2, padx=0, sticky="ew")
    lab_test_combo_box['values'] = valuesmed
    choose_lab_test_btn.grid(row=3, column=3, padx=0, sticky="ew")

def validate_lab_test():
    entry_data = []
    for child in framelabreport.winfo_children():
        if isinstance(child, (tk.Entry, tk.Label)):
            child.grid_remove()
    if lab_test_combo_box.get() == "":
        messagebox.showerror("Error", "Please Choose Lab Test")
    else:
        create_lab_report()

def create_lab_report():
    s = lab_test_combo_box.get().split(":")[0]
    lab_report_listbox_label.grid(row=4, column=1, padx=0, sticky="e")
   #lab_report_listbox.grid(row=4, column=2, padx=0, sticky="ew", rowspan=2)

    lab_variables = ""
    try:
        conn = sqlite3.connect('user_db.db')
        cur = conn.cursor()
        cur.execute("SELECT lab_test_data FROM Labtests WHERE id = ?", ((s)))

        for row in cur.fetchall():
            lab_variables = (str(row[0]))
    except sqlite3.OperationalError as e:
        print("Lab Tests Table does not exist")

    finally:
        cur.close()
        conn.close()

    lab_variables1 = lab_variables.split(";")

    framelabreport.grid(row=4, column=2, columnspan=4, rowspan=7, sticky="nw")

    for index, item in enumerate(lab_variables1):
        #print(index, item)
        #enterlistbox = entry_var.get()
        #if item:
        #lab_report_listbox.insert(tk.END, enterlistbox)
        #entry_var.set("")
        if index != (len(lab_variables1) - 1):
            label = tk.Label(framelabreport, text=item)
            label.grid(row=index, column=0, sticky="w")
            entry = tk.Entry(framelabreport)
            entry.grid(row=index, column=1, sticky="ew")

    lab_report_comments_label.grid(row=8, column=1, sticky="e")
    lab_report_comments_entry.grid(row=8, column=2, sticky="ew")
    save_lab_report_btn.grid(row=9, column=2, pady=10, sticky="w")
    view_report_btn.grid(row=9, column=3, padx=0, sticky="w")

def validate_lab_report():
    flag = False
    entry_data = []
    for child in (framelabreport.winfo_children()):
        if isinstance(child, tk.Entry):
            if child.get() == "":
                messagebox.showerror("Error", "Please Enter Lab Report Data")
                break
            elif combo_box.get() == "":
                messagebox.showerror("Error", "Please Choose Patient Name")
                break
            elif diagnosis_dates_combobox.get() == "":
                messagebox.showerror("Error", "Please Choose Diagnosis Date")
                break
            elif lab_test_combo_box.get() == "":
                messagebox.showerror("Error", "Please Choose Lab Test")
                break
            elif lab_report_comments_entry.get().strip() == "":
                messagebox.showerror("Error", "Please Enter Doctor's Comment")
                break
            else:
                flag = True
            entry_data.append(child.get())
    combined_data = ';'.join(entry_data)
    #print(combined_data)

    if flag == True:
        patientid = combo_box.get().split(":")[0]
        diagnosis_id = diagnosis_dates_combobox.get().split(":")[0]
        lab_test_id = lab_test_combo_box.get().split(":")[0]
        lab_report_comment = lab_report_comments_entry.get()

        # Connect to SQLite3 database
        conn = sqlite3.connect("user_db.db")
        cursor = conn.cursor()

        # Create User table if not exists
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Labreports (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            lab_report_comment TEXT,
                            combined_data TEXT,
                            patientid INTEGER,
                            diagnosis_id INTEGER,
                            lab_test_id INTEGER    
                        )
                    """)

        # Insert user data into User table
        cursor.execute(
            "INSERT INTO Labreports(lab_report_comment, combined_data, patientid, diagnosis_id, lab_test_id) VALUES (?, ?, ?, ?, ?)",
            (lab_report_comment, combined_data, int(patientid), int(diagnosis_id), int(lab_test_id)))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Lab Test Created Successfully!")

def view_lab_report_database():
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Labreports")
    rows = cursor.fetchall()
    text.delete(1.0, tk.END)

    for row in rows:
        text.insert(tk.END, f"ID: {row[0]}\n")
        text.insert(tk.END, f"lab_report_comment: {row[1]}\n")
        text.insert(tk.END, f"lab_data: {row[2]}\n")
        text.insert(tk.END, f"patient_id: {row[3]}\n")
        text.insert(tk.END, f"diagnosis_id: {row[4]}\n")
        text.insert(tk.END, f"lab_test_id: {row[5]}\n")

    conn.close()

def type_treatment():
    if initial_tile == "Dr. ":
        treatment_ui()
    elif initial_tile == "Admin":
        admin_treatment_ui()
    else:
        patient_treatment_ui()

def admin_treatment_ui():
    hide_objects()

    combo_box.config(state="enabled")
    combo_box.set("")
    diagnosis_select_patient_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    combo_box.grid(row=1, column=2, padx=0, sticky="ew")
    admin_treatment_check_patient_btn.grid(row=1, column=3, padx=0, sticky="w")
    treatment_name_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    treatment_name_entry.grid(row=2, column=2, padx=0, pady=0, sticky="ew")
    treatment_combo_box_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    treatment_combobox.grid(row=3, column=2, padx=0, pady=0, sticky="ew")
    treatment_start_date_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    treatment_start_day_combobox.set("Day")
    treatment_start_day_combobox.grid(row=4, column=2, padx=0, pady=0, sticky="w")
    treatment_start_month_combobox.set("Month")
    treatment_start_month_combobox.grid(row=4, column=2, padx=(120, 0), pady=0, sticky="w")
    treatment_start_year_combobox.set("Year")
    treatment_start_year_combobox.grid(row=4, column=2, padx=(240, 0), pady=0, sticky="w")
    treatment_end_date_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    treatment_end_day_combobox.set("Day")
    treatment_end_day_combobox.grid(row=5, column=2, padx=0, pady=0, sticky="w")
    treatment_end_month_combobox.set("Month")
    treatment_end_month_combobox.grid(row=5, column=2, padx=(120, 0), pady=0, sticky="w")
    treatment_end_year_combobox.set("Year")
    treatment_end_year_combobox.grid(row=5, column=2, padx=(240, 0), pady=0, sticky="w")
    treatment_doctor_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    treatment_doctor_combobox.grid(row=6, column=2, padx=0, pady=0, sticky="ew")
    #save_treatment_btn.grid(row=7, column=2, padx=0, pady=0, sticky="w")
    #view_treatment_btn.grid(row=7, column=2, padx=0, pady=0, sticky="e")
    admin_alter_treatment_patient_btn.grid(row=7, column=2, padx=0, pady=0, sticky="w")

    valuesdoctors = []
    try:
        conn = sqlite3.connect('user_db.db')
        cur = conn.cursor()
        cur.execute("SELECT id, name, surname FROM Doctor")

        for row in cur.fetchall():
            valuesdoctors.append(str(row[0]) + ": " + str(row[1]) + " " + str(row[2]))
    except sqlite3.OperationalError as e:
        print("Doctor table does not exist")

    finally:
        cur.close()
        conn.close()

    treatment_doctor_combobox['values'] = valuesdoctors

def admin_alter_treatment():
    global admin_variable
    #admin_variable =

    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Example UPDATE statement with multiple column updates
    sql = "UPDATE Treatments SET treatment_name = ?, treatment_type = ?, treatment_start_date = ?, treatment_end_date = ?, doctor_id = ? WHERE id = ?"

    # Example values for the column updates
    treatment_name = treatment_name_entry.get()
    treatment_type = treatment_combobox.get()
    treatment_start_date = treatment_start_day_combobox.get() + " " + treatment_start_month_combobox.get() + " " + treatment_start_year_combobox.get()
    treatment_end_date = treatment_end_day_combobox.get() + " " + treatment_end_month_combobox.get() + " " + treatment_end_year_combobox.get()
    doctorid = treatment_doctor_combobox.get().split(":")[0]

    print(treatment_name + " " + treatment_type + " " + treatment_start_date + " " + treatment_end_date + " " + doctorid)

    # Execute the UPDATE statement with multiple column updates
    cursor.execute(sql, (treatment_name, treatment_type, treatment_start_date, treatment_end_date, doctorid, admin_variable))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Treatment Data Changed")

def admin_treatment_details():
    global admin_variable
    admin_variable = combo_box.get().strip(":")[0]


    conn = sqlite3.connect('user_db.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Treatments WHERE patient_id = ?", ((admin_variable)))
    rows = cur.fetchone()
    #print(rows)

    admin_variable = rows[0]

    treatment_name_entry.insert(0, str(rows[1]))
    treatment_combobox.set(str(rows[2]))
    startdate = []
    startdate = str(rows[3].strip(" "))

    treatment_start_day_combobox.set(startdate[0])
    treatment_start_month_combobox.set(startdate[1])
    treatment_start_year_combobox.set(startdate[2])

    enddate = []
    enddate = str(rows[4].strip(" "))
    treatment_end_day_combobox.set(enddate[0])
    treatment_end_month_combobox.set(enddate[1])
    treatment_end_year_combobox.set(enddate[2])

    doctorid = str(rows[6])

    doctorlist = []
    str1 = ""

    cur.execute("SELECT * FROM Doctor")
    rows = cur.fetchall()

    for row in rows:
        str1 = str(row[0]) + ": " + str(row[1]) + " " + str(row[2])
        doctorlist.append(str1)

    #print(doctorlist)

    treatment_doctor_combobox["values"] = doctorlist

    treatment_doctor_combobox.set(doctorlist[int(doctorid) - 1])

    conn.close()


def patient_treatment_ui():
    hide_objects()

    treatment_combobox_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    treatment_patient_combobox.grid(row=1, column=2, padx=0, sticky="ew")
    view_patient_treatment_btn.grid(row=1, column=3, padx=10, sticky="w")
    treatment_text.grid(row=2, column=2, padx=0, sticky="w", rowspan=4, columnspan=2)

    choices = []
    str1 = ""
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Treatments WHERE patient_id = ?", ((data_variable)))
    rows = cursor.fetchall()

    for row in rows:
        str1 = str(row[0]) + ": " + str(row[1])
        choices.append(str1)

    treatment_patient_combobox['values'] = choices

    conn.close()

def view_patient_treatment():
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Treatments WHERE patient_id = ?", ((data_variable)))
    rows = cursor.fetchall()

    for row in rows:
        treatment_text.insert(tk.END, f"Treatment Name: {row[1]}\n")
        treatment_text.insert(tk.END, f"Treatment Type: {row[2]}\n")
        treatment_text.insert(tk.END, f"Treatment Start Date: {row[3]}\n")
        treatment_text.insert(tk.END, f"Treatment End Date: {row[4]}\n")

        cursor.execute("SELECT * FROM Doctor WHERE id = ?", ((str(row[6]))))
        r = cursor.fetchone()
        treatment_text.insert(tk.END, f"Doctor In Charge: Dr. {r[1]} {r[2]}\n")

        treatment_text.insert(tk.END, f"\n\n\n")
    conn.close()


def treatment_ui():
    hide_objects()

    combo_box.config(state="enabled")
    combo_box.set("")
    diagnosis_select_patient_label.grid(row=1, column=1, padx=0, pady=0, sticky="e")
    combo_box.grid(row=1, column=2, padx=0, sticky="ew")
    treatment_name_label.grid(row=2, column=1, padx=0, pady=0, sticky="e")
    treatment_name_entry.grid(row=2, column=2, padx=0, pady=0, sticky="ew")
    treatment_combo_box_label.grid(row=3, column=1, padx=0, pady=0, sticky="e")
    treatment_combobox.grid(row=3, column=2, padx=0, pady=0, sticky="ew")
    treatment_start_date_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")
    treatment_start_day_combobox.set("Day")
    treatment_start_day_combobox.grid(row=4, column=2, padx=0, pady=0, sticky="w")
    treatment_start_month_combobox.set("Month")
    treatment_start_month_combobox.grid(row=4, column=2, padx=(120, 0), pady=0, sticky="w")
    treatment_start_year_combobox.set("Year")
    treatment_start_year_combobox.grid(row=4, column=2, padx=(240, 0), pady=0, sticky="w")
    treatment_end_date_label.grid(row=5, column=1, padx=0, pady=0, sticky="e")
    treatment_end_day_combobox.set("Day")
    treatment_end_day_combobox.grid(row=5, column=2, padx=0, pady=0, sticky="w")
    treatment_end_month_combobox.set("Month")
    treatment_end_month_combobox.grid(row=5, column=2, padx=(120, 0), pady=0, sticky="w")
    treatment_end_year_combobox.set("Year")
    treatment_end_year_combobox.grid(row=5, column=2, padx=(240, 0), pady=0, sticky="w")
    treatment_doctor_label.grid(row=6, column=1, padx=0, pady=0, sticky="e")
    treatment_doctor_combobox.grid(row=6, column=2, padx=0, pady=0, sticky="ew")
    save_treatment_btn.grid(row=7, column=2, padx=0, pady=0, sticky="w")
    view_treatment_btn.grid(row=7, column=2, padx=0, pady=0, sticky="e")


    valuesdoctors = []
    try:
        conn = sqlite3.connect('user_db.db')
        cur = conn.cursor()
        cur.execute("SELECT id, name, surname FROM Doctor")

        for row in cur.fetchall():
            valuesdoctors.append(str(row[0]) + ": " + str(row[1]) + " " + str(row[2]))
    except sqlite3.OperationalError as e:
        print("Doctor table does not exist")

    finally:
        cur.close()
        conn.close()

    treatment_doctor_combobox['values'] = valuesdoctors

def validate_save_treatment():
    if combo_box.get() == '':
        messagebox.showerror("Error", "Please choose patient name")
    elif treatment_name_entry.get().strip() == '':
        messagebox.showerror("Error", "Please enter treatment name")
    elif treatment_combobox.get() == '':
        messagebox.showerror("Error", "Please choose treatment type")
    elif treatment_start_day_combobox.get() == "Day" or treatment_start_month_combobox.get() == "Month" or treatment_start_year_combobox.get() == "Year":
        messagebox.showerror("Error", "Please choose start date of treatment")
    elif treatment_end_day_combobox.get() == "Day" or treatment_end_month_combobox.get() == "Month" or treatment_end_year_combobox.get() == "Year":
        messagebox.showerror("Error", "Please choose end date of treatment")
    elif treatment_doctor_combobox.get() == '':
        messagebox.showerror("Error", "Please choose a doctor in charge")
    else:
        save_treatment()

def save_treatment():
    treatment_name = treatment_name_entry.get()
    treatment_type = treatment_combobox.get()
    treatment_start_date = treatment_start_day_combobox.get() + " " + treatment_start_month_combobox.get() + " " + treatment_start_year_combobox.get()
    treatment_end_date = treatment_end_day_combobox.get() + " " + treatment_end_month_combobox.get() + " " + treatment_end_year_combobox.get()
    patientid = combo_box.get().split(":")[0]
    doctorid = treatment_doctor_combobox.get().split(":")[0]

    # Connect to SQLite3 database
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()

    # Create User table if not exists
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Treatments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        treatment_name TEXT,
                        treatment_type TEXT,
                        treatment_start_date TEXT,
                        treatment_end_date TEXT,
                        patient_id INTEGER,
                        doctor_id INTEGER
                    )
                """)

    # Insert user data into User table
    cursor.execute(
        "INSERT INTO Treatments(treatment_name, treatment_type, treatment_start_date, treatment_end_date, patient_id, doctor_id) VALUES (?, ?, ?, ?, ?, ?)",
        (treatment_name, treatment_type, treatment_start_date, treatment_end_date, patientid, doctorid))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Treatment Created Successfully!")

def view_treatment():
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Treatments")
    rows = cursor.fetchall()
    text.delete(1.0, tk.END)

    for row in rows:
        text.insert(tk.END, f"ID: {row[0]}\n")
        text.insert(tk.END, f"treatment_name: {row[1]}\n")
        text.insert(tk.END, f"treatment_type: {row[2]}\n")
        text.insert(tk.END, f"treatment_start_date: {row[3]}\n")
        text.insert(tk.END, f"treatment_end_date: {row[4]}\n")
        text.insert(tk.END, f"patientid {row[5]}\n")
        text.insert(tk.END, f"doctorid {row[6]}\n")

    conn.close()

def logout():
    # Exit the first Python file
    # sys.exit()
    root.destroy()

    # Run another Python file using subprocess
    if initial_tile == "Dr. ":
        subprocess.run(["python", "Login_doctor.py"])
    elif initial_tile == "Admin":
        subprocess.run(["python", "Login_administrator.py"])
    else:
        subprocess.run(["python", "Login_patient.py"])

# Define the left frame
#left_frame = ttk.Frame(root, padding=20)
#left_frame.grid(row=0, column=0, sticky="ns")

# Define the database connection and cursor
#conn = sqlite3.connect('patients.db')
#c = conn.cursor()

# Retrieve the name of the patient from the database
#c.execute("SELECT name FROM User WHERE id = 1")
#patient_name = c.fetchone()[0]

# Set the style for the buttons and heading
style = ttk.Style()

style.configure("TButton", padding=10, relief="flat",
                foreground="black", background="#ADD8E6",
                font=("Arial", 14, "bold"))

style.configure("TLabel", foreground="#333", background="white",
                font=("Arial", 24))

# Create 6 buttons on the left side of the application
if initial_tile == "Dr. ":
    button1 = ttk.Button(root, text="Doctor Details", command=view_details)
elif initial_tile == "Admin":
    button1 = ttk.Button(root, text="Admin Details", command=view_details)
else:
    button1 = ttk.Button(root, text="Patients Details", command=view_details)
button1.grid(row=1, column=0,  padx=70, pady=10, sticky="ew")

button2 = ttk.Button(root, text="Diagnosis", command=type_diagnosis)
button2.grid(row=2, column=0, padx=70, pady=10, sticky="ew")

button3 = ttk.Button(root, text="Medication", command=type_medication)
button3.grid(row=3, column=0, padx=70, pady=10, sticky="ew")

button4 = ttk.Button(root, text="Lab Results", command=type_lab)
button4.grid(row=4, column=0, padx=70, pady=10, sticky="ew")

button5 = ttk.Button(root, text="Treatment", command=type_treatment)
button5.grid(row=5, column=0, padx=70, pady=10, sticky="ew")

button6 = ttk.Button(root, text="Log Out", command=logout)
button6.grid(row=6, column=0, padx=70, pady=10, sticky="ew")

#For output correct name on heading
if (initial_tile == "Dr. "):
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Doctor WHERE ID = ?", ((data_variable)))
    rows = cursor.fetchone()
    conn.close()
elif initial_tile == "Admin":
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Administrator WHERE ID = ?", ((data_variable)))
    rows = cursor.fetchone()
    conn.close()
else:
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE ID = ?", ((data_variable)))
    rows = cursor.fetchone()
    conn.close()

#Add a big heading in the middle
if(initial_tile == "Dr. "):
    heading = ttk.Label(root, text="Record for Doctor: " + initial_tile + rows[1] + " " + rows[2])
elif(initial_tile == "Admin"):
    heading = ttk.Label(root, text="Record for Administrator: " + initial_tile + " " + rows[1] + " " + rows[2])
else:
    heading = ttk.Label(root, text="Record for Patient: " + rows[1] + " " + rows[2])
heading.grid(row=0, column=1, columnspan=2, padx=60, pady=10)

name_label = tk.Label(root, text="Name:", font=("Helvetica", 8, "bold"))
surname_label = tk.Label(root, text="Surname:", font=("Helvetica", 8, "bold"))
email_label = tk.Label(root, text="Email:", font=("Helvetica", 8, "bold"))
dateofbirth_label = tk.Label(root, text="Date of Birth:", font=("Helvetica", 8, "bold"))
gender_label = tk.Label(root, text="Gender:", font=("Helvetica", 8, "bold"))
contactno_label = tk.Label(root, text="Contact No:", font=("Helvetica", 8, "bold"))
physicaladdress_label = tk.Label(root, text="Physical Address:", font=("Helvetica", 8, "bold"))

#button to request patient data change
btn = tk.Button(root, text="Request for data change", padx=10, pady=5)

#Entry for patient details
name_entry = ttk.Entry(root)
surname_entry = ttk.Entry(root)
email_entry = ttk.Entry(root)
dateofbirth_entry = ttk.Entry(root)
gender_entry = ttk.Entry(root)
contactno_entry = ttk.Entry(root)
physicaladdress_entry = ttk.Entry(root)

#For the Diagnosis

# Testing: Populate from database
diagnosis_select_patient_label = tk.Label(root, text="Please select the patient: ", font=("Helvetica", 8, "bold"))

#sql to retrieve the names and surnames from patient table from database
values = []
try:
    conn = sqlite3.connect('user_db.db')
    cur = conn.cursor()
    cur.execute("SELECT id, name, surname FROM user")

    for row in cur.fetchall():
        values.append(str(row[0]) + ': ' + row[1] + " " + row[2])
except sqlite3.OperationalError as e:
    print("patient diagnosis table does not exist")
finally:
    cur.close()
    conn.close()
search_var = tk.StringVar()
search_var.trace('w', update_options)
#combo_box = ttk.Combobox(root, values=values, textvariable=search_var)
combo_box = ttk.Combobox(root, values=values, textvariable=search_var)# for the patient data
combo_box.bind('<KeyRelease>', update_options)


#SQL to populate the patient diagnosis dates
valuesdate = []
try:
    conn = sqlite3.connect('user_db.db')
    cur = conn.cursor()
    cur.execute("SELECT id, dateofdiagnosis FROM PatientDiagnosis WHERE patientid = ?", ((data_variable)))

    for row in cur.fetchall():
        valuesdate.append(str(row[0]) + ": " + str(row[1]))
except sqlite3.OperationalError as e:
    print("patient diagnosis table does not exist")

finally:
    cur.close()
    conn.close()

diagnosis_date_label = tk.Label(root, text="Please choose the date of diagnosis", font=("Helvetica", 8, "bold"))
diagnosis_dates_combobox = ttk.Combobox(root, values=valuesdate, state='readonly')
diagnosis_date_check_btn = tk.Button(root, text="View Diagnosis", padx=10, pady=5, command=lambda: get_diagnosis(str(diagnosis_dates_combobox.get())))

diagnosis_heartbeat_label = tk.Label(root, text="Heartbeat", font=("Helvetica", 8, "bold"))
diagnosis_heartbeat_entry = ttk.Entry(root)

diagnosis_heartpressure_label = tk.Label(root, text="Heart Pressure", font=("Helvetica", 8, "bold"))
diagnosis_heartpressure_entry = ttk.Entry(root)

diagnosis_height_label = tk.Label(root, text="Height(cm)", font=("Helvetica", 8, "bold"))
diagnosis_height_entry = ttk.Entry(root)

diagnosis_weight_label = tk.Label(root, text="Weight(grams)", font=("Helvetica", 8, "bold"))
diagnosis_weight_entry = ttk.Entry(root)

diagnosis_bloodsugar_label = tk.Label(root, text="Blood Sugar Levels(mg/dL)", font=("Helvetica", 8, "bold"))
diagnosis_bloodsugar_entry = ttk.Entry(root)

diagnosis_cholesterol_label = tk.Label(root, text="Cholesterol Levels(mg/dL)", font=("Helvetica", 8, "bold"))
diagnosis_cholesterol_entry = ttk.Entry(root)

diagnosis_info_label = tk.Label(root, text="Diagnosis Information", font=("Helvetica", 8, "bold"))
diagnosis_info_entry = ttk.Entry(root)

diagnosis_doctor_feedback_label = tk.Label(root, text="Doctor Feedback", font=("Helvetica", 8, "bold"))
diagnosis_doctor_feedback_entry = ttk.Entry(root)

day_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 32)], state='readonly', width=15)
month_combobox = ttk.Combobox(root, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state='readonly', width=15)
year_combobox = ttk.Combobox(root, values=[str(i) for i in range(1900, date.today().year + 1)], state='readonly', width=15)

diagnosis_btn = tk.Button(root, text="Add Diagnosis", padx=10, pady=5, command=lambda: validation_input_diagnosis())

debug_btn = tk.Button(root, text="View Diagnosis", padx=10, pady=5, command=view_diagnosis)

# Text widget for the diagnosis
text = tk.Text(root, height=6, width=50)
text.grid(row=10, column=2, padx=10, pady=10)

#text to view for patient
prescription_text = tk.Text(root, height=6, width=85)
lab_report_text = tk.Text(root, height=18, width=85)
treatment_text = tk.Text(root, height=18, width=85)


#For all the medication
add_medication_btn = tk.Button(root, text="Add Medicine Details", padx=10, pady=5, command=add_medication)
add_medication_diagnosis_btn = tk.Button(root, text="Add Medication to Diagnosis", padx=10, pady=5, command=medication_diagnosis)

medicine_name_label = tk.Label(root, text="Medicine Name: ", font=("Helvetica", 8, "bold"))
medicine_name_entry = ttk.Entry(root)
medicine_details_label = tk.Label(root, text="Details of the medicine: ", font=("Helvetica", 8, "bold"))
medicine_details_entry = ttk.Entry(root)
medicine_type_label = tk.Label(root, text="Type of medicine: ", font=("Helvetica", 8, "bold"))
medicine_type_combobox = ttk.Combobox(root, values=["Liquid", "Tablets", "Capsules", "Topical Medicines", "Suppositories", "Drops", "Inhalers", "Injections", "Patches"], state='readonly', width=15)
medicine_size_label = tk.Label(root, text="Size of medicine: ", font=("Helvetica", 8, "bold"))
medicine_size_entry = ttk.Entry(root)
medicine_infants_label = tk.Label(root, text="Suitable for infants(Ages under 5 years): ", font=("Helvetica", 8, "bold"))
medicine_infants_combobox = ttk.Combobox(root, values=["Yes", "No"], state='readonly', width=15)
medicine_children_label = tk.Label(root, text="Suitable for children(Ages between 5- 13 years): : ", font=("Helvetica", 8, "bold"))
medicine_children_combobox = ttk.Combobox(root, values=["Yes", "No"], state='readonly', width=15)
medicine_cures_label = tk.Label(root, text="Cures: ", font=("Helvetica", 8, "bold"))
medicine_cures_entry = ttk.Entry(root)
medicine_side_effects_label = tk.Label(root, text="Side Effects: ", font=("Helvetica", 8, "bold"))
medicine_side_effects_entry = ttk.Entry(root)
add_medicine_btn = tk.Button(root, text="Add Medicine", padx=10, pady=5, command=lambda: add_medicine_validation())
view_medicine_btn = tk.Button(root, text="View Medicine", padx=10, pady=5, command=lambda: view_medicine())
open_medicine_diagnosis_btn = tk.Button(root, text="Open Diagnosis for this patient", padx=10, pady=5, command=view_date_medication_diagnosis_check_empty)
add_medicine_diagnosis_btn = tk.Button(root, text="Add Medication for Diagnosis", padx=10, pady=5, command=get_medication_diagnosis_check_empty)


#Listbox and other widgets
medicine_combo_box_label = tk.Label(root, text="Please select the medicine ", font=("Helvetica", 8, "bold"))
medicine_combo_box = ttk.Combobox(root, state='readonly', width=15)
listbox = tk.Listbox(root)
medicine_add_btn = tk.Button(root, text="Add Medicine", padx=10, pady=5, command=add_medicine_listbox)
medicine_clear_btn = tk.Button(root, text="Clear All", padx=0, pady=5, command=clear_medicine_listbox)
scrollbar = tk.Scrollbar(listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
medicine_quantity_label = tk.Label(root, text="Quantity of medicine: ", font=("Helvetica", 8, "bold"))
medicine_quantity_entry = ttk.Entry(root)
medicine_usage_label = tk.Label(root, text="Daily Dosage(Dose per day) ", font=("Helvetica", 8, "bold"))
medicine_usage_entry = ttk.Entry(root)
add_medicine_prescription_btn = tk.Button(root, text="Add Prescription For Diagnosis", padx=10, pady=5, command=add_prescription_validation)
view_medicine_prescription_btn = tk.Button(root, text="View Prescription", padx=10, pady=5, command=view_prescription)

view_patient_prescription_btn = tk.Button(root, text="View Prescription At This Date", padx=10, pady=5, command=view_patient_prescription_validation)


#For all Lab Results
add_lab_test_btn = tk.Button(root, text="Add Lab Test", padx=10, pady=5, command=add_lab_test_ui)
add_lab_report_btn = tk.Button(root, text="Add Lab Report", padx=10, pady=5, command=add_lab_report_ui)
lab_test_label = tk.Label(root, text="Enter Name Of Lab Test: ", font=("Helvetica", 8, "bold"))
lab_test_entry = ttk.Entry(root)
lab_test_details_label = tk.Label(root, text="Enter Details Of Lab Test: ", font=("Helvetica", 8, "bold"))
lab_test_details_entry = ttk.Entry(root)
lab_test_listbox_label = tk.Label(root, text="Enter Lab Test Data: ", font=("Helvetica", 8, "bold"))
lab_test_data_entry = ttk.Entry(root)
lab_test_unit_label = tk.Label(root, text="Enter Unit for the Lab Test Data: ", font=("Helvetica", 8, "bold"))
lab_test_unit_entry = ttk.Entry(root)
lab_test_listbox = tk.Listbox(root)
lab_test_add_btn = tk.Button(root, text="Add Lab Test Data", padx=10, pady=5, command=add_lab_test_listbox)
lab_test_clear_btn = tk.Button(root, text="Clear All", padx=0, pady=5, command=clear_lab_test_listbox)
lab_test_scrollbar = tk.Scrollbar(lab_test_listbox)
lab_test_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lab_test_listbox.config(yscrollcommand=lab_test_scrollbar.set)
lab_test_scrollbar.config(command=lab_test_listbox.yview)
lab_test_create_btn = tk.Button(root, text="Create Lab Test", padx=10, pady=5, command=create_lab_test_validation)
lab_test_view_btn = tk.Button(root, text="View Lab Test", padx=10, pady=5, command=view_lab_test_validation)

open_lab_test_diagnosis_btn = tk.Button(root, text="Choose Patient", padx=10, pady=5, command=validate_lab_test_diagnosis_date)
add_lab_test_diagnosis_btn = tk.Button(root, text="Choose Diagnosis Date", padx=10, pady=5, command=validate_lab_test_lab_test_ui)
lab_test_combo_box_label = tk.Label(root, text="Choose Lab Test: ", font=("Helvetica", 8, "bold"))
lab_test_combo_box = ttk.Combobox(root, state='readonly', width=15)
choose_lab_test_btn = tk.Button(root, text="Choose Lab Test", padx=10, pady=5, command=validate_lab_test)
lab_report_listbox = tk.Listbox(root, width=20, height=10)
lab_report_listbox_label = tk.Label(root, text="Enter Data For Lab Report: ", font=("Helvetica", 8, "bold"))
framelabreport = tk.Frame(root, width=800, height=200)
save_lab_report_btn = tk.Button(root, text="Save Lab Report", padx=10, pady=5, command=validate_lab_report)
lab_report_comments_label = tk.Label(root, text="Doctor's Comments On Lab Tests: ", font=("Helvetica", 8, "bold"))
lab_report_comments_entry = ttk.Entry(root)
view_report_btn = tk.Button(root, text="View Lab Report", padx=10, pady=5, command=view_lab_report_database)

#Patients Lab Report
view_patient_lab_report_btn = tk.Button(root, text="View Patient's Lab Report", padx=10, pady=5, command=view_patient_lab_report)

#For treatment
treatment_combo_box_label = tk.Label(root, text="Choose Type of Treatment: ", font=("Helvetica", 8, "bold"))
treatment_combobox = ttk.Combobox(root, values=["Surgery", "Therapy"], state='readonly', width=15)
treatment_name_label = tk.Label(root, text="Enter Treatment Name: ", font=("Helvetica", 8, "bold"))
treatment_name_entry = ttk.Entry(root)
treatment_start_date_label = tk.Label(root, text="Enter Treatment Start Date: ", font=("Helvetica", 8, "bold"))
treatment_start_day_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 32)], state='readonly', width=15)
treatment_start_month_combobox = ttk.Combobox(root, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state='readonly', width=15)
treatment_start_year_combobox = ttk.Combobox(root, values=[str(i) for i in range(1900, date.today().year + 1)], state='readonly', width=15)
treatment_end_date_label = tk.Label(root, text="Enter Treatment End Date: ", font=("Helvetica", 8, "bold"))
treatment_end_day_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 32)], state='readonly', width=15)
treatment_end_month_combobox = ttk.Combobox(root, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state='readonly', width=15)
treatment_end_year_combobox = ttk.Combobox(root, values=[str(i) for i in range(1900, date.today().year + 1)], state='readonly', width=15)
treatment_doctor_label = tk.Label(root, text="Choose Doctor In Charge Of Treatment: ", font=("Helvetica", 8, "bold"))
treatment_doctor_combobox = ttk.Combobox(root, state='readonly', width=15)
save_treatment_btn = tk.Button(root, text="Save Treatment", padx=10, pady=5, command=validate_save_treatment)
view_treatment_btn = tk.Button(root, text="View Treatment", padx=10, pady=5, command=view_treatment)

treatment_combobox_label = tk.Label(root, text="Choose Treatment: ", font=("Helvetica", 8, "bold"))
treatment_patient_combobox = ttk.Combobox(root, state='readonly', width=15)
view_patient_treatment_btn = tk.Button(root, text="View Treatment", padx=10, pady=5, command=view_patient_treatment)

#Admin widgets
#admin for personal details
view_admin_details_btn = tk.Button(root, text="View Admin Details", padx=10, pady=5, command=view_admin_details)
view_doctor_details_btn = tk.Button(root, text="View Doctor Details", padx=10, pady=5, command=admin_view_doctors_details_validation)
view_patient_details_btn = tk.Button(root, text="View Patient Details", padx=10, pady=5, command=admin_view_patients_details_validation)
admin_patients_combo_box = ttk.Combobox(root, state='readonly', width=15)
admin_doctors_combo_box = ttk.Combobox(root, state='readonly', width=15)
btn_save_doctor_details = tk.Button(root, text="Save Data", padx=10, pady=5, command=alter_doctor_details)
btn_save_admin_details = tk.Button(root, text="Save Data", padx=10, pady=5, command=alter_admin_details)
btn_save_patient_details = tk.Button(root, text="Save Data", padx=10, pady=5, command=alter_patient_details)
admin_check_patient_btn = tk.Button(root, text="View Diagnosis Dates", padx=10, pady=5, command=admin_diagnosis_ui)
admin_check_diagnosis_dates_btn = tk.Button(root, text="View Diagnosis For Patient", padx=10, pady=5, command=admin_diagnosis_patient)
btn_save_diagnosis_details = tk.Button(root, text="Save Data", padx=10, pady=5, command=alter_admin_diagnosis_details)
admin_treatment_check_patient_btn = tk.Button(root, text="Choose Patient", padx=10, pady=5, command=admin_treatment_details)
admin_alter_treatment_patient_btn = tk.Button(root, text="Save Data For Treatment", padx=10, pady=5, command=admin_alter_treatment)

admin_medication_label = tk.Label(root, text="Choose Medication: ", font=("Helvetica", 8, "bold"))
admin_medication_combobox = ttk.Combobox(root, state='readonly', width=15)
admin_medication_btn = tk.Button(root, text="Get Medication", padx=10, pady=5, command=alter_admin_medication)
save_admin_medicine_btn = tk.Button(root, text="Save Data", padx=10, pady=5, command=save_alter_admin_medication)

#entry to hide the entries
name_entry.grid_forget()
surname_entry.grid_forget()
email_entry.grid_forget()
dateofbirth_entry.grid_forget()
gender_entry.grid_forget()
contactno_entry.grid_forget()
physicaladdress_entry.grid_forget()
btn.grid_forget()
name_label.grid_forget()
surname_label.grid_forget()
email_label.grid_forget()
dateofbirth_label.grid_forget()
gender_label.grid_forget()
contactno_label.grid_forget()
physicaladdress_label.grid_forget()

# Start the main event loop
root.mainloop()
