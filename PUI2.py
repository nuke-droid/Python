import PySimpleGUI as sg
import os

# Turn off padding in order to get a really tight looking layout.
folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))
TREEDATA = sg.TreeData()


def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def add_files_in_folder(parent, dirname):

    os.chdir(dirname)
    pwd = os.getcwd()
    files = os.listdir(pwd)
    for f in files:
        fullname = os.path.join(dirname, f)

        if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
            try:
                TREEDATA.Insert(parent, fullname, f,
                                values=[], icon=folder_icon)
                add_files_in_folder(fullname, fullname)
            except OSError:
                "#dfsdfs"

        else:
            try:
                TREEDATA.Insert(parent, fullname, f, values=[
                                os.stat(fullname).st_size], icon=file_icon)
            except OSError:
                "#sjndfjns"


root = sg.popup_get_folder("Select Parent Folder")
add_files_in_folder('', root)

layout = [[sg.Tree(data=TREEDATA,
                   headings=['Size', ],
                   auto_size_columns=True,
                   num_rows=20,
                   col0_width=40,
                   key='-TREE-',
                   show_expanded=False,
                   enable_events=True),
           ],
          [sg.Button('Start', button_color=('white', 'black'), enable_events=True, ),
           sg.Button('Stop', button_color=('gray50', 'black')),
           sg.Button('Reset', button_color=('white', '#9B0023')),
           sg.Button('Submit', button_color=('gray60', 'springgreen4')),
           sg.Button('Exit', button_color=('white', '#00406B'))],

          ]

window = sg.Window("Borderless Window",
                   layout,
                   default_element_size=(50, 20),
                   text_justification='r',
                   auto_size_text=False,
                   auto_size_buttons=False,
                   no_titlebar=True,
                   grab_anywhere=True,
                   default_button_element_size=(12, 1))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
