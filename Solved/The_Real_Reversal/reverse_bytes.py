#!/usr/bin/env python3
with open('reversed.txt', 'rb') as f:
	contents = f.read()
'''
def reverse_bits(orig):
	return int('{:08b}'.format(orig)[::-1], 2)

output = b''
for b in contents:
	output += bytes([reverse_bits(int(b))])
'''
output = contents[::-1]
with open('fixed.txt', 'wb') as f:
	f.write(output)