from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

filepath = ''

def browsefiles():
    global filepath
    # Create file selection functionality
    filetype = (("comma-separated values","*.csv"),("all files", "*.*"))
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = filetype)
    # Change label contents after file is selected
    label.configure(text="File Opened: "+ filename)
    filepath = filename
def openwindow():
    # Set up window
    window = Tk()  
    window.title('Data Selection')
    window.resizable(False, False)
    window.config(background = "light grey")
    # Create label and button
    global label
    label = Label(window, text = "Select the data to run", anchor="nw", fg = "blue")
    label.grid(column = 1, row = 1)
    browse_button = Button(window, text = "Browse Files", anchor="nw", command = browsefiles)
    browse_button.grid(column = 1, row = 2)
    # Exit button acting as a run button
    exit_button = Button(window, text = "Run", command = window.destroy)
    exit_button.grid(column = 1,row = 3)
    # Run window
    window.mainloop()
    return filepath

