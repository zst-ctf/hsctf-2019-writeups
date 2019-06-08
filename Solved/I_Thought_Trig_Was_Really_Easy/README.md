# I Thought Trig Was Really Easy
Reversal

## Challenge 

After finishing a hard lesson in geometry class, Keith decided that he wanted to put your understanding of trig and python to the test. Can you solve his challenge?

Hint: Align each letter of input with its corresponding group of characters for output.

## Solution

If we do some debugging, we see the output is 

	$ python3 debug.py 
	Enter the text: a
	out_i=0: [1, 1] len=2
	Nope sorry, try again!
	
	$ python3 debug.py 
	Enter the text: ab
	out_i=0: [-2, 1] len=2
	out_i=1: [-2, 1, 2, -1, 4] len=5
	Nope sorry, try again!
	
	$ python3 debug.py 
	Enter the text: abc
	out_i=0: [-1, 1] len=2
	out_i=1: [-1, 1, -1, 4, -1] len=5
	out_i=2: [-1, 1, -1, 4, -1, -4, 3, -2, 5] len=9
	Nope sorry, try again!
	
	$ python3 debug.py 
	Enter the text: abcd
	out_i=0: [-4, 1] len=2
	out_i=1: [-4, 1, -1, 4, 4] len=5
	out_i=2: [-4, 1, -1, 4, 4, -4, 3, -2, -2] len=9
	out_i=3: [-4, 1, -1, 4, 4, -4, 3, -2, -2, -5, 4, -3, 6, -1] len=14
	Nope sorry, try again!

The output length is this sequence.

	if n = 3,
	output_length = 2+3+4

	if n = 4,
	output_length = 2+3+4+5

We can [transform it into a formula](https://www.varsitytutors.com/hotmath/hotmath_help/topics/sum-of-the-first-n-terms-of-an-arithmetic-sequence)

	Sn= (a1+an)* (n/2) , 
	where n is the number of terms, a1 is the first term and an is the last term. 

	output_length = (2+[n+1]) * (n/2)
	output_length = (n+3) * (n/2)

We see that the `ans` provided has a length of 90.

- Using WolframAlpha, I solved for `(n+3) * (n/2) = 90`
- Answer is `n = 12`

According to the hint, we can actually bruteforce each group of the flag.

	$ python3 solve.py 
	group [-25, 1]
	flag: :
	group [10, 7, 4]
	flag: :h
	group [7, 2, 9, 3]
	flag: :hy
	group [8, 1, 10, 3, -1]
	flag: :hyp
	group [-8, 3, -6, 5, -4, 7]
	flag: :hype
	group [-5, 8, -3, 10, -1, 12, 10]
	flag: :hyper
	group [7, -6, 9, -4, 11, -2, 13, -2]
	flag: :hypert
	group [-11, 6, -9, 8, -7, 10, -5, 12, 1]
	flag: :hyperth
	group [-12, 7, -10, 9, -8, 11, -6, 13, -4, 11]
	flag: :hypertho
	group [6, -13, 8, -11, 10, -9, 12, -7, 14, -5, 22]
	flag: :hyperthon
	group [-16, 7, -14, 9, -12, 11, -10, 13, -8, 15, -6, -2]
	flag: :hyperthonk
	group [2, -21, 4, -19, 6, -17, 8, -15, 10, -13, 12, -11, 5]
	flag: :hyperthonk:
	final flag: :hyperthonk:

## Flag

	hsctf{:hyperthonk:}
