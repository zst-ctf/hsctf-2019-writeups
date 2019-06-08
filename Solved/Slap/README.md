# Slap
Forensics

## Challenge 
Don't get slapped too hard.

## Solution

There's text hidden in the EXIF.

	$ exiftool slap.jpg | grep hsctf

	Location Shown Country Name     : Lorem ipsum dolor sit amet, consectetur 
	adipiscing elit, sed do eiusmod tempor incididunt ut la bore et dolore magna 
	aliqua. Massa id neque aliquam vestibulum morbi blandit
	cursu hsctf{twoslapsnonetforce} s risus. Sed viverra ipsum nunc aliquet 
	bibendum. Nisl purus in mollis nunc sed.

## Flag

	hsctf{twoslapsnonetforce}
