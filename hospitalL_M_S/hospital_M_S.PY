import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database connection function
def connect_db():
    return sqlite3.connect('hospital.db')

# Function to create tables if they do not exist
def create_tables():
    conn = connect_db()
    c = conn.cursor()

    # Create Patients table
    c.execute('''CREATE TABLE IF NOT EXISTS Patients (
                 PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Name TEXT NOT NULL,
                 Age INTEGER,
                 Gender TEXT,
                 Address TEXT,
                 Phone TEXT)''')

    # Create Doctors table
    c.execute('''CREATE TABLE IF NOT EXISTS Doctors (
                 DoctorID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Name TEXT NOT NULL,
                 Specialization TEXT,
                 Phone TEXT)''')

    # Create Appointments table
    c.execute('''CREATE TABLE IF NOT EXISTS Appointments (
                 AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                 PatientID INTEGER,
                 DoctorID INTEGER,
                 Date TEXT,
                 Time TEXT,
                 FOREIGN KEY(PatientID) REFERENCES Patients(PatientID),
                 FOREIGN KEY(DoctorID) REFERENCES Doctors(DoctorID))''')

    # Create Billing table
    c.execute('''CREATE TABLE IF NOT EXISTS Billing (
                 BillID INTEGER PRIMARY KEY AUTOINCREMENT,
                 PatientID INTEGER,
                 Amount REAL,
                 Date TEXT,
                 FOREIGN KEY(PatientID) REFERENCES Patients(PatientID))''')

    conn.commit()
    conn.close()

# Main Application Class
class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("600x400")
        
        # Create the necessary tables
        create_tables()
        
        # Main Menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        patient_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Patients", menu=patient_menu)
        patient_menu.add_command(label="Add Patient", command=self.add_patient)
        patient_menu.add_command(label="View Patients", command=self.view_patients)
        
        doctor_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Doctors", menu=doctor_menu)
        doctor_menu.add_command(label="Add Doctor", command=self.add_doctor)
        doctor_menu.add_command(label="View Doctors", command=self.view_doctors)
        
        appointment_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Appointments", menu=appointment_menu)
        appointment_menu.add_command(label="Add Appointment", command=self.add_appointment)
        appointment_menu.add_command(label="View Appointments", command=self.view_appointments)
        
        billing_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Billing", menu=billing_menu)
        billing_menu.add_command(label="Generate Bill", command=self.generate_bill)
        billing_menu.add_command(label="View Bills", command=self.view_bills)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def add_patient(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Add Patient", font=('Arial', 20)).pack(pady=20)
        tk.Label(self.main_frame, text="Name").pack()
        name_entry = tk.Entry(self.main_frame)
        name_entry.pack()
        
        tk.Label(self.main_frame, text="Age").pack()
        age_entry = tk.Entry(self.main_frame)
        age_entry.pack()
        
        tk.Label(self.main_frame, text="Gender").pack()
        gender_entry = tk.Entry(self.main_frame)
        gender_entry.pack()
        
        tk.Label(self.main_frame, text="Address").pack()
        address_entry = tk.Entry(self.main_frame)
        address_entry.pack()
        
        tk.Label(self.main_frame, text="Phone").pack()
        phone_entry = tk.Entry(self.main_frame)
        phone_entry.pack()
        
        def save_patient():
            name = name_entry.get()
            age = age_entry.get()
            gender = gender_entry.get()
            address = address_entry.get()
            phone = phone_entry.get()
            
            conn = connect_db()
            c = conn.cursor()
            c.execute("INSERT INTO Patients (Name, Age, Gender, Address, Phone) VALUES (?, ?, ?, ?, ?)",
                      (name, age, gender, address, phone))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Patient added successfully")
            self.clear_frame()
        
        tk.Button(self.main_frame, text="Save", command=save_patient).pack(pady=20)
    
    def view_patients(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Patients", font=('Arial', 20)).pack(pady=20)
        
        columns = ("ID", "Name", "Age", "Gender", "Address", "Phone")
        tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.pack(fill=tk.BOTH, expand=True)
        
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM Patients")
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()
    
    def add_doctor(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Add Doctor", font=('Arial', 20)).pack(pady=20)
        tk.Label(self.main_frame, text="Name").pack()
        name_entry = tk.Entry(self.main_frame)
        name_entry.pack()
        
        tk.Label(self.main_frame, text="Specialization").pack()
        specialization_entry = tk.Entry(self.main_frame)
        specialization_entry.pack()
        
        tk.Label(self.main_frame, text="Phone").pack()
        phone_entry = tk.Entry(self.main_frame)
        phone_entry.pack()
        
        def save_doctor():
            name = name_entry.get()
            specialization = specialization_entry.get()
            phone = phone_entry.get()
            
            conn = connect_db()
            c = conn.cursor()
            c.execute("INSERT INTO Doctors (Name, Specialization, Phone) VALUES (?, ?, ?)",
                      (name, specialization, phone))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Doctor added successfully")
            self.clear_frame()
        
        tk.Button(self.main_frame, text="Save", command=save_doctor).pack(pady=20)
    
    def view_doctors(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Doctors", font=('Arial', 20)).pack(pady=20)
        
        columns = ("ID", "Name", "Specialization", "Phone")
        tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.pack(fill=tk.BOTH, expand=True)
        
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM Doctors")
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()
    
    def add_appointment(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Add Appointment", font=('Arial', 20)).pack(pady=20)
        tk.Label(self.main_frame, text="Patient ID").pack()
        patient_id_entry = tk.Entry(self.main_frame)
        patient_id_entry.pack()
        
        tk.Label(self.main_frame, text="Doctor ID").pack()
        doctor_id_entry = tk.Entry(self.main_frame)
        doctor_id_entry.pack()
        
        tk.Label(self.main_frame, text="Date").pack()
        date_entry = tk.Entry(self.main_frame)
        date_entry.pack()
        
        tk.Label(self.main_frame, text="Time").pack()
        time_entry = tk.Entry(self.main_frame)
        time_entry.pack()
        
        def save_appointment():
            patient_id = patient_id_entry.get()
            doctor_id = doctor_id_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            
            conn = connect_db()
            c = conn.cursor()
            c.execute("INSERT INTO Appointments (PatientID, DoctorID, Date, Time) VALUES (?, ?, ?, ?)",
                      (patient_id, doctor_id, date, time))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Appointment added successfully")
            self.clear_frame()
        
        tk.Button(self.main_frame, text="Save", command=save_appointment).pack(pady=20)
    
    def view_appointments(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Appointments", font=('Arial', 20)).pack(pady=20)
        
        columns = ("ID", "Patient ID", "Doctor ID", "Date", "Time")
        tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.pack(fill=tk.BOTH, expand=True)
        
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM Appointments")
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()
    
    def generate_bill(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Generate Bill", font=('Arial', 20)).pack(pady=20)
        tk.Label(self.main_frame, text="Patient ID").pack()
        patient_id_entry = tk.Entry(self.main_frame)
        patient_id_entry.pack()
        
        tk.Label(self.main_frame, text="Amount").pack()
        amount_entry = tk.Entry(self.main_frame)
        amount_entry.pack()
        
        tk.Label(self.main_frame, text="Date").pack()
        date_entry = tk.Entry(self.main_frame)
        date_entry.pack()
        
        def save_bill():
            patient_id = patient_id_entry.get()
            amount = amount_entry.get()
            date = date_entry.get()
            
            conn = connect_db()
            c = conn.cursor()
            c.execute("INSERT INTO Billing (PatientID, Amount, Date) VALUES (?, ?, ?)",
                      (patient_id, amount, date))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Bill generated successfully")
            self.clear_frame()
        
        tk.Button(self.main_frame, text="Save", command=save_bill).pack(pady=20)
    
    def view_bills(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Bills", font=('Arial', 20)).pack(pady=20)
        
        columns = ("ID", "Patient ID", "Amount", "Date")
        tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.pack(fill=tk.BOTH, expand=True)
        
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM Billing")
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
