from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from merger import *


pdf_folder_path = None
pdf_file_names = []


# ----------------------- Response to buttons -------------------------

def selectFile():

    global pdf_folder_path,pdf_file_names

    tmp = []
    while not tmp:

        if pdf_folder_path is not None:
            file_names = filedialog.askopenfilenames(initialdir = pdf_folder_path)

        elif pdf_folder_path is None:
            file_names = filedialog.askopenfilenames()
        
        # update file path
        if len(file_names) > 0:
            dirname = os.path.dirname(file_names[0])

            # if a new folder is selected: 
            if dirname != pdf_folder_path:
                pdf_folder_path = dirname
                pdf_file_names = []
                textbox.delete("1.0", END)


        # extract all pdf files from files_names
        tmp = [os.path.basename(file) for file in file_names if file[-4:].lower() == ".pdf"]
        tmp = [file for file in tmp if file not in pdf_file_names]

        # exit the loop if "cancelled" button was clicked
        if file_names == "":
            break

        # if no pdf file is selected, then try again
        if len(tmp) == 0:
            messagebox.showinfo(title="Open Files Error", message = "No new PDF was found")

    # if at least 1 pdf file was selected, then show all selected pdf
    for new_pdf in tmp:
        textbox.insert(END,f"{new_pdf} \n")
        pdf_file_names.append(new_pdf)


def clearFile():
    global pdf_file_names
    clear = messagebox.askyesno(title="Clear Selected Files", message = "Clear? \nNo or Yes")
    if clear: 
        textbox.delete("1.0",END)
        pdf_file_names = []

def processFile():
    if len(pdf_file_names)>0:
        ok = messagebox.askokcancel(title="Transform PDF", message="Merge? \n No or Yes?")
        if ok: 
            for pdf in pdf_file_names:
                add_blank_page_to_the_right(pdf_folder_path, pdf)
            messagebox.showinfo(title="Transform PDF", message="Completed!")
            clearFile()
        elif not ok:
            messagebox.showinfo(title = "Transform PDF", message="Incompleted.")


def Done():
    window.quit()

def showRules():
    rule_window = Toplevel(window)
    rule_window.title("Instructions")
    rule_txt = Label(rule_window, text="\
        • Select PDF files from ONE folder Only.\n \
        • Pre-selected PDF are cleared whenever a new folder is selected.\n \
        • Select 'Process' after selecting all PDF files to be merged. \n \
        • Select 'Done' to exit the program.")
    rule_txt.pack(side="left")



# ---------------------------- GUI -----------------------------

window = Tk()
window.title("Adding Blank Space to PDF for Note-Taking")
window.config(padx = 10, pady=15)

# add logo to GUI
canvas = Canvas(width = 400,height = 390)
logo = PhotoImage(file = "logo2.png")
scale_factor = max(logo.height()//400, logo.width()//400)
logo = logo.subsample(scale_factor, scale_factor) 
canvas.create_image(200, 185, image=logo)
canvas.grid(row=1,column=1, rowspan=4)


# button task: select files
open_button = Button(text="Select", command = selectFile)
open_button.grid(row=2, column=2)

# scrolled textbox to GUI
textbox = scrolledtext.ScrolledText(width=60)
textbox.grid(row=1, column=2,columnspan=6)

# button task: process pdf
process_button = Button(text="Process", command=processFile)
process_button.grid(row=2,column=3)

# button task: clear the textbox
clear_button = Button(text = "Clear", command=clearFile)
clear_button.grid(row=2, column=4)

# button task: quit program
stop_button = Button(text="Done", command=Done)
stop_button.grid(row = 2, column=5)

# button task: show instructions

rule_button = Button(text="Instructuions", command=showRules)
rule_button.grid(row=2, column=6)

showRules()


# ------------------- run the program --------------------
window.mainloop()