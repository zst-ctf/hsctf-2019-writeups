#!/usr/bin/env python3
import subprocess
import string

payload = ['x']*31

payload[0] = 'h'
payload[1] = 's'
payload[2] = 'c'
payload[3] = 't'
payload[4] = 'f'
payload[5] = '{'

index = 0

while index < 31:
	for ch in string.printable:
		payload[index] = ch
		payload_str = ''.join(payload)
		result = subprocess.check_output(['java', 'VirtualJavaModified', payload_str]).decode().strip()

		index = int(result)
		print(result, payload_str)
			
