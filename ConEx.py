from ConEx import ConEx
import os

if __name__ == "__main__":
    items = list()
    main = ConEx()

    main.open_dir(items)
    main.print_items_in_list(items)
    inp = None
    os.chdir("C:\\")
    while inp != 'q':

        inp_l = input(f"'q' = quit | 'g' = grep | 'c' = cat | 'v' = modify | Index number to access subdirectories:\n")
        inp = inp_l.split(" ")
        if inp_l[0] == 'c':
            item = items[int(inp[1])]

            print(item)
            print(os.path.dirname(item))
            print(os.path.abspath(item))
            print(os.listdir(item))
            main.cat_file(os.path.abspath(item))

