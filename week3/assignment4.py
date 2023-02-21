#!/usr/bin/env python3
# This is a singe line commet
# Python programme to illustrate
# Name : brian kibet
# Email : blkagatum@gmail.com
# Date : 21th feb 2023
# File : assignment4.py
#when drawing a diamond
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
D=(b**2)-(4*a*c) # discriminant
print("The value of discriminant is",D)
sol1 = (-b+D**0.5/2*a)
sol2 = (+b-D**0.5/2*a)
print("The roots of this quadraticn equations are",sol1,"and",sol2)