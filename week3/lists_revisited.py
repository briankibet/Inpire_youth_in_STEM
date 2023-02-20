#!/usr/bin/env python3
# This is a singe line commet
# Python programme to illustrate
# Name : brian kibet
# Email : blkagatum@gmail.com
# Date : 20th Feb 2023
# File : lists_revisited
myfavouritefruits =["banana","apple","mango","lime","avocando"]
for fruit in myfavouritefruits:
    print(fruit)
my_favourite_fruit = ["banana","apple","mango","lime","avocando"]
for fruit in my_favourite_fruit:
    print(len(fruit))
friends = ["levin","kevin","joash","dennis","brian"]
friends[0] = "mary"
print(friends)
print("------------------------------")
new_friends = friends.copy()
print(new_friends)
new_friends.sort()
print(new_friends)
new_friends.pop()
print(new_friends)