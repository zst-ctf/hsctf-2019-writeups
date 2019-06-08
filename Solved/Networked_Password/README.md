# Networked Password
Web

## Challenge 

Storing passwords on my own server seemed unsafe, so I stored it on a seperate one instead. However, the connection between them is very slow and I have no idea why.

https://networked-password.web.chal.hsctf.com/

Hint: You know the flag format.

## Solution

Simple timing attack. For each correct char, the server takes a longer time to respond.


	$ time python3 solve.py 
	progress: hsct 3.41
	progress: hsctf 4.01
	progress: hsctf{ 4.69
	progress: hsctf{s 4.97
	progress: hsctf{sm 5.49
	Retry hsctf{sm
	progress: hsctf{sm0 5.9
	progress: hsctf{sm0l 6.11
	Retry hsctf{sm0l
	progress: hsctf{sm0l_ 6.86
	progress: hsctf{sm0l_f 7.4
	progress: hsctf{sm0l_fl 7.94
	progress: hsctf{sm0l_fl4 8.54
	Retry hsctf{sm0l_fl4
	progress: hsctf{sm0l_fl4g 9.1
	progress: hsctf{sm0l_fl4g} 9.43

	real	20m20.293s
	user	1m24.300s
	sys	0m14.661s

## Flag

	hsctf{sm0l_fl4g}
