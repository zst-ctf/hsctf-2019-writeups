#!/usr/bin/env python3
import string

def get_position(contents, forward=True):
	x = 0
	y = 0
	for line in contents.splitlines():
		if 'north' in line:
			y += 1
		if 'south' in line:
			y -= 1
		if 'west' in line:
			x += 1
		if 'east' in line:
			x -= 1
	return (x, y)

flag = ''
for i in range(1, 12+1):
	filename = f'./input/{i}.txt'
	with open(filename) as f:
		contents = f.read()
	x, y = get_position(contents)

	distance_half = (x**2 + y**2)**0.5
	distance = 2 * distance_half

	letter = round(distance) % 26
	letter = string.ascii_lowercase[letter]
	flag += letter

print(f'hsctf{{{flag}}}')