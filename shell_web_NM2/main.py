import eel
import ctypes
import sys

width = sys.argv[1]
height = sys.argv[2]
port_data = sys.argv[3]
name_ = sys.argv[4]

find_free_port_dll = ctypes.CDLL('./FindFreePort.dll')
find_free_port_dll.FindFreePort.restype = ctypes.c_int

@eel.expose
def quit():
    sys.exit()

@eel.expose
def port():
    return port_data

@eel.expose
def icon_data():
    with open('icon.data', 'r') as file:
        base64_data = file.read()
    return base64_data

@eel.expose
def name():
    return name_

eel.init('web')

eel.start('index.html', size=(width, height), port=find_free_port_dll.FindFreePort())