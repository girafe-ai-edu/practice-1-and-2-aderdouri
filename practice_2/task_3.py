# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. 
The user must enter their height and weight, 
after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""

print("Enter your weight in kilograms:")
weight = input()
print("Enter your height in meters:")
height = input()

print("Your BMI is: {}".format(float(weight) / (float(height) ** 2)))


