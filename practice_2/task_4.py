# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number 
and calculates the sum of its constituent digits. 
For example, if the user enters the number 3141, 
the program should output the following result: 3 + 1 + 4 + 1 = 9
"""

print("Enter an integer 4-digit number:")
input_number = input()

sum = 0
for digit in str(input_number):
    sum += int(digit)

print("The sum of the constituent digits is: " + str(sum))
