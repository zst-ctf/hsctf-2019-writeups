# Super Secure System
Cryptography

## Challenge 

	Written by: Tux

	Keith made a SUPER SECURE SYSTEM!!! He claims it is so secure as long as he doesn't reuse his key...

	nc crypto.hsctf.com 8111

## Solution

We have a server where we can encrypt our own stuff. An example message (the flag) is also encrypted.

	* * * SUPER SECURE SYSTEM * * *
	My encryption system is impossible to crack if used once!
	You can use this system to encrypt any of your messages with my super special key!!!
	Here is my super secret message: 3b1e092f2e0f3f662d004f041278394959632d18472d531a733e3f1c2913664c514362710030624d3a1562056105657b2d6a44044a

	Enter the message you want to encrypt: 
	Encrypted: 

	Enter the message you want to encrypt: 
	Encrypted: 

	Enter the message you want to encrypt: hello

	Encrypted: 3b08063727


Analysis:

- Encryption hex is the same length as the plaintext.
- The encryption differs from each run.
- The encryption differs for each character index.
- ***The encryption for the example and our submitted encryption is the same at the same character index***

Solving:

- So we can write a script to submit 'aaaaa...', 'bbbbb...', 'ccccc...' and so on.
- From this, we can then compare the example to our crafted payload.
- Piece together the flag bit by bit...

Run the script

	$ python3 solve.py 
	Progress:        0
	Progress:        0                        1
	Progress:        0                        1
	Progress:        0   3   3    3        3  1 3   3   3  3
	...
	Progress:   c f  0  d3d  3  de3c   4   3  1 3   3c  3  355a9e
	Progress:   c f  0  d3d  3  de3c   4   3  1 3   3c  3  355a9e
	Progress: h c f h0  d3d  3  de3c   4  h3  1 3   3c  3  355a9e
	...
	Progress: hsctf h0w d3d y3u de3cry 4 th3 s1p3  s3cu 3 m355a9e
	Progress: hsctf h0w d3d y3u de3cry 4 th3 s1p3  s3cu 3 m355a9e
	Progress: hsctf h0w d3d y3u de3cry 4 th3 s1p3  s3cu 3 m355a9e
	Progress: hsctf h0w d3d y3u de3cry 4 th3 s1p3  s3cu 3 m355a9e
	...
	Progress: hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e?}

## Flag

	hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e?}
