import PySimpleGUI as sg

form_rows = [[sg.Text('Enter 2 files to comare')],
                 [sg.Text('File 1', size=(15, 1)), sg.InputText(key='file1'), sg.FileBrowse()],
                 [sg.Text('File 2', size=(15, 1)), sg.InputText(key='file2'), sg.FileBrowse(target='file2')],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('File Compare')
event, values = window.Layout(form_rows).Read()

print("Event =", event)
print("Values = ", values)