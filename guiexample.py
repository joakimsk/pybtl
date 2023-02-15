#!/usr/bin/env python

import pybtl
import PySimpleGUI as sg

bottlefile = pybtl.Btl("sta0078.btl")

def make_table(rows, toprow):
    tbl1 = sg.Table(values=rows, headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)
    layout = [[tbl1]]
    window = sg.Window("Table Demo", layout, size=(715, 200), resizable=True)

    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        #if '+CLICKED+' in event:
            #sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
    window.close()


toprow = ['Key', 'Value']
rows = []

left_column = []
right_column = []

starstar_dict = bottlefile.return_starstar_dict()
for key in starstar_dict:
    print(key, "=", starstar_dict[key])
    rows.append([key, starstar_dict[key]])
    left_column.append([sg.Text(key)])
    right_column.append([sg.InputText(starstar_dict[key])])



layout = [
[sg.Column(left_column), sg.VSeperator(), sg.Column(right_column)],
[sg.Submit("Read values from eventlogger"), sg.Submit("Continue processing using these values")]
]

#make_table(rows, toprow)

window = sg.Window('Test', layout).Finalize()
event, values = window.read()
window.close()