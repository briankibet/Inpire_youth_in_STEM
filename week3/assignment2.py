#!/usr/bin/env python3
# This is a singe line commet
# Python programme to illustrate
# Name : brian kibet
# Email : blkagatum@gmail.com
# Date : 21th feb 2023
# File : assignment2.py
#when drawing a diamond
h = eval(input("Enter diamond's height:"))

for x in range(h):
    print("" * (h - x),"*" * (2*x + 1))
for x in range(h - 2, -1):
    print("" * (h - x),"*" * (2*x + 1))