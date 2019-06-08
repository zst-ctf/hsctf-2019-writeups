# Cool Image
Forensics

## Challenge 
My friend told me he found a really cool image, but I couldn't open it. Can you help me access the image?

## Hint
Is the file really a PDF?

## Solution

	$ file cool.pdf 
	cool.pdf: PNG image data, 1326 x 89, 8-bit/color RGBA, non-interlaced
	$ cp cool.pdf cool.png
	$ open cool.png 

## Flag

	hsctf{who_uses_extensions_anyways}
