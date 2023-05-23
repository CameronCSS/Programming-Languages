## pyinstaller --noconsole serials.py --onefile --hidden-import openpyxl.cell._writer

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import difflib
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

file_paths = []
target_columns = ['Unit', 'Fridge', 'Range', 'Microwave', 'Dishwasher', 'Washer', 'Dryer']

def close_match(col_name, column_list):
    best_match = difflib.get_close_matches(col_name, column_list, n=1, cutoff=0.6)
    return best_match[0] if best_match else col_name

def process_data():
    combined_df = pd.DataFrame()

    for file_path in file_paths:
        df = pd.read_excel(file_path)
        df.columns = [col.lower() for col in df.columns]
        df.columns = [close_match(col, target_columns) for col in df.columns]

        for col in target_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.upper().str.replace('-', '').str.replace(',', '').str.replace('.', '').str.replace(' ', '').str.replace('AND', 'N').str.replace('IS', '').str.replace('ARE', 'R').str.replace('IF', 'F').str.replace('SEA', 'C').str.replace('FP', 'FB').str.replace('#', '').str.replace(':', '')

        combined_df = pd.concat([combined_df, df])

    combined_df = combined_df.sort_values(by='Unit', ascending=True)
    combined_df = combined_df.reset_index(drop=True)

    return combined_df

def save_data():
    combined_df = process_data()

    if not combined_df.empty:
        combined_df.drop_duplicates(inplace=True)
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile="Processed Serial Numbers")
        if output_file:
            combined_df.replace({pd.NA: 'N/A', 'NAN': 'N/A'}, inplace=True)
            combined_df.to_excel(output_file, index=False)
            auto_fit_columns(output_file)
            messagebox.showinfo("Success", "Processing completed successfully!")
    else:
        messagebox.showwarning("Warning", "No files selected.")

def preview_data(): 
    combined_df = process_data()

    for i in preview_tree.get_children():
        preview_tree.delete(i)

    if not combined_df.empty:
        combined_df = combined_df[['Unit', 'Fridge', 'Range', 'Microwave', 'Dishwasher', 'Washer', 'Dryer']]

        preview_tree["columns"] = combined_df.columns.tolist()

        for column in combined_df.columns:
            if column.lower() == 'unit':
                preview_tree.heading(column, text='Unit')
            else:
                preview_tree.heading(column, text=column)

        for index, row in combined_df.iterrows():
            preview_tree.insert('', 'end', values=list(row))

        preview_tree.grid(row=1, column=0)
        label_preview.grid()

def pick_files(): 
    files = filedialog.askopenfilenames() 
    if files: 
        file_paths.clear()
        file_paths.extend(files) 
        preview_data()

def process_files(): 
    if file_paths: 
        save_data() 
    else: 
        messagebox.showwarning("Warning", "No files selected.") 

def auto_fit_columns(file_path):
    wb = load_workbook(file_path)
    ws = wb.active
    for column in ws.columns:
        max_length = 0
        column = [cell for cell in column]
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        col_letter = get_column_letter(column[0].column)
        ws.column_dimensions[col_letter].width = adjusted_width
    wb.save(file_path)
    wb.close()

root = tk.Tk()
root.title("Serial Number Processing")

root.geometry("1500x800")
root.configure(background='darkgray')

frame = tk.Frame(root, bg='darkgray')
frame.place(relx=0.5, rely=0.3, anchor='center')

button_style = ttk.Style()
button_style.configure('TButton', font=('calibri', 11, 'bold'), borderwidth='4')

button_pick = ttk.Button(frame, text="Pick Excel File(s)", command=pick_files)
button_pick.pack(side="left", padx=(0, 20))

button_process = ttk.Button(frame, text="Process and Save", command=process_files)
button_process.pack(side="right")

preview_frame = tk.Frame(root, bg='darkgray')
preview_frame.place(relx=0.5, rely=0.6, anchor='center')

label_preview = ttk.Label(preview_frame, text="Preview:", font=("Arial", 18))
label_preview.grid(row=0, column=0, pady=(20, 0))
label_preview.grid_remove()

preview_tree = ttk.Treeview(preview_frame, columns=target_columns + ['Unit'], show='headings', height=10)

for column in target_columns + ['Unit']:
    preview_tree.heading(column, text=column)

preview_tree.grid(row=1, column=0)
preview_tree.grid_remove()

root.mainloop()
