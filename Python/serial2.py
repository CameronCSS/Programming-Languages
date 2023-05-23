## pyinstaller --noconsole serials.py --onefile --hidden-import openpyxl.cell._writer

## pyinstaller --noconsole --noconfirm serials.py --onedir --onefile --windowed --add-data "c:/users/leaf3/appdata/local/programs/python/python310/lib/site-packages/customtkinter;customtkinter/" --hidden-import openpyxl.cell._writer

import customtkinter as ctk
import tkinter as tk
import pandas as pd
import difflib
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from pyhtml2pdf import converter
import os

file_paths = []
target_columns = ['Unit', 'Fridge', 'Range', 'Microwave', 'Dishwasher', 'Washer', 'Dryer']
tab_names = ["Preview", "Details"]
data_loaded_label = None

class CustomDialog(tk.Toplevel):
    def __init__(self, master=None, title=None, message=None):
        super().__init__(master)
        self.title(title)
        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.message_label = ctk.CTkLabel(self.frame, text=message, font=("calibri", 12))
        self.message_label.pack(pady=20)
        self.ok_button = ctk.CTkButton(self.frame, text="OK", command=self.close)
        self.ok_button.pack(pady=20)

    def close(self):
        self.destroy()


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
        output_file = ctk.filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile="Processed Serial Numbers")
        if output_file:
            combined_df.replace({pd.NA: 'N/A', 'NAN': 'N/A'}, inplace=True)
            combined_df.to_excel(output_file, index=False)
            auto_fit_columns(output_file)

            html_file = output_file.replace(".xlsx", ".html")
            combined_df.to_html(html_file, index=False)

            # Add CSS styling
            css = """
            <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }
            </style>
            """
            
            # Read the HTML file
            with open(html_file, 'r') as file:
                html_content = file.read()

            # Insert the CSS styling
            html_content_with_css = css + html_content

            # Write the modified HTML file
            with open(html_file, 'w') as file:
                file.write(html_content_with_css)

            output_pdf_file = ctk.filedialog.asksaveasfilename(defaultextension=".pdf", initialfile="Serials")
            if output_pdf_file:
                converter.convert(html_file, output_pdf_file)
                CustomDialog(app, "Success", "Processing completed successfully!")

                # Close the application and delete the HTML file
                app.destroy()
                os.remove(html_file)
    else:
        CustomDialog(app, "Warning", "No files selected.")


def pick_files():
    global data_loaded_label

    files = ctk.filedialog.askopenfilenames()
    if files:
        file_paths.clear()
        file_paths.extend(files)
        data_loaded_label.configure(text="DATA LOADED. You can now save the files.")
    

def process_files():
    if file_paths:
        save_data()
    else:
        CustomDialog(app, "Warning", "No files selected.")

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

app = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app.geometry("350x250")  # Adjust the window size here
app.title("Serial Number Processing")

frame = ctk.CTkFrame(app)
frame.place(relx=0.5, rely=0.3, anchor='center')

data_loaded_label = ctk.CTkLabel(master=frame, text="")
data_loaded_label.pack(pady=(50, 10))

button_pick = ctk.CTkButton(master=frame, text="Pick Excel File(s)", command=pick_files, font=('calibri', 11, 'bold'))
button_pick.pack(side="left", padx=(0, 20))

button_process = ctk.CTkButton(master=frame, text="Process and Save", command=process_files, font=('calibri', 11, 'bold'))
button_process.pack(side="right")

app.mainloop()
