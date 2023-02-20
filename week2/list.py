#!/usr/bin/env python3
# This is a singe line commet
# Python programme to illustrate
# Name : brian kibet
# Email : blkagatum@gmail.com
# Date : 17th Feb 2023
# File : list.py
name = ["brian","moses","jack","frank","mary"]
#accessing item in a list
print(name)
print(name[-1])















fruits = ["mango","orange","kiwi","lime","lemon","guava","strawberry"]
print(fruits[0:-1])
print(fruits[3])




vegetables =["kales","cabbage","spinach","manangu","broccoli","carrot","sukuma","onions"]

stationery = ["pens","glues","ink","paper","steepler","pounch"]
shoppings = vegetables + stationery
print(shoppings) 
print(shoppings[4])
print("my name is"+name[0]+"and my favourite foood is"+ fruits[2])
for vegetable in vegetables:
 print(vegetable)
 for shopping in shoppings:
    print(shopping)   