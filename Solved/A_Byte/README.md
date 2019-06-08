# A Byte
Reversal

## Challenge

a-byte

## Solution

Decompiled Ghidra

	  local_10 = *(long *)(in_FS_OFFSET + 0x28);
	  if (iParm1 == 2) {
	    __s = *(char **)(lParm2 + 8);
	    sVar3 = strlen(__s);
	    if ((int)sVar3 == 0x23) {
	      local_48 = 0;
	      while (local_48 < 0x23) {
	        __s[(long)local_48] = __s[(long)local_48] ^ 1;
	        local_48 = local_48 + 1;
	      }
	      
	      <snip>

	      iVar1 = strcmp(&local_38,__s);
	      if (iVar1 == 0) {
	        puts("Oof, ur too good");
	        uVar2 = 0;
	        goto LAB_00100891;
	      }
	    }
	  }
	  puts("u do not know da wae");

From the code:

1. it takes in a parameter with length of 0x23.
2. it XORs each char with key of 0x01
3. then part where I removed due to brevity (`<snip>` portion of the code) is a long array of characters to be compared to using strcmp().

Use LD_PRELOAD to hijack strcmp(). We can print out our text/

	$ gcc -fPIC -c strcmp-hijack.c -o strcmp-hijack.o
	$ gcc -shared -o strcmp-hijack.so strcmp-hijack.o
	$ chmod +x a-byte 
	
	$ LD_PRELOAD="./strcmp-hijack.so" ./a-byte 
	u do not know da wae
	
	$ LD_PRELOAD="./strcmp-hijack.so" ./a-byte $(pwn cyclic 35)
	S1 eq irbugzv1v^x1t^jo1v^e5^v@2^9i3c@138|
	S2 eq ````c```b```e```d```g```f```i```h``
	Oof, ur too good

Then we get the string, we need to XOR with 0x01.

	$ python3
	>>> def bxor(a1, b1):
	...     encrypted = [ (a ^ b) for (a, b) in zip(a1, b1) ]
	...     return bytes(encrypted)
	... 

	>>> import itertools
	>>> bxor(b'irbugzv1v^x1t^jo1v^e5^v@2^9i3c@138|', itertools.cycle(b'\x01'))
	b'hsctf{w0w_y0u_kn0w_d4_wA3_8h2bA029}'

## Flag

	hsctf{w0w_y0u_kn0w_d4_wA3_8h2bA029}
