# Accessible Rich Internet Applications
Web

## Challenge 

A very considerate fellow, Rob believes that accessibility is very important!

NOTE: The flag for this challenge starts with flag{ instead of hsctf{

## Solution

The HTML file provided is obfuscated. Open it in a browser and see the source code.

There is a whole chunk of 1s and 0s below. There is a parameter called aria-posinset which is the indexing of the binary char.

I extracted it out in list.txt and then converted it to a python code.

	$ cat list.txt | sed 's/<div role="option" aria-posinset="/flag[/g' | sed 's/" aria-setsize="1040">/] += "/g' | sed 's|</div>|"|g' | grep flag


In python, merge all the bites together

	>>> flag = ['x']*2000
	>>> # <paste code>
	>>> ''.join(flag).replace('x', '')

And decode binary to ascii. https://www.binaryhexconverter.com/binary-to-ascii-text-converter
	
	im gonna add some filler text here so the page is a bit longer. lorem ipsum... here's the flag btw, flag{accessibility_is_cruci0

## Flag

	flag{accessibility_is_crucial}
