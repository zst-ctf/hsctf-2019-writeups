import hashlib

def MD4(x):
	hexdigest = hashlib.new("md4", x.encode()).hexdigest()
	return hexdigest

x = 162333977
x = 0
while True:
	plaintext = f"0000e{x}"
	hashed = MD4(plaintext)
	if hashed.startswith('0') and hashed.replace('0e', '', 1).isdigit():
		print(f'hash={hashed}, input={plaintext}')

	x += 1
