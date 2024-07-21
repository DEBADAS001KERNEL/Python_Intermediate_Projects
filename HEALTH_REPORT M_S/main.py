import sqlite3

# Function to create database tables
def create_tables():
    conn = sqlite3.connect('health_management.db')
    c = conn.cursor()
    
    # Create patients table
    c.execute('''CREATE TABLE IF NOT EXISTS patients (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 weight REAL,
                 height REAL,
                 blood_pressure TEXT,
                 cholesterol REAL,
                 blood_sugar REAL)''')
    
    conn.commit()
    conn.close()

# Function to add a new patient
def add_patient(name, weight, height, blood_pressure, cholesterol, blood_sugar):
    conn = sqlite3.connect('health_management.db')
    c = conn.cursor()
    c.execute('''INSERT INTO patients (name, weight, height, blood_pressure, cholesterol, blood_sugar) 
                 VALUES (?, ?, ?, ?, ?, ?)''', 
                 (name, weight, height, blood_pressure, cholesterol, blood_sugar))
    conn.commit()
    conn.close()

# Function to evaluate the health of a patient
def evaluate_health(patient_id):
    conn = sqlite3.connect('health_management.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM patients WHERE id = ?''', (patient_id,))
    patient_info = c.fetchone()
    conn.close()
    
    if patient_info:
        name, weight, height, blood_pressure, cholesterol, blood_sugar = patient_info[1:]
        bmi = weight / (height/100)**2
        is_healthy = True
        
        # Simple health criteria for evaluation
        if bmi < 18.5 or bmi > 24.9:
            is_healthy = False
        if blood_pressure != '120/80':
            is_healthy = False
        if cholesterol > 200:
            is_healthy = False
        if blood_sugar > 100:
            is_healthy = False
        
        print(f"\nPatient: {name}")
        print(f"BMI: {bmi:.2f}")
        print(f"Blood Pressure: {blood_pressure}")
        print(f"Cholesterol: {cholesterol}")
        print(f"Blood Sugar: {blood_sugar}")
        print("Health Status:", "Healthy" if is_healthy else "Unhealthy")
    else:
        print("Patient not found!")

# Command-line interface for the health management system
def main():
    create_tables()
    
    while True:
        print("\nHealth Management System")
        print("1. Add Patient")
        print("2. Evaluate Health")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient name: ")
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (cm): "))
            blood_pressure = input("Enter blood pressure (e.g., 120/80): ")
            cholesterol = float(input("Enter cholesterol level (mg/dL): "))
            blood_sugar = float(input("Enter blood sugar level (mg/dL): "))
            add_patient(name, weight, height, blood_pressure, cholesterol, blood_sugar)
            print("Patient added successfully!")
        
        elif choice == '2':
            patient_id = int(input("Enter patient ID: "))
            evaluate_health(patient_id)
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
