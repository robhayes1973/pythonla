#!/usr/bin/env python3

# Dictionary Examples

ages = { 'Robert': 48, 'Vida': 40, 'Gabe': 14 }
print(ages)
print(ages['Robert'])
print(ages['Gabe'])

#Add to Dictionary

ages['Angelica'] = 10
print(ages)

ages['Billy'] = 29
print(ages)

# Delete from Dictionary

del ages['Billy']
print(ages)

ages.pop('Robert')
print(ages)

# Get function

print(ages.get('Vida'))
print(ages.get('Gabe'))

# SHow Dictionary key

print(ages.keys())

# Show Dictionary values

print(ages.values())
