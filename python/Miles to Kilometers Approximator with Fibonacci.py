# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 09:26:51 2025

@author: semmo
"""

import matplotlib.pyplot as plt

def fibonacci(n):
    a = 0
    b = 1
    while a < n:
        a, b = b, a + b
    return b

def percent_error(calc,actual):
    error = (abs(calc-actual) / actual) * 100
    return error

miles = int(input("Input an integer number of miles:\n"))

calc_kilometers = fibonacci(miles)
error = percent_error(calc_kilometers,(miles * 1.60934))
print(f'Fibonacci estimate: {calc_kilometers}km')
print(f'Actual value: {miles * 1.60934}km')
print(f'{error}% error')