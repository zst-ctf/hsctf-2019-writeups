# Hidden Flag
Misc

## Challenge 

This image seems wrong.....did Keith lose the key again?

## Solution

We see the key at the end of the file.

	$ strings chall.png | tail -5
	PnvI
	hnv0}ib
	i03-?
	ible +8-
	key is invisible

If we do the command "xxd", we see that the file does not have a PNG header. It appears to be encrypted using XOR key.

Decrypt XOR using python to get back the original image.

[solve.py](solve.py)

## Flag

	hsctf{}0t_1nv1s1bl3_an5m0r3?-39547632}
