#!/usr/bin/env python3

# The not operation

name = ''
print(not name)

if not name:
    print('No name was given')


# The or operation

first = ''
last = 'Hayes'

if first or last:
    print('The user has a  first or last name')

first = ''
last = ''

if first or last:
    print('The user has a first or last name')
else:
    print('The user has not specified a first or last name')


first = 'Robert'
last = ''

if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last Name: {last}")


first = 'Robert'
last = 'hayes'

if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last Name: {last}")

first = ''
last = 'Hayes'

if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last Name: {last}")
