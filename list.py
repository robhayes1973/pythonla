#!/usr/bin/env python3

#Working with lists

my_list = [1, 2, 3, 4, 5]
print(my_list[3])

#Slicing Lists

print(my_list[0:2])
print(my_list[1:])
print(my_list[0::1])
print(my_list[:4])
print(my_list[0::2])

#len function
print(len(my_list))

#Modifying a list
my_list[0] = 'a'
print(my_list)

my_list.append(6)
my_list.append(7)

print(my_list)

my_list + [8, 9 ,10]
print(my_list)

my_list += [8, 9, 10]
print(my_list)

#Slicing sets

my_list[1:3] = ['b', 'c']
print(my_list)

my_list[3:5] = ['d', 'e', 'f']
print(my_list)

#Removing from list using empty space

my_list[6:] = []
print(my_list)

#Removing from a list using hte .remove

my_list.remove('b')
print(my_list)

my_list.pop(0)
print(my_list)

my_list.pop(1)
print(my_list)

my_list.pop(2)
print(my_list)
