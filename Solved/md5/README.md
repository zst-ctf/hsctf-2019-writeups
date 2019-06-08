# md5--
Web

## Challenge 

Written by: dwang

md5-- == md4

https://md5--.web.chal.hsctf.com

Note: If the link above doesn't work, try https://md4.web.chal.hsctf.com

## Solution

This is a web challenge, not crypto. So we assume wedo not need to break MD4.

We see there is a double-equal operator used in PHP which may be the vulnerability

-https://news.ycombinator.com/item?id=9484757
-https://github.com/spaze/hashes

Similar to this challenge

- https://github.com/bl4de/ctf/blob/master/2017/HackDatKiwi_CTF_2017/md5games1/md5games1.md

We need to bruteforce to get to strings which start with `0e`. In PHP, strings with 0e is treated like a float which equals to zero.

After many hours of bruteforcing, I finally got a string.

	$ python3 md4.py 
	hash=01339929483967618880605757000892, input=0000e7022066
	hash=05519589531120432303221252151901, input=0000e25317960
	hash=05988132038745101301048560678376, input=0000e33003193
	hash=077246068687740131800e3081993684, input=0000e51131519
	hash=06607184228172955602806147683562, input=0000e69055806
	hash=04037411826213674448990328790983, input=0000e71276156
	hash=04052607291878131471921869390957, input=0000e97615983
	hash=06913618023371172132220e64588475, input=0000e206136468
	hash=02962460051890840164902253355477, input=0000e208295487
	hash=09310594003656252201689855337565, input=0000e209303653
	hash=075360e2899369118855555056288499, input=0000e220728330
	hash=03290e86612621412085723805977650, input=0000e229844858
	hash=03254401523679077628249302497388, input=0000e232307128
	hash=00529996276925852889302670873348, input=0000e251240386
	hash=07660671324523839480876245148901, input=0000e291047253
	hash=04955202265546342370511229939567, input=0000e343605930
	hash=03174491773427170323274347454790, input=0000e348452776
	hash=0e700792641619389821358440376109, input=0000e435260724

https://md4.web.chal.hsctf.com/?md4=0000e435260724

## Flag

	hsctf{php_type_juggling_is_fun}