#!/usr/bin/env python

"""gui.py: a python script for creating a multi-platform GUI for imgcomparetool."""

import os, sys
import PySimpleGUI as sg
from imgcomparetool import ImageList

def main():
    # GUI Parameters
    sg.SetOptions(button_color=sg.COLOR_SYSTEM_DEFAULT)
    text_size = (25, 1)
    layout = [  [sg.Text('Enter the following details to compare your list of images.')],
                [sg.Text('Select the input CSV file', size=text_size), sg.InputText(), sg.FileBrowse()],
                [sg.Text('Enter the output file name', size=text_size), sg.InputText('image_comparson_result.csv')],
                [sg.Text('Select output CSV folder', size=text_size), sg.InputText(), sg.FolderBrowse()],
                [sg.Submit(tooltip='Click to submit this window'), sg.Text('', size=(18, 1)), sg.Button('Close')] ]

    # GUI Window creation and results interpretation
    window = sg.Window('ImgCompareTool Similarity Tool', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Close'):
            break
        elif event == 'Submit':
            try:
                image_list = ImageList(values[0])
                image_list.compare(os.path.join(values[2], values[1]))
                sg.Popup('Comparison successfully completed!', title='Success')
            except Exception as e:
                sg.Popup(e, title='Exception')

    # Closing the GUI
    window.close()

if __name__ == '__main__':
    main()