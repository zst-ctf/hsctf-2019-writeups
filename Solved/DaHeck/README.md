# DaHeck
Reversal

## Challenge 

DaHeck.java

## Solution

The code is very confusing, but in essence, ***for each char, subtract heck[i] from flag[i] to produce return_value***.

	flag[i] - heck[i] = return_value[i]

Simply do the reverse to get back the flag

	flag[i] = heck[i] + return_value[i]

Run [Solve.java](Solve.java) to get the flag

## Flag

	hsctf{th4t_w4s_fun!_l3ts_try_s0m3_m0r3_r3v3rs3}
