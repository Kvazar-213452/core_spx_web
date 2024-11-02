import eel
import ctypes
import sys

width = sys.argv[1]
height = sys.argv[2]

find_free_port_dll = ctypes.CDLL('./FindFreePort.dll')
find_free_port_dll.FindFreePort.restype = ctypes.c_int

def get_free_port():
    port = find_free_port_dll.FindFreePort()
    return port

@eel.expose
def quit():
    sys.exit()

eel.init('.')

free_port = get_free_port()

eel.start('index.html', size=(width, height), port=free_port)