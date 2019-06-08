# Forgot Your Password?
Reversal

## Challenge 

Written by: Ptomerty

Help! I got this new lock for Christmas, but I've forgotten the first two values. I know the last value is hsctfissocoolwow. I also managed to grab a copy of their secret key generator. Can you help me out?

Note: submit the first two combo values separated by a space in hex format.

## Solution


	[SECRET_2 = 15168562398851639424,
	 SECRET_1 = 16344524629591564275,
	 next_6 = 685604511556443309,
	 next_5 = 13066342954733652083]
	SECRET_2: 15168562398851639424
	SECRET_1: 16344524629591564275
	next_6: 685604511556443309
	next_5: 13066342954733652083

	real	1m49.909s
	user	1m48.297s
	sys	0m0.489s
	Forgot_Your_Password $ 

To solve this, I will be using Microsoft Z3 which is a constraint solver.

In the program, we see that next() is called twice. After each iteration, the SECRET is replaced.

I decided to split the solving into multiple parts as it was too slow to solve everything at once.

### Step 1:

I decided to solve for secrets starting from next_5 onwards.

	# Get integer for next() values from the combo
	combo3 = b'hsctfissocoolwow'
	next_7 = int.from_bytes(combo3[:8], "little")
	next_8 = int.from_bytes(combo3[8:], "little")

    solver.add(next() == next_5) # 5
    solver.add(next() == next_6) # 6
    solver.add(next() == next_7) # 7
    solver.add(next() == next_8) # 8

With this, we can solve for next_5 and next_6 which constitues our combo2.

	$ time python3 test.py 
	SECRET_2: 15168562398851639424
	SECRET_1: 16344524629591564275
	next_6: 685604511556443309
	next_5: 13066342954733652083

	real	1m54.325s
	user	1m51.184s
	sys	0m0.800s

### Step 2:

With the secret at next_5, work backwards to solve secret at next_3.

	$ time python3 test.py 
	SECRET_2: 15319349121703965325
	SECRET_1: 1975711866010926419
	next_6: 685604511556443309
	next_5: 13066342954733652083
	next_4: 15145497047134903538
	next_3: 17295060987714891744

	real	0m0.726s
	user	0m0.521s
	sys	0m0.090s

### Step 3:

Using the secrets from next_3, work backwards one more time

	$ time python3 test.py 
	SECRET_2: 16423178736247365903
	SECRET_1: 7294543424534665732
	next_6: 685604511556443309
	next_5: 13066342954733652083
	next_4: 15145497047134903538
	next_3: 17295060987714891744

	real	0m1.189s
	user	0m0.990s
	sys	0m0.105s

### Step 4:

Modify the code slightly and we get our flag

	$ time python3 test.py 
	b'hsctfissocoolwow'
	SECRET_2: 16423178736247365903
	SECRET_1: 7294543424534665732
	next_6: 685604511556443309
	next_5: 13066342954733652083
	next_4: 15145497047134903538
	next_3: 17295060987714891744
	Combo1: b'e06f76cd556604f0f21c34f1519d2fd2'
	Combo2: b'73c8535ab0f954b5ad1cbab7abc18309'
	Combo3: b'hsctfiss-ocoolwow'
	FLAG: b'hsctf{e06f76cd556604f0f21c34f1519d2fd2 73c8535ab0f954b5ad1cbab7abc18309}'

	real	0m1.043s
	user	0m0.951s
	sys	0m0.077s


## Flag

	hsctf{e06f76cd556604f0f21c34f1519d2fd2 73c8535ab0f954b5ad1cbab7abc18309}
