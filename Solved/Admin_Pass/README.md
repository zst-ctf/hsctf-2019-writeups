# Admin Pass
Misc

## Challenge 

Hey guys, found a super cool website at http://misc.hsctf.com:8001!

## Solution

The webpage has a link to the source code

- https://gitlab.com/WeastieWeastie/admin-password/

There is a md5 hash of the flag, but it cannot be cracked by CrackStation or any other online database.

Look through all the commits and we eventually find the flag

- https://gitlab.com/WeastieWeastie/admin-password/commit/2f48a1b4b2eba922bca1e644b9a9d609cf08be77

## Flag

	hsctf{i_love_richard_stallman_hes_so_cute_8a65926fcdcdac0b}
