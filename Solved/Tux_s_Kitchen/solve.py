#!/usr/bin/env python3
import string
import socket
import telnetlib

charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#charset = charset.replace(':', '').replace('#', '').replace('%', '').replace('"', '')
#charset = string.printable

def reverse_prepare(food):
    # Reverse ADD of MY_LUCKY_NUMBER
    MY_LUCKY_NUMBER = 29486316
    food[len(food)-1] -= MY_LUCKY_NUMBER * len(food)
    # Reverse XOR of MY_LUCKY_NUMBER
    good_food = []
    for i in range(len(food)):
        good_food.append(food[i]^MY_LUCKY_NUMBER)
    return good_food


def get_numbers():
    # Connect to server
    s = socket.socket()
    s.connect(('crypto.hsctf.com', 8112))
    t = telnetlib.Telnet()
    t.sock = s

    # Retrieve contents
    t.read_until(b'--    \n')
    array_contents = t.read_until(b']').decode().replace('L', '')
    array_contents = eval(array_contents)
    return array_contents


def get_possible_chars(numb):
    # Return array of chars that number is divisible by
    chars = []
    for ch in charset:
        if numb % ord(ch) == 0:
            chars.append(ch)
    return chars

def main():
    overall_possible = [list(charset)] * len(get_numbers())
    # From server, we see 71 numbers so length is 71

    while True:
        # Get possible char groups
        prepared_numbers = get_numbers()
        numbers = reverse_prepare(prepared_numbers)
        possible = list(map(get_possible_chars, numbers))
        # print(possible)

        # Eventually intersected groups will produce one single char per group
        next_overall_possible = []
        for a, b in zip(possible, overall_possible):
            intersect = set(a).intersection(b)
            next_overall_possible.append(intersect)
        overall_possible = next_overall_possible
        #print(overall_possible)
        print(list(map(lambda item: ''.join(item), overall_possible)))

        # Check if all groups have 1 element, when
        # this occurs the process has been completed.
        len_possible = list(map(len, overall_possible))
        if all(item == 1 for item in len_possible):
            break

    flag = ''.join(map(lambda item: item[0], overall_possible))
    print(flag)

if __name__ == '__main__':
    main()
