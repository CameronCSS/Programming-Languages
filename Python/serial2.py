import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import difflib
import openpyxl

file_paths = []

def close_match(col_name, column_list):
    best_match = difflib.get_close_matches(col_name, column_list, n=1, cutoff=0.6)
    return best_match[0] if best_match else col_name

def process_data():
    combined_df = pd.DataFrame()  # Combined dataframe to store all data

    target_columns = ['fridge', 'range', 'microwave', 'dishwasher', 'washer', 'dryer']
    
    for file_path in file_paths:
        df = pd.read_excel(file_path)
        df.columns = [col.lower() for col in df.columns] # convert column names to lowercase
        df.columns = [close_match(col, target_columns) for col in df.columns] # match to target columns if close
        
        for col in target_columns:
            if col in df.columns: # make sure this column exists in df
                df[col] = df[col].astype(str).str.upper().str.replace('-', '').str.replace(',', '').str.replace('.', '').str.replace(' ', '').str.replace('AND', 'N').str.replace('IS', '').str.replace('ARE', 'R').str.replace('IF', 'F').str.replace('SEA', 'C').str.replace('FP', 'FB')

        if 'unit' in df.columns: # make sure 'unit' column exists in df
            df['unit'] = df['unit'].astype(int)
        
        combined_df = pd.concat([combined_df, df])  # Append data to combined dataframe

    combined_df = combined_df.sort_values(by='unit', ascending=True)
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

# Set window size, background color and icon
root.geometry("350x250")  # Width x Height
root.configure(background='darkgray')

# Add a frame
frame = tk.Frame(root, bg='darkgray')
frame.place(relx=0.5, rely=0.5, anchor='center')

button_style = ttk.Style()
button_style.configure('TButton', font=('calibri', 11, 'bold'), borderwidth='4')

button_pick = ttk.Button(frame, text="Pick Excel File(s)", command=pick_files)
button_pick.pack(side="left", padx=(0, 20))

button_process = ttk.Button(frame, text="Process and Save", command=process_files)
button_process.pack(side="right")

root.mainloop()
