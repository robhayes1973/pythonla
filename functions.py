#!/usr/bin/env python3

def hello_world():
    print('hello world')

print(hello_world())
hello_world()


def print_name(name):
    print(f"Name is {name}")

print_name("Robert")

def add_two(num):
    return num + 2

result = add_two(2)
print(result)

def add(num1, num2, num3):
    return num1 + num2 + num3

result = add(1, 5, 7)
print(result)