import os


def solve():
    with open('ciphertext.txt') as f:
        line = f.readline()
        hex_line = bytearray.fromhex(line)
        print(hex_line)
        for i in range(0x00, 0xff+1):
            r = xor(hex_line, i)
            if r.__contains__("flag"):
                print(r)
    pass


def xor(line, key):
    result = ""
    for c in line:
        result += (chr(ord(chr(c)) ^ key))
    return result


solve()
