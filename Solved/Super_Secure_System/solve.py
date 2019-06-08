#!/usr/bin/env python3
import socket
import telnetlib
import string

def connect_server():
    s = socket.socket()
    s.connect(('crypto.hsctf.com', 8111))

    t = telnetlib.Telnet()
    t.sock = s
    return t

flag = [' '] * 100
charset = string.printable

def main():
    for ch in charset:
        t = connect_server()

        t.read_until(b'Here is my super secret message: ')
        secret = t.read_until(b'\n').decode()
        secret = bytes.fromhex(secret)

        t.read_until(b'Enter the message you want to encrypt: ')
        fuzz_payload = ch * len(secret)
        t.write(fuzz_payload.encode() + b'\n')

        t.read_until(b'Encrypted: ')
        fuzzed = t.read_until(b'\n').decode()
        fuzzed = bytes.fromhex(fuzzed)

        #print('secret', secret.hex())
        #print('fuzzed', fuzzed.hex())

        # fill in all chars
        for i, (a, b) in enumerate(zip(fuzzed, secret)):
            if a == b:
                flag[i] = ch

        progress = ''.join(flag)
        print("Progress:", progress)

        # quit early if done
        if (' ' not in progress.strip() and
            progress.strip().startswith('hsctf{') and
            progress.strip().endswith('}')):
            quit()

if __name__ == '__main__':
    main()
