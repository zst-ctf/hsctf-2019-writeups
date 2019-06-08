#!/usr/bin/env python3
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin
# export PYTHONPATH=~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin/python
from z3 import *

# Solver functions
solver = Solver()
bit_size = 64
s = [BitVec('SECRET_1', bit_size), BitVec('SECRET_2', bit_size)]

# TOP SECRET: DO NOT LEAK
def o(x,k):
    return x<<k
def m(a):
    #return a
    return a&0xffffffffffffffff

def next():
    b = m(s[0]+s[1])
    h()
    # print("debug", b)
    return m(b)
def p(k, x):
    #return x>>(64-k)
    return LShR(x, (64-k))
def x(b, a):
    return a^b
def oro(a, b):
    return a|b
def h():
    s1 = m(x(s[0],s[1]))
    s[0] = m(x(oro(o(s[0],55),p(55,s[0])),x(s1,(o(s1,14)))))
    s[1] = m(oro(o(s1,36),p(36,s1)))

# create variables of unknown
next_1 = BitVec('next_1', bit_size)
next_2 = BitVec('next_2', bit_size)
next_3 = BitVec('next_3', bit_size)
next_4 = BitVec('next_4', bit_size)
next_5 = BitVec('next_5', bit_size)
next_6 = BitVec('next_6', bit_size)

# Get integer for next() values from the combo
combo3 = b'hsctfissocoolwow'
next_7 = int.from_bytes(combo3[:8], "little")
next_8 = int.from_bytes(combo3[8:], "little")

# I took a few steps to derive the key
STEP = 3

# Step 1: consists of getting the secrets starting from next_5 onwards.
if STEP == 1:
    solver.add(next() == next_5) # 5
    solver.add(next() == next_6) # 6
    solver.add(next() == next_7) # 7
    solver.add(next() == next_8) # 8

# Step 2: we have secrets at step5, work backwards to get secret at step_3
if STEP == 2:
    solver.add(next() == next_3) # 3
    solver.add(next() == next_4) # 4
    solver.add(s[1] == 15168562398851639424) # next5, SECRET_2: 15168562398851639424
    solver.add(s[0] == 16344524629591564275) # next5, SECRET_1: 16344524629591564275
    solver.add(next() == next_5) # 5
    solver.add(next() == next_6) # 6
    solver.add(next() == next_7) # 7
    solver.add(next() == next_8) # 8

# Step 3: do one more time to get the original secret
if STEP == 3:
    next() # 1
    next() # 2
    solver.add(s[1] == 15319349121703965325) # next3, SECRET_2: 15319349121703965325
    solver.add(s[0] == 1975711866010926419) # next3, SECRET_1: 1975711866010926419
    solver.add(next() == next_3) # 3
    solver.add(next() == next_4) # 4
    solver.add(s[1] == 15168562398851639424) # next5, SECRET_2: 15168562398851639424
    solver.add(s[0] == 16344524629591564275) # next5, SECRET_1: 16344524629591564275
    solver.add(next() == next_5) # 5
    solver.add(next() == next_6) # 6
    solver.add(next() == next_7) # 7
    solver.add(next() == next_8) # 8

# Helper methods
def bin2chr(data):
    result = b''
    while data:
        char = data & 0xff
        result += bytes([char])
        data >>= 8
    return result

def isp(d):
    ch = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    if all(c in ch for c in d):
        return d
    else:
        # return d.encode('hex')
        return d.hex().encode()

print(bin2chr(next_7) + bin2chr(next_8))
assert (bin2chr(next_7) + bin2chr(next_8)) == combo3

# check if there is a solution
if solver.check() != sat:
    print("No solution")
    quit()

model = solver.model()
# print(model)

for name in model:
    value = model[name]
    print(f'{name}: {value}')

# 
next_3_int = int(str(model[next_3]))
next_4_int = int(str(model[next_4]))
next_5_int = int(str(model[next_5]))
next_6_int = int(str(model[next_6]))
next_7_int = next_7
next_8_int = next_8

Xcombo1 = isp(bin2chr(next_3_int)) + b"" + isp(bin2chr(next_4_int))
Xcombo2 = isp(bin2chr(next_5_int)) + b"" + isp(bin2chr(next_6_int))
Xcombo3 = isp(bin2chr(next_7_int)) + b"-" + isp(bin2chr(next_8_int))

print('Combo1:', Xcombo1)
print('Combo2:', Xcombo2)
print('Combo3:', Xcombo3)
print('FLAG:', b'hsctf{' + Xcombo1 + b' ' + Xcombo2 + b'}')
