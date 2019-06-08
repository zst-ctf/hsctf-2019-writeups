#!/usr/bin/env python3

from itertools import cycle

with open('chall.png', 'rb') as f:
	encrypted = f.read()

def bxor(a1, b1):
	encrypted = [ (a ^ b) for (a, b) in zip(a1, b1) ]
	return bytes(encrypted)

decrypted = bxor(encrypted, cycle(b'invisible'))

with open('fixed.png', 'wb') as f:
	f.write(decrypted)