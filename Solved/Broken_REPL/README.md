# Broken REPL
Misc

## Challenge 

My friend says that there is a bug in my REPL. Can you help me find it?

nc misc.hsctf.com 8550

Hint: What happens to the given input?

## Solution

Input goes through compile().

Trying on my local Python instance... It was not easy to find the cause of MemoryError. I found out that the cause was due to parser stacks.

	>>> compile('A'*1000, "<input>", "exec")
	<code object <module> at 0x10fe445d0, file "<input>", line 1>
	
	>>> compile('A'*2000, "<input>", "exec")
	<code object <module> at 0x10fe44810, file "<input>", line 1>
	
	>>> compile('['*2000, "<input>", "exec")
	s_push: parser stack overflow
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	MemoryError

	>>> compile('['*100, "<input>", "exec")
	s_push: parser stack overflow
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	MemoryError

Flag

	$ nc misc.hsctf.com 8550
	>>> [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
	s_push: parser stack overflow
	hsctf{dont_you_love_parsers}

## Flag

	hsctf{dont_you_love_parsers}
