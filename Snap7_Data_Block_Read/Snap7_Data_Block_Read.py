#  Test program for communication of Snap7 python with S7 1200
# Reading data from one variable in a data block
# by Radosław Tecmer
# radek69tecmer@gmail.com
# ------------------------

import snap7
import struct
import csv

# Function read data from instance db


def data_block_read(db_number, inst_number, data):
    db_val = client.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!f", db_val[:4])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = float('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.4f' % result
    return my_str_value


client = snap7.client.Client()
client.connect('192.168.1.121', 0, 1)
print('connected to PLC')

# Read temperature Outside (db 3, instance 24, data =" real" )
outside = data_block_read(3, 24, 4)

print(outside)