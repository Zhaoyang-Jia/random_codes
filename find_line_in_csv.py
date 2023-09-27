import tkinter as tk
from tkinter import ttk
import pandas as pd

csv_file = '/media/zhaoyang-new/workspace/KarSim/clinical_mapping_files/Prenatal_sample_map.csv'
output_fontsize = 13  # 10 is default size
column_to_search = 1  # e.g. 1 is the second column

# Function to perform the search and display results
def search_csv(event=None):
    # Get the user input substring
    substring = entry.get()

    # Clear the text box
    result_text.delete(1.0, tk.END)

    # Search the DataFrame for rows containing the substring in the second column
    matching_rows = df[df.iloc[:, column_to_search].str.contains(substring, case=False, na=False)]

    # Display matching rows in the text box
    result_text.insert(tk.END, matching_rows.to_string(index=False))

# Function to select all text in the input box
def select_all(event):
    entry.select_range(0, tk.END)
    return "break"  # Prevents the default behavior of Ctrl+A

# Create a Tkinter window
window = tk.Tk()
window.title("CSV Search")

# Create a label and an entry widget for user input
label = ttk.Label(window, text="Enter Substring:")
label.grid(row=0, column=0, padx=10, pady=5)
entry = ttk.Entry(window)
entry.grid(row=0, column=1, padx=10, pady=5)

# Create a button to trigger the search
search_button = ttk.Button(window, text="Search", command=search_csv)
search_button.grid(row=0, column=2, padx=10, pady=5)

# Create a text box to display search results with a larger font
result_text = tk.Text(window, height=10, width=40)
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
result_text.config(font=("TkDefaultFont", int(result_text.cget("height")) * output_fontsize // 10))

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Bind the Enter key to trigger the search
entry.bind('<Return>', search_csv)
# Bind the Ctrl+A event to select all text in the entry box
entry.bind('<Control-a>', select_all)

# Allow the text widget to expand with window resizing
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the GUI application
window.mainloop()
