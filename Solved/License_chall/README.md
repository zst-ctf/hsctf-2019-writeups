# License
Reversal

## Challenge 

	Description: Keith made a cool license-checking program but he forgot the flag he used to create the key! To make matters worse, he lost the source code and stripped the binary for his license-generator program. Can you help Keith recover his flag? All he knows is:

	The license key is 4-EZF2M-7O5F4-V9P7O-EVFDP-E4VDO-O
	He put his name (in the form of 'k3ith') as the first part of the flag
	There are 3 underscores
	The flag is in the format hsctf{}
	The flag doesn't have random character sequences (you should be able to read the entire flag easily).
	The flag only contains lowercase English letters and numbers.
	The generator might produce the same keys for different inputs because Keith was too lazy to write the algorithm properly.

## Solution

There's no need to actually decompile the program. Some intelligent guesses are needed.

License key maps with a 1 char input to 1 char output.

	$ ./license 
	gimme dat string: hsctf{
	generating key for: hsctf{
	4-EZF2M

License key does not depend on index position

	$ ./license 
	gimme dat string: hhhhhh
	generating key for: hhhhhh
	4-44444

Thus, get a map of input to output. We see that indeed there are some inputs that map to a single output (ie. produce the same keys for different inputs)

	$ ./license 
	gimme dat string: abcdefghijklmnopqrstuvwxyz0123456789_{}
	generating key for: abcdefghijklmnopqrstuvwxyz0123456789_{}
	
Using python, I mapped the output string back to the input

	$ python3 solve.py 
	Decode hsctf{k}ith_m4k}s_tr4sh_r}}

Note that there are some chars that have multiple inputs to a single output. So running again but removing the chars `{}` give me.

	$ python3 solve.py 
	Decode hsctf1k3ith_m4k3s_tr4sh_r33

## Flag

	hsctf{k3ith_m4k3s_tr4sh_r3}
