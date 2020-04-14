#  Test program for communication of Snap7 python with S7 1200
# Reading coils array
# by Radosław Tecmer
# radek69tecmer@gmail.com
# ------------------------

import snap7
import struct
import csv


# function reading coils (byte_out - PLC) (byte-size - PLC coils size) (out_bit - PLC coil)


def read_coils_s7(byte_out, byte_size, out_bit):
    byte_bit = client.ab_read(byte_out, byte_size)
    byte_bit_array = (byte_bit[0])
    byte_coils = bin(byte_bit_array).replace("0b", "")
    result = (byte_coils[out_bit])
    return result


client = snap7.client.Client()
client.connect('192.168.1.121', 0, 1)
print('connected to PLC')


coil_nr1 = read_coils_s7(0, 8, 1)
print(coil_nr1)

