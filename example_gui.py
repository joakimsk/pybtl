#!/usr/bin/env python

import pyseabird
import PySimpleGUI as sg

def show_table(rows, toprow):
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

def show_editable_window(left_column, right_column):
    layout = [
                [sg.Column(left_column), sg.VSeperator(), sg.Column(right_column)],
                [sg.Submit("Submit"), sg.Cancel("Cancel")]
            ]
    window = sg.Window('Editable window', layout).Finalize()
    event, values = window.read()
    if event == 'Cancel' or event == None:
        print("You pressed cancel")
    elif event == 'Submit':
        print("You pressed submit")
    window.close()

def main():
    toprow = ['Key', 'Value']
    rows = []

    bottlefile = pyseabird.Btl("sta.btl")
    starstar_header = bottlefile.starstar_header

    lcol = []
    rcol = []

    for key, value in starstar_header.items():
        #print(key, "=", value)
        rows.append([key, value])
        lcol.append([sg.Text(key)])
        rcol.append([sg.InputText(value)])

    show_table(rows, toprow)
    show_editable_window(lcol, rcol)


if __name__ == '__main__':
    main()