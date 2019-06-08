# Bitecode
Reversal

## Challenge 

Keith went crazy and told me to work on the compiled form of Java instead of the source code. Unfortunately, all decompilers I've tried crash on attempting to decompile. Can you help out?

## Solution

Cannot decompile in any tools, Java class is also corrupted.

Use javap to view bytecode...

	 $ javap -v BiteCode
	Classfile /Bitecode/BiteCode.class
	  Last modified 4 Jun 2019; size 1365 bytes
	  MD5 checksum 56b9930da07186d4611b1ffb96da69ca
	public class BiteCode
	  minor version: 0
	  major version: 45
	  flags: (0x0001) ACC_PUBLIC
	  this_class: #62                         // BiteCode
	  super_class: #63                        // java/lang/Object
	  interfaces: 0, fields: 1, methods: 1, attributes: 0
	Constant pool:
	   #1 = String             #95            // Stuck? Maybe try Krakatau!

We see that we need to [download Krakatau](https://github.com/Storyyeller/Krakatau).

	$ git clone https://github.com/Storyyeller/Krakatau

We still cannot decompile

	$ python Krakatau/decompile.py BiteCode.class 
	Krakatau  Copyright (C) 2012-18  Robert Grosse
	This program is provided as open source under the GNU General Public License.
	See LICENSE.TXT for more details.

	Attempting to automatically locate the standard library...
	Unable to find the standard library
	processing target BiteCode, 1 remaining
	Loading BiteCode
	Traceback (most recent call last):
	  File "Krakatau/decompile.py", line 158, in <module>
	    decompileClass(path, targets, args.out, args.skip, magic_throw=args.xmagicthrow)
	  File "Krakatau/decompile.py", line 101, in decompileClass
	    c = e.getClass(target.decode('utf8'))
	  File "/Users/manzelseet/Desktop/hsctf2019-writeups/Bitecode/Krakatau/Krakatau/environment.py", line 24, in getClass
	    result = self._loadClass(name)
	  File "/Users/manzelseet/Desktop/hsctf2019-writeups/Bitecode/Krakatau/Krakatau/environment.py", line 90, in _loadClass
	    raise ClassLoaderError('ClassNotFoundException', name)
	Krakatau.error.ClassLoaderError: 
	ClassNotFoundException: BiteCode

We can only disassemble

	$ python Krakatau/disassemble.py BiteCode.class 
	Krakatau  Copyright (C) 2012-18  Robert Grosse
	This program is provided as open source under the GNU General Public License.
	See LICENSE.TXT for more details.

	processing target BiteCode.class, 1/1 remaining
	Class written to /Users/zst123/BiteCode.j
	0.0125799179077  seconds elapsed

Read the disassembly

	L87:    iconst_0 
	L88:    caload 
	L89:    ldc 189074585 
	L91:    ixor 
	L92:    ldc 189074673 
	L94:    isub 
	L95:    ifeq L106 
	L98:    pop 
	L99:    iload_2 
	L100:   ifne L535 
	L103:   jsr L51 
	L106:   dup 

	L107:   iconst_1 
	L108:   caload 
	L109:   ldc -227215135 
	L111:   ixor 
	L112:   ldc -227215214 
	L114:   isub 
	L115:   ifeq L126 
	L118:   pop 
	L119:   iload_2 
	L120:   ifne L179 
	L123:   jsr L51 
	L126:   dup 

We see that 2 numbers are loaded onto the stack and the XORed with each other.

At the same time, these numbers also appear in `$ javap -v BiteCode`, which makes it easy for me to extract the numbers.

I extracted all these numbers and then wrote a simple script to XOR the pairs together to produce the flag

	$ python3 solve.py 
	hsctf{wH04_u_r_2_pr0_4_th1$}

## Flag

	hsctf{wH04_u_r_2_pr0_4_th1$}
