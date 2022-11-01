from os import listdir, getcwd 
from os.path import isfile, join
import pandas as pd
from tkinter import *
from tkinter import messagebox

# ---------------------------- FILE NAME READER ------------------------------- #
def clear_all_fields():
    # Clear all fields for next use
    input_entry.delete(0,'end')
    output_entry.delete(0,'end')
    csv_name_entry.delete(0, "end")
    input_entry.focus()

def generate_csv():
    if len(input_entry.get()) == 0:
        # If no input path is given, show an error message.
        messagebox.showerror("Error. No file path entered.", "You haven't selected a file path to read. \nPlease enter a file path and try again.")
    else:
        # Get file path from input entry field
        file_path = input_entry.get()
        
        # Generate a list from the list of filenames in the directory 
        file_list = [f for f in listdir(file_path) if isfile(join(file_path, f))]
        
        # Create pandas DataFrame from list of filenames
        df = pd.DataFrame(file_list, columns=["File name"])
        
        if len(output_entry.get()) == 0:
            # Warn user that no output directory was given and declare where the file will go 
            is_ok = messagebox.askokcancel(title="Warning. No output directory specified.", message=f"You have not chosen an output directory.\n\nCSV will be sent to the following location: {getcwd()}")
            
            if is_ok:
                # Change output path to current directory
                output_path = getcwd()
                
                # Export dataframe as csv to output path
                df.to_csv(f'{output_path}/{csv_name_entry.get()}', index=False)
                
                # Clear all fields for next use
                clear_all_fields()  
        else:   
            # Get output path from output directory field 
            output_path = output_entry.get()
            
            # Export dataframe as csv to output path
            df.to_csv(f'{output_path}/{csv_name_entry.get()}', index=False)

            # Clear all fields for next use
            clear_all_fields()

        # Hardcoded file path
        # file_list = [f for f in listdir("L:\Cellular_Pathology\TalkingPoint Server\Outsourcing\Import Completed") if isfile(join("L:\Cellular_Pathology\TalkingPoint Server\Outsourcing\Import Completed", f))]

# ---------------------------- UI SETUP ------------------------------- #
FONT = "Arial", 14

window = Tk()
window.title("File Name Reader")
window.config(width=650, height=500, padx=40, pady=40)

input_label = Label(text="Enter directory to read: ", font=FONT)
input_label.grid(column=0, row=1)

output_label = Label(text="Enter output directory: ", font=FONT)
output_label.grid(column=0, row=3)

csv_name_label = Label(text="Enter desired CSV filename: (Please include .csv suffix)", font=FONT)
csv_name_label.grid(column=0, row=5)

input_entry = Entry(width=37, font=FONT)
input_entry.grid(column=0, row=2)
input_entry.focus()

output_entry = Entry(width=37, font=FONT)
output_entry.grid(column=0, row=4)

csv_name_entry = Entry(width=37, font=FONT)
csv_name_entry.grid(column=0, row=6)

generate_csv_btn = Button(text="Generate CSV", font=FONT, command=generate_csv)
generate_csv_btn.grid(column=0, row=7)



window.mainloop()