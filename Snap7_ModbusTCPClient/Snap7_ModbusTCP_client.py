# Library Snap7 Modbus TCP client
# Connection with the PLC controller S7 1200
# by  Radosław Tecmer
# e-mail radek69tecmer@gmail.com
# --------------------------------------------------


import snap7
import struct
from pymodbus.client.sync import ModbusTcpClient

# Reading output coil S7  read_coils ( byte start, bit read) example ( 0, 8) -> Q0.0 - Q0.7
client = ModbusTcpClient('192.168.1.121')
result = client.read_coils(0, 8)


client = snap7.client.Client()
client.connect('192.168.1.121', 0, 1)

for i in range(8):
    print(result.bits[i])


# --end --