import binascii
import itertools
import collections

parts = collections.OrderedDict([("0x69355f71",""), ("0xc2c8c11c",""), ("0xdf45873c",""), ("0x9d26aaff",""), ("0xb1b827f4",""), ("0x97d1acf4","")])
posibilities = list(itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!?_', 4))

tmp = ''
solution = ''

for s in posibilities:
	for s1 in s:
		tmp += s1
	if hex(binascii.crc32(bytes(tmp, "ascii"))) in parts:
		parts[hex(binascii.crc32(bytes(tmp, "ascii")))] = tmp
	tmp = ''

for s in parts.values():
	solution += s + "-"
print("solution: " + solution)