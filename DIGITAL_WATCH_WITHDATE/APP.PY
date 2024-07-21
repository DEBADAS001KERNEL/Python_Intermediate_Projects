import tkinter as tk
import time

# Initialize the main window
root = tk.Tk()
root.title("Digital Watch with Date")
root.geometry("300x150")
root.resizable(False, False)

def update_time_date():
    # Get the current time and date
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %B %d, %Y")
    
    # Update the time and date labels
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # Call this function again after 1000ms (1 second)
    root.after(1000, update_time_date)

# Create labels for the time and date
time_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
time_label.pack(pady=10)

date_label = tk.Label(root, font=("Helvetica", 18))
date_label.pack(pady=10)

# Call the update function to initialize the time and date display
update_time_date()

# Start the main event loop
root.mainloop()





