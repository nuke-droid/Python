import os, webbrowser
from tkinter.constants import END
from tkinter import *



class PyEx:

   

    def get_child_items(self, l, c):

        l.delete(1, END)
        path = c.get()
        print(path)
        if os.path.isdir(path):
            dirs = os.listdir(path)
            for folder in dirs:
                print(folder)
                l.insert(END, folder)

        if os.path.isfile(path):
            webbrowser.open(path)
