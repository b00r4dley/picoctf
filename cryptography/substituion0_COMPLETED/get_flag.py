#!/usr/bin/env python3

import string

with open("message.txt") as filp:
	contents = filp.read()

uppercase_key = "QWITJSYHXCNDFERMUKGOPVALBZ"
lowercase_key = uppercase_key.lower()

flag = []

for character in contents:
	if character.isupper():
		position = uppercase_key.index(character)
		flag.append(string.ascii_uppercase[position])
	elif character.islower():
		position = lowercase_key.index(character)
		flag.append(string.ascii_lowercase[position])
	else:
		flag.append(character)

flag = "".join(flag)

print(flag.split()[-1])
