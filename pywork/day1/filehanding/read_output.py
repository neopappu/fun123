#!/usr/bin/env python3

filename = "output.txt"

with open(filename, "r") as f:
    contents = f.read()
print(contents)
