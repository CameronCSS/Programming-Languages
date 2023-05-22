import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

file_paths = []

def process_data():
    combined_df = pd.DataFrame()  # Combined dataframe to store all data
    
    for file_path in file_paths:
        df = pd.read_excel(file_path)

        columns = ['Fridge', 'Range', 'Microwave', 'Dishwasher ', 'Washer', 'Dryer']
        for col in columns:
            df[col] = df[col].astype(str).str.upper()

        for col in columns:
            df[col] = df[col].str.replace('-', '').str.replace(',', '').str.replace('.', '').str.replace(' ', '').str.replace('AND', 'N').str.replace('IS', '').str.replace('ARE', 'R').str.replace('IF', 'F').str.replace('SEA', 'C').str.replace('FP', 'FB')

        df['Unit'] = df['Unit'].astype(int)
        
        combined_df = combined_df.append(df)  # Append data to combined dataframe

    combined_df = combined_df.sort_values(by='Unit', ascending=True)
    combined_df = combined_df.reset_index(drop=True)
    
    if not combined_df.empty:
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile="Processed Serial Numbers")
        if output_file:
            combined_df.to_excel(output_file, index=False)
            messagebox.showinfo("Success", "Processing completed successfully!")
    else:
        messagebox.showwarning("Warning", "No files selected.")

def pick_files():
    files = filedialog.askopenfilenames()
    if files:
        file_paths.clear()  # Clear the existing file paths
        file_paths.extend(files)

def process_files():
    if file_paths:
        process_data()
    else:
        messagebox.showwarning("Warning", "No files selected.")


root = tk.Tk()
root.title("Serial Number Processing")

button_pick = tk.Button(root, text="Pick Excel File(s)", command=pick_files)
button_pick.pack(pady=20)

button_process = tk.Button(root, text="Process and Save", command=process_files)
button_process.pack(pady=10)

root.mainloop()
