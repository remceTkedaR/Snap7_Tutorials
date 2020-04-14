# Library Snap7
# Connection with the PLC controller
# by  Radosław Tecmer
# e-mail radek69tecmer@gmail.com
# --------------------------------------------------


import snap7
import time


# client = snap7.client.Client()
# client.connect('192.168.1.121', 0, 1)


try:
    client = snap7.client.Client()
    client.connect('192.168.1.121', 0, 2)
except snap7.snap7exceptions.Snap7Exception:
    time.sleep(0.2)
    client = snap7.client.Client()
    client.connect('192.168.1.121', 0, 1)
    print('connected to PLC')
else:
    print('not connected')

