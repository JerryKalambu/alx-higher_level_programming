#!/usr/bin/python3
"""Print the alphabet in lowercase, not follow by a new line."""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
