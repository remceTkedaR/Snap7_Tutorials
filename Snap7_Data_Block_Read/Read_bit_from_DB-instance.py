#  Test program for communication of Snap7 python with S7 1200
# Reading bit from DB instance byte
# by Radosław Tecmer
# radek69tecmer@gmail.com
# ------------------------


import snap7
from snap7.util import *


def db_read_byte(plc, db_number, inst_number, size, byte_index, bit_index):
    db_area = plc.db_read(db_number, inst_number, size)
    db_byte = get_bool(db_area, byte_index, bit_index)
    return db_byte


if __name__ == "__main__":
    plc = snap7.client.Client()
    plc.connect('192.168.1.121', 0, 1)
    plc_db4_bb0 = db_read_byte(plc, 4, 0, 1, 0, 5)
    print(plc_db4_bb0)




