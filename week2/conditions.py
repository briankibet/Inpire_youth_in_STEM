#!/usr/bin/env python3
# This is a singe line commet
# Python programme to illustrate
# Name : brian kibet
# Email : blkagatum@gmail.com
# Date : 17th Feb 2023
# File : conditions.py
age = 16

gender = "male"

if (age < 18):
    print("you are still young")
else:
    print("you shouid get an id")


#compound / multiple conditions

if((age >30) & (gender == 'male')):
    print("you qualify for a loan")
else:
    print("No loan for you")
fav_color = "grey"
age =22
if (fav_color == 'grey') | ( age <=20):
   print("Happy birthday to you") 
else:
    print("No happy birthday present  for you")