import sys
import os


class ConEx:

    @staticmethod
    def cat_file(file):
        with open(file, 'r') as f:
            contents = f.read()
        print(contents)

    @staticmethod
    def open_dir(items):

        root = "C:\\"

        for item in os.listdir(root):
            if os.path.isfile(os.path.join(root, item)):
                items.append(item)
            if os.path.isdir(os.path.join(root, item)):
                items.append(item)

    @staticmethod
    def print_items_in_list(items):
        for i in items:
            if os.path.isdir(i):
                meta = os.stat(i)
                print(items.index(i), "|", i, meta.st_size, meta.st_birthtime, meta.st_ctime)
            elif os.path.isfile(i):
                meta = os.stat(i)
                print(items.index(i), "|", i, meta.st_size, meta.st_birthtime, meta.st_ctime)
            else:
                print(items.index(i), "|", i)

