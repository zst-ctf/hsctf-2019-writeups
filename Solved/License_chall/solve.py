#!/usr/bin/env python3
import string

input_map = "abcdefghijklmnopqrstuvwxyz0123456789_{}"
output_map = "X-YZ012-34567-890AB-CDEFG-HIJKL-LMNOP-QRSTU-VMO".replace('-', '')

def decode(s):
    lookup = str.maketrans(output_map, input_map)
    return s.translate(lookup)

license = "4-EZF2M-7O5F4-V9P7O-EVFDP-E4VDO-O".replace('-', '')

print("Decode", decode(license))
