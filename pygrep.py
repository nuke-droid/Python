# Python program to create
# a file explorer in Tkinter
import os
# import all components
# from the tkinter library
from tkinter import * 
  
# import filedialog module
from tkinter import filedialog
from tkinter import Listbox
from tkinter import commondialog
from tkinter import Text
from tkinter import ttk
  
# Function for opening the
# file explorer window

# Create the root window
window = Tk()
window.resizable(True, True)



search_entry = Text(window,
                        background= "black",
                        fg= "#00ff00",
                        height= 1,
                        width= 40)

lb = Listbox(window,
                height= 38,
                width= 100,
                background= "black",
                fg= "#00ff00"
                )

cb = ttk.Combobox(window,
                    height= 1,
                    width= 40,
                    background= "black",
                    foreground= "#00ff00",
                    )

def get_child_items():

    lb.delete(1, END)
    path = cb.get()
    print(path)
    dirs = os.listdir(path)
    for folder in dirs:
        print(folder)
        lb.insert(END, folder)

def callback(event):
    i = event.widget.curselection()[0]
    text = event.widget.get(i)
    text = cb.get() + text + "\\"
    cb.set(text)
def browseFiles():
    '''
    if search_entry.get("1.0",'end-1c') != None:
        filename = filedialog.Directory(search_entry.get("1.0",'end-1c'))
    '''
    
    filename = filedialog.askdirectory(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("Text files",
                                                        "*.txt*"),
                                                    ("all files",
                                                        "*.*")))
      
    # Change label contents
    
      
      
                                                                                                  

lb.bind("<<ListboxSelect>>", callback)
# Set window title
window.title('PyEx')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "black")



button_explore = Button(window,
                        text = "Navigate",
                        command = get_child_items,
                        background= "black",
                        fg= "#00ff00",
                        height= 1,
                        width= 8)
  


  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns

  
button_explore.grid(column = 0, row = 1)
button_explore.anchor("nw")
cb.grid(column= 1, row= 1)

lb.grid(column= 1, row= 3)
  
  
# Let the window wait for any events
window.mainloop()