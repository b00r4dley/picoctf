#!/usr/bin/env python3

import string


flag = []

# Context manager; open() creates a pointer (handler of the file).
with open("message.txt") as filp:

	contents = filp.read()
	numbers = [ int(v) for v in contents.split() ]
	for number in numbers:
		modulus_37 = number % 37

		if modulus_37 in range(26):
			flag.append(string.ascii_uppercase[modulus_37])
		elif modulus_37 in range(26,36):
			flag.append(string.digits[modulus_37 - 26]) 
		else:
			flag.append("_")

	print("picoCTF{%s}" % "".join(flag))

	filp.close()