#!/usr/bin/env python3
# This is a singe line commet
# Python programme to illustrate
# Name : brian kibet
# Email : blkagatum@gmail.com
# Date : 21th feb 2023
# File : assignment3.py
#when drawing pascals triangle
x=[]
for i in range(n):
    x.append([])
    x[i].append(1)
    for j in range(1,i):
        x[i].append(x[i-1][j-1]+x[i-1][j])
    if(n!=0):
        x[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(x[i][j]),end=" ",sep=" ")
    print()