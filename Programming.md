---
layout: default
title: Programming
permalink: /programming/
---
# Programming

As an astronomy student I have spent a fair amount of time programming for classes or for research, but I also often enjoy making silly programs. I primarily know and use Python, though I am certainly happy to learn other languages. This page includes project descriptions and the code for much of what I have written, both serious class or research projects, and fun personal projects. 

While I do not like AI for cheating on schoolwork/education or for doing art, it is sometimes useful for programming. I primarily use it for bugfixing as my most common errors tend to be typos and forgotten function names - which it can find easily. That being said, I don't trust AI to do all coding for me, especially not the free models I have access to. I prefer to do as much of the programming as possible myself - it both helps keep me sharper and able to explain the code to others when needed. When I do use AI for coding beyond debugging, I have it explain everything it does in detail so I can both double check its work, and learn myself so I won't need to use it as much in the future. On this page, anywhere I used AI for more the debugging will be listed in the project's description. 

## Research Code

### PsycheESE Receiver Reader Script


## Coding for Classes/TAing

### Planetary Atmospheres Lab (AST 111 TA)


## Silly Code and Games

### matplotlib tictactoe
I had this idea after chatting with a friend before a research group meeting. In simple terms, it is a simple game of tic tac toe, with options to play against a second player or the computer (which will often insult you when it makes a move), a wide variety options for player color and symbol (instead of just "x" and "o"), and it displays the board using matplotlib figures. The computer opponent has 3 different difficulty levels and several diefferent "personalities". Of the different difficulty levels: level 1 just selects random moves until it finds a valid one, level 3 always chooses the "optimal" move, and level 2 has several different modes that are randomly selected when the player selects that difficulty - including 50/50 between random move and optimal move orprioritizing the edges (but not corners). Of the completed projects on this page, this is definitely the one that took the longest - and I still sometimes add more options for what the computer opponent can say when I think of them. 

For the sake of keeping this page readable, I have put the code onto a separate page, linked <a href="https://semmons98.github.io/programming/matplotlib_tictactoe/" target="_blank">here</a>.

### Golden Ratio Distance Conversion
This was based on a meme I saw online about how the conversion between miles and kilometers was close to the Golden Ratio. The code takes an input integer number of miles from the user, then finds the next fibonacci number after that integer and prints it as the estimated number of kilometers. It then also calculates the actual unit conversion, printing that and the percent error. Though this was just something I did for fun, in the future I may comeback and add the ability to convert the other way (kilometers to miles). 

```python
"""
Created on Wed Dec  3 09:26:51 2025

@author: semmo
"""

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

### Currently Unamed Space Game

<!--
Include tic-tac-toe, any school or research python scripts that seem appropriate/good enough to share, etc. Include something about the space game I am planning. Include possible additions to the current programs (other games or modes that would work well with tic-tac-toe, using the actual Fibonacci Sequence for the Golden Ratio conversion, etc.
-->
