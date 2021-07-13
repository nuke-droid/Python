# Python program to create
# a file explorer in Tkinter
import os, webbrowser
# import all components
# from the tkinter library
from tkinter import *
# import custom module
from PyEx import PyEx
# import filedialog module
from tkinter import filedialog
from tkinter import Listbox
from tkinter import commondialog
from tkinter import Text
from tkinter import ttk

# Function for opening the
# file explorer window


class UI:



    # Create the root window
    window = Tk()
    
    window.resizable(True, True)


    search_entry = Text(window,
                        background="black",
                        fg="#00ff00",
                        height=1,
                        width=40)

    lb = Listbox(window,
                height=38,
                width=100,
                background="black",
                fg="#00ff00"
                )

    cb = ttk.Combobox(window,
                    height=1,
                    width=40,
                    background="black",
                    foreground="#00ff00",
                    )


   
    PE = PyEx()
    

    def _callback(self, event):
        i = event.widget.curselection()[0]
        text = event.widget.get(i)
        fileext = "."
        
        if text.find(fileext) != -1:
            text = self.cb.get() + text
        else:
            text = self.cb.get() + text + "\\"
        self.cb.set(text)



    lb.bind("<<ListboxSelect>>", _callback)
    # Set window title
    window.title('PyEx')

    # Set window size
    window.geometry("1000x500")

    # Set window background color
    window.config(background="black")


    button_explore = Button(window,
                            text="Navigate",
                            command= PE.get_child_items(lb, cb),
                            background="black",
                            fg="#00ff00",
                            height=1,
                            width=8)



    button_explore.grid(column=0, row=1)
    button_explore.anchor("nw")
    cb.grid(column=1, row=1)

    lb.grid(column=1, row=3)


    # Let the window wait for any events
    window.mainloop()
