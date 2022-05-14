#!/usr/bin/env python3

import string


flag = []

# Context manager; open() creates a pointer (handler of the file).
with open("message.txt") as filp:

	contents = filp.read()
	numbers = [ int(v) for v in contents.split() ]
	print(numbers)
	for number in numbers:
		modulus_41 = pow(number, -1, 41)

		if modulus_41 in range(1,27):
			flag.append(string.ascii_uppercase[modulus_41 - 1])
		elif modulus_41 in range(27,37):
			flag.append(string.digits[modulus_41 - 27]) 
		else:
			flag.append("_")

	print("picoCTF{%s}" % "".join(flag))

	filp.close()