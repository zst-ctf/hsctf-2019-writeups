# Locked Up
Misc

## Challenge 
My friend gave me a zip file with the flag in it, but the zip file is encrypted. Can you help me open the zip file?

## Hint
Try opening it. What happens?

## Solution

If we try to unzip, we see the filenames. The password is in one of the filenames

    $ unzip locked.zip 
    Archive:  locked.zip
    [locked.zip] !lBo;!71}c'&!?m$NAtfBLH password: 
       skipping: !lBo;!71}c'&!?m$NAtfBLH  incorrect password
       skipping: !l^-W~zN>?}i*{jRYG:=X=b:5Hdp7U  incorrect password
       skipping: !m9*t0r9Rf%V"           incorrect password
       skipping: !_bubre6A{|TB:Q`#X1Vu#Zm<V  incorrect password
       skipping: !~fz'OO!FiRsH3fybOR1!B  incorrect password
       ...
       skipping: hsctf{w0w_z1ps_ar3nt_th@t_secUr3}  incorrect password

## Flag

    hsctf{w0w_z1ps_ar3nt_th@t_secUr3}
