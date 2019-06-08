# Tux's Kitchen
Cryptography

## Challenge 

Written by: Tux

I need to bake it!

nc crypto.hsctf.com 8112

## Solution

If we do some debugging, we see that we can reverse one process of the numbers. In this case, I reversed the prepared numbers to get the treasure numbers.

	Tux_s_Kitchen $ python3 test_bake.py 
	mess      [491331212338]
	bart      557867493151
	cart      593502638314
	dart      231779094114
	art0      491331212338
	art1      25593105266
	art2      97092635154
	art3      51483513586
	baked     [491331212338, 25593105266, 97092635154, 51483513586]
	treasure1 [31936528801970, 1689144947556, 6505206555318, 3500878923848]
	prepared  [31936516295774, 1689149218696, 6505219182170, 3501009442900]
	--------------------------------------------------
	treasure2 [31936528801970, 1689144947556, 6505206555318, 3500878923848]

See in this code

	def final_baking(food,key):
		baked = rand0m_mess(food,key)
		treasure = []
		for i in range(len(baked)):
			treasure.append(ord(food[i])*baked[i])
		treasure = prepare(treasure)
		return treasure

We know that the treasure number had the flag-ord multiplied with the baked number.

With this, we can test all characters and see which ones divide nicely with the treasure number. If it divides with no remainder, it is a possibility.

And if we do it many times, we can see which chars are repeated. The repeated chars should ideally be the flag alone.

Running our code, we see the flag somewhat

	['h4', 's', '!c', ':t', '3f"', '){', ':t', 'h4', '#i', '#i', '#i', '1', '1', '1', '#i', '#i', '#i', 's', 's', '_', '#i', 's', 's', 's', 's', 's', '_', 'y', 'o%', '0', "u'", '9r&', '_', 'b1', '1', '9r&', ':t', 'h4', 'd2', '4', 'y', '_', 's', '0', '7n', 'g', '_', '#i', ':t', '_', '#i', 's', '7n', ':t', '_', 'v;', 'e', '9r&', 'y', '_', 'l6$', 'o%', '7n', 'g', '_', '6', '6', '2', '1', '}', '']

Intelligent guessing, remove chars of `:%#"`. And run the script again, we get...

	['4h', 's', 'c!', 't', '3f', '{)', 't', '4h', 'i', 'i', 'i', '1', '1', '1', 'i', 'i', 'i', 's', 's', '_', 'i', 's', 's', 's', 's', 's', '_', 'y', 'o', '0', "u'", '&9r', '_', 'b1', '1', '&9r', 't', '4h', '2d', '4', 'y', '_', 's', '0', 'n7', 'g', '_', 'i', 't', '_', 'i', 's', 'n7', 't', '_', 'v;', 'e', '&9r', 'y', '_', '6l$', 'o', 'n7', 'g', '_', '6', '6', '2', '1', '}', '']


Now filter out by hand..

	'hsctf{' +

	't', '4h', 'i', 'i', 'i', '1', '1', '1', 'i', 'i', 'i', 's', 's', 
	'_', 

	'i', 's', 's', 's', 's', 's',
	'_', 

	'y', 'o', '0', "u'", '&9r',
	'_', 

	'b1', '1', '&9r', 't', '4h', '2d', '4', 'y', 
	'_',

	's', '0', 'n7', 'g',
	'_', 

	'i', 't', 
	'_', 
	
	'i', 's', 'n7', 't', 
	'_',

	'v;', 'e', '&9r', 'y',
	'_',

	'6l$', 'o', 'n7', 'g',
	'_',

	'6', '6', '2', '1'
	'}'

And combine them

	hsctf{
	thiii111iiiss_
	isssss_
	yo0ur_
	b1rthd4y_
	s0ng_
	it_
	isnt_
	very_
	long_
	6621} 

## Flag

	hsctf{thiii111iiiss_isssss_yo0ur_b1rthd4y_s0ng_it_isnt_very_long_6621} 
