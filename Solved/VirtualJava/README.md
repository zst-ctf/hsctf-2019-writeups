# VirtualJava
Reversal

## Challenge 

There's nothing like executing my own code in Java in my own special way.

## Solution

We get a java program that implements an instruction set (ie. a mini-VM).

However, there is no need to analyse the instructions.

From the code, we see that each character of our input will be checked and it will exit at the index which is wrong.

    char[] c = args[0].toCharArray();
    for (int i = 0; i < c.length; i++) {
        String s = getOutput(Math.abs(java.run(i, (int) c[i])));
        if (s.equals(owo[1])) {
            System.exit(0);
        }
    }

Hence, if we add in a single line, to print the index, we know which index is wrong.

        char[] c = args[0].toCharArray();
        for (int i = 0; i < c.length; i++) {
            String s = getOutput(Math.abs(java.run(i, (int) c[i])));
            if (s.equals(owo[1])) {
                System.out.println(i);
                System.exit(0);
            }
        }

Knowing this, we run a bruteforce for char-by-char until the index increases. 


	$ javac VirtualJavaModified.java 
	$ python3 bruteforce.py 
	30 hsctf{y0u_d3f34t3d_th3_b4by_vm`
	30 hsctf{y0u_d3f34t3d_th3_b4by_vm{
	30 hsctf{y0u_d3f34t3d_th3_b4by_vm|
	Traceback (most recent call last):
	  File "bruteforce.py", line 22, in <module>
	    index = int(result)
	ValueError: invalid literal for int() with base 10: 'ur too pro for this'

## Flag

	hsctf{y0u_d3f34t3d_th3_b4by_vm}
