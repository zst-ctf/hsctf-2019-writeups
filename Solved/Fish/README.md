# Fish
Forensics

## Challenge 

I got a weird image from some fish. What is this?

## Solution

A JPEG file, with a weird string at the end. Perhaps bobross63 is some sort of password.

	$ strings fish.jpg | tail -5
	$:$1
	O'#Z
	QU$K
	B5%Go
	bobross63

I found an online tool which can decode the message for us.

- https://futureboy.us/stegano/decinput.html

## Flag

	hsctf{fishy_fishy_fishy_fishy_fishy_fishy_fishy123123123123}
