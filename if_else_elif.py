#!/usr/bin/env python3

#Demo if/else/elif conditions

my_list = [1, 2, 3, 4, 5]

if 2 in my_list:
    print('This is a true staement')
else:
    print('This is a false statement')

if 6 in my_list:
    print('This is a true staement')
else:
    print('This is a false statement')

name = 'Robert'

if len(name) >= 7:
    print('This is a long name')
elif len(name) == 6:
    print('Name is 6 characters long')
elif len(name) >= 4:
    print('Name is more than 4 characters long')
else:
    print('Name is short')
