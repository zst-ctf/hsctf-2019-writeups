#!/usr/bin/env python3
import math
import string

# Provided
def nice_math(x, y):
    return round(x + y*math.cos(math.pi * x))

lots_of_nums = lambda n,a:(lambda r:[*r,n-sum(r)])(range(n//a-a//2,n//a+a//2+a%2))

def get_number(char):
    return ord(char) - 96

ans = [-25, 1, 10, 7, 4, 7, 2, 9, 3, 8, 1, 10,
            3, -1, -8, 3, -6, 5, -4, 7, -5, 8, -3,
            10, -1, 12, 10, 7, -6, 9, -4, 11, -2,
            13, -2, -11, 6, -9, 8, -7, 10, -5, 12,
            1, -12, 7, -10, 9, -8, 11, -6, 13, -4,
            11, 6, -13, 8, -11, 10, -9, 12, -7, 14,
            -5, 22, -16, 7, -14, 9, -12, 11, -10, 13,
            -8, 15, -6, -2, 2, -21, 4, -19, 6, -17, 8,
            -15, 10, -13, 12, -11, 5]

# Solution to bruteforce flag
len_inp = 12

# groups will be length 2, 3, 4, and so on.
group_index = 0
group_length = 2

flag = ''
for i in range(0, len_inp):
    # extract each group
    group = ans[group_index:group_index+group_length]

    # bruteforce character until our answer group equals our generated group
    print('group', group)
    for ch in string.printable:
        generated_nums = lots_of_nums(nice_math(get_number(ch), len_inp - i), i + 1)
        generated_group = list(map(lambda j: nice_math(j, i + 1), generated_nums))
        # print('gener', generated_group)

        if generated_group == group:
            flag += ch
            print('flag:', flag)
            break

    # keep track of group start and end indices
    group_index += group_length
    group_length += 1

print('final flag:', flag)
