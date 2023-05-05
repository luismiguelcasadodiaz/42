import PySimpleGUI as sg
from qrgenerator import generate_qr
from shared_secret_key import generate_secret_key, beautiful_key
from PIL import Image, ImageTk
import time

QR_SIZE = (300, 300)
BASE32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567= abcdefghijklmnopqrstuvwxyz"
BASE32_CHARSET = "234567=abcdefghijklmnopqrstuvwxyz"

def cb_func_use_my_key():
    layout = [
        [sg.Text('Introduzca la clave base 32 (8 grupos de 4 letras):')],
        [sg.Text('Formato :aaaa bbbb cccc dddd eeee ffff gggg hhhh')],
        [sg.Text(f'Solamente {BASE32_CHARSET}')],
        [sg.Text("Use '=' como separador de cada grupo en blanco")],
        [sg.Input("", enable_events=True,  key='-INPUT-')],
        [sg.Text("0", key='-CONTADOR-')],
        [sg.Button('Ok', key='-OK-'), sg.Button('Exit')]]

    my_window = sg.Window('TOTP con una clave conocida previamente', layout)

    while True:             # Event Loop
        event, values = my_window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # if last char entered not a digit
        if event == '-INPUT-' and len(values['-INPUT-']) and values['-INPUT-'][-1] not in BASE32_CHARSET:
            # delete last char from input
            my_window['-INPUT-'].update(values['-INPUT-'][:-1])
        input_size = len(values['-INPUT-'])
        if event == '-INPUT-' and input_size < 40:
            my_window['-CONTADOR-'].update(input_size)
            

        if event == '-INPUT-' and input_size ==40:
           resultado = values['-INPUT-'][:-1]
           resultado_b="".join(resultado.split("=")).encode('utf8')
           break

    my_window.close()
    window["-CLAVE-"].update(resultado_b)


def cb_func_update_key(clave_bytes=None):
    if clave_bytes is None:
        #clave_bytes = generate_secret_key()
        clave_bytes = 'MNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQ===='
    window["-CLAVE-"].update(clave_bytes)
    user = values["-USER-"]
    mail = values["-MAIL-"]
    imagepath = generate_qr(clave_bytes, user, mail)
    im = Image.open(imagepath)

    im = im.resize(QR_SIZE, resample=Image.BICUBIC)
    if im is not None:
        image = ImageTk.PhotoImage(image=im)
        window["-QRCODE-"].update(data=image)


TOTP_layout_Left = [
    [sg.Text("User name")],
    [sg.In(size=(45, 1), enable_events=True, key="-USER-",font='Courier')],
    [sg.Text("User mail")],
    [sg.In(size=(45, 1), enable_events=True, key="-MAIL-",font='Courier')],
    [sg.HSeparator()],
   # [sg.Text("Usa una clave secreta conocida")],
   # [sg.In(size=(25, 1), enable_events=True, key="-CLAVE-")],
    [sg.Button("Create key", key="-CREATE-")],
    [sg.Text("Clave secreta generada")],
    [sg.In(size=(45, 1), enable_events=True, key="-CLAVE-", font='Courier')],
    
    [sg.Button("Uso mi clave", key="-USE-")],
    [sg.Text("Clave secreta generada", key="-SECONDS-")],
]
TOTP_layout_Right = [
    [sg.Text("QR CODE")],
    [sg.Image(size=QR_SIZE,key="-QRCODE-")],

]
TOTP_layout = [
    [
        sg.Column(TOTP_layout_Left),
        sg.VSeparator(),
        sg.Column(TOTP_layout_Right)
    ]
]
window = sg.Window(title="Time-based One time Paswword generator - (TOTP)", layout=TOTP_layout , margins=(15, 15))
start_time = time.time()
my_time = start_time
while True:
    actual_time = time.time()
    elapsed_time = actual_time - my_time  #  time diff between loops
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-CREATE-":
        window['-USE-'].update(disabled = True)
        cb_func_update_key()
    elif event == "-USE-":
        window['-CREATE-'].update(disabled = True)
        cb_func_use_my_key()
    elif event == "-CLAVE-":
        cb_func_update_key(values["-CLAVE-"])
        

    
