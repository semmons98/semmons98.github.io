---
layout: default
title: Programming
permalink: /programming/
---
# Programming

As an astronomy student I have spent a fair amount of time programming for classes or for research, but I also often enjoy making silly programs. I primarily know and use Python, though I am certainly happy to learn more. This page includes project descriptions and the code for much of what I have written, both serious class or research projects, and fun personal projects. 

## Research Code

### PsycheESE Receiver Reader Script


## Coding for Classes

### Planetary Atmospheres Lab (AST 111 TA)


## Silly Code and Games

### matplotlib tictactoe



### Golden Ratio Distance Conversion

```python
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
```

<!--
Include tic-tac-toe, fibonnacci, any school or research python scripts that seem appropriate/good enough to share. Include something about the space game I am planning. Include possible additions to the current programs (other games or modes that would work well with tic-tac-toe, using the actual Fibonacci Sequence for the Golden Ratio conversion, etc.
-->
