import base64
import binhex
import os
import xortool

"""
xortool -x -l 5 -c "0x20" mbxor_cipher.txt  --> to give key
"""

def solve():
    with open("mbxor_cipher.txt") as cipher:
        line = cipher.readline()
        hex_line = bytearray.fromhex(line)
        x = xor(hex_line)
        print(x)


def xor(line):
    result = ""
    key = [0x57, 0x47, 0x75, 0x58, 0x6e]
    for idx, c in enumerate(line):
        result += chr(ord(chr(c)) ^ key[idx % 5])
    return result


key = "WGuXn"

solve()