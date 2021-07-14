import PySimpleGUI as sg
import os


folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'



theme_dict = {'BACKGROUND': '#000000',
                'TEXT': '#00FF00',
                'INPUT': '#00FF00',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#00FF00',
                'BUTTON': ('#000000', '#00FF00'),
                'PROGRESS': ('#000000', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}


sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')
treedata = sg.TreeData()
BORDER_COLOR = '#000000'
DARK_HEADER_COLOR = '#000000'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))



top_banner = [[sg.Text('Dashboard'+ ' '*64, font='Any 20', background_color=DARK_HEADER_COLOR)]]



block_3 = [
            [sg.Button('Search'), sg.Button('Exit')]  ]


block_2 = [[sg.Text('', font='Any 20')],
            [sg.T('')]]

block_4 = [[sg.Text('Block 4', font='Any 20')],
           [sg.Tree(data=treedata,
                    headings=['Size', ],
                    auto_size_columns=True,
                    num_rows=27,
                    col0_width=58,
                    key='-TREE-',
                    show_expanded=False,
                    enable_events=True),
            ]
           ]
def add_files_in_folder(parent, dirname):
    try:
        files = os.listdir(dirname)
        for f in files:
            fullname = os.path.join(dirname, f)
            if OSError:
                pass
            elif os.path.isdir(fullname):  # if it's a folder, add folder and recurse
                treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
                add_files_in_folder(fullname, fullname)
            else:

                treedata.Insert(parent, fullname, f, values=[
                    os.stat(fullname).st_size], icon=file_icon)
    except ValueError:
        pass


path = "C:\\"
add_files_in_folder('',path)

layout = [[sg.Column(top_banner, size=(960, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
          [sg.Column([[sg.Column(block_3, size=(450,40), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_2, size=(450,560),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
           sg.Column(block_4, size=(600, 620), pad=BPAD_RIGHT)]
          ]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=True)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Search':
        start_path = sg.popup_get_folder("Select Tree Path")
        add_files_in_folder('', start_path)
        print(start_path)


window.close()
