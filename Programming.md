---
layout: default
title: Programming
permalink: /programming/
---
# Programming

As an astronomy student I have spent a fair amount of time programming for classes or for research, but I also often enjoy making silly programs. I primarily know and use Python, though I am certainly happy to learn other languages. This page includes project descriptions and the code for much of what I have written, both serious projects for research or classes, and fun/silly personal projects. 

I don't like generative AI for most things, but coding is one of the few things it can be helpful for. That being said, I prefer to do as much of the programming as possible myself - it both helps keep me sharper and able to explain the code to others when needed. When I do use AI for coding beyond debugging (which it is *usually* pretty good at), I have it explain everything it does in detail so I can both double check its work, and learn myself so I won't need to use it as much in the future. On this page, anywhere I used AI for more than debugging will be described in the project's description. 

## Research Code

### PsycheESE Receiver Reader Script
I wrote this script as part of the PsycheESE Project that was my astrophysics major's capstone. It reads the receiver (simulated seismometer) output files from SeisSol and plots the results. As for how it works, first it loads the file and skips the first 2 rows as they are the header (there are commented out lines to instead only load a portion of the data if desired), it then splits this into the time (the first column of the output file), and the ground velocity in each direction. Adding additional lines of code for the stress outputs is easy, they are indexed 1-6. Then the program scales the time data so that the plots will have seconds rather then number of time steps for the x-axis, and takes the derivative of the ground velocity data to get the ground acceleration. Then the plots are made. 

```python

"""
Created on Sat Apr  4 22:10:59 2026

@author: semmo
"""

import numpy as np
import matplotlib.pyplot as plt

#Load Data
data = np.loadtxt('your_file_path',skiprows=2)
#load first 160000 data points (80 seconds)
#data = np.loadtxt('your_file_path',skiprows=2,max_rows=160000)
#load first 65000 data points
#data = np.loadtxt('your_file_path',skiprows=2,max_rows=65000)
#load first 135000 data points
#data = np.loadtxt('your_file_path',skiprows=2,max_rows=135000)

#Split Data
time = data[:, 0]
vx = data[:, 7]
vy = data[:, 8]
vz = data[:, 9]
dt = 0.0005

#Scale time data
x_scaled = np.arange(len(data)) * dt

#Take derivative of velocity to get acceleration
dxdx = np.gradient(vx)
dydx = np.gradient(vy)
dzdx = np.gradient(vz)

#Plot velocities
#plt.plot(x_scaled, vx, label='Vx')
#plt.plot(x_scaled, vy, label='Vy')
#plt.plot(x_scaled, vz, label='Vz')

#Total Acceleration
ddx = dxdx + dydx + dzdx

#Plot ground accelerations
#plt.plot(x_scaled, dxdx, label='dxdx')
#plt.plot(x_scaled, dydx, label='dydx')
#plt.plot(x_scaled, dzdx, label='dzdx')
```

## Coding for Classes/TAing

### Planetary Atmospheres Lab (AST 111 TA)
This one came from me teaching the Planetary Atmospheres lab for AST 111 my first semester as a TA, nobody was asking for any help while working on the lab and I got a bit bored. So I wrote this script to do all the calculations involved in the lab (and a few more) and then plot the results. It calculates a planets effective temperature based solely on its distance from the Sun, then incorporates first the planet's albedo and then the planet's atmosphere. And yes, as one of my students incredulously pointed out, it does contain dictionaries within a dictionary. 

```python

"""
Created on Sat Nov  1 21:43:02 2025

@author: semmo
"""
#I got bored and made this...
import matplotlib.pyplot as plt
import numpy as np

def run_equations(r, a, tau):
    t_eff = 279 * r**(-0.5)
    t_alb = t_eff * (1 - a)**0.25
    t_atmo = t_alb * (1.5 * tau + 1)**0.25
    return t_eff, t_alb, t_atmo

planets = {
    "Venus Modern":  {"r": 0.72, "a": 0.72, "tau": 64},
    "Earth Modern":  {"r": 1.00, "a": 0.29, "tau": 0.50},
    "Earth Perihelion": {"r": 0.9833, "a": 0.29, "tau": 0.50},
    "Earth Aphelion": {"r": 1.0167, "a": 0.29, "tau": 0.50},
    "Mars Modern":   {"r": 1.52, "a": 0.16, "tau": 0.077},
    "Venus Ancient": {"r": 0.72, "a": 0.50, "tau": 1.00},
    "Earth Ancient": {"r": 1.00, "a": 0.50, "tau": 1.00},
    "Mars Ancient":  {"r": 1.52, "a": 0.50, "tau": 1.00},
    "Jungle Venus":  {"r": 0.72, "a": 0.72, "tau": 0.50},
    "Mars Terraformed": {"r": 1.52, "a": 0.16, "tau": 0.50}
}

eff_temps, alb_temps, atmo_temps = {}, {}, {}
for name, planet in planets.items():
    eff, alb, atmo = run_equations(planet["r"], planet["a"], planet["tau"])
    eff_temps[name] = eff
    alb_temps[name] = alb
    atmo_temps[name] = atmo

Mercury_r = 0.39
Mercury_a = 0.10
Mercury_tau = 0

merc_eff, merc_alb, merc_atmo = run_equations(Mercury_r, Mercury_a, Mercury_tau)
merc_eff *= 2**0.25
merc_alb *= 2**0.25
merc_atmo = merc_alb

eff_temps["Mercury"] = merc_eff
alb_temps["Mercury"] = merc_alb
atmo_temps["Mercury"] = merc_atmo

eff_temps["Young Sun Earth"] = eff_temps["Earth Ancient"] * (.7**(1/4))
alb_temps["Young Sun Earth"] = alb_temps["Earth Ancient"] * (.7**(1/4))
atmo_temps["Young Sun Earth"] = atmo_temps["Earth Ancient"] * (.7**(1/4))

for name in eff_temps:
    print(f"{name}:")
    print(f"  Effective temperature: {eff_temps[name]:.1f} K")
    print(f"  Albedo temperature: {alb_temps[name]:.1f} K")
    print(f"  Atmospheric temperature: {atmo_temps[name]:.1f} K\n")
print("Note: Mercury has no (substantial) atmosphere. (and calculating its atmospheric temperature is not required for this lab)")

names = list(eff_temps.keys())
eff_values = [eff_temps[n] for n in names]
alb_values = [alb_temps[n] for n in names]
atmo_values = [atmo_temps[n] for n in names]

x = range(len(names))
width = 0.25

plt.figure(figsize=(11, 6))
plt.bar([i - width for i in x], eff_values, width, label='Effective Temp', alpha=0.8)
plt.bar(x, alb_values, width, label='Albedo Temp', alpha=0.8)
plt.bar([i + width for i in x], atmo_values, width, label='Atmospheric Temp', alpha=0.8)
plt.xticks(x, names, rotation=30, ha='right')
plt.yticks(np.arange(0,776,50))
plt.ylabel("Temperature (K)")
#plt.yscale("log")
plt.title("Planet Temperature Comparison")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
```

## Silly Code and Games

### matplotlib tictactoe
I had this idea after chatting with a friend before a research group meeting, instead of using something like pygame (or a non-python based game engine) it should be possible to use matplotlib to show the board states of turn-based games. In simple terms, it is a simple game of tic tac toe, with options to play against a second player or the computer (which will often insult you when it makes a move), a wide variety options for player color and symbol (instead of just "x" and "o"), and it displays the board using matplotlib figures. The computer opponent has 3 different difficulty levels and several diefferent "personalities". Of the different difficulty levels: level 1 just selects random moves until it finds a valid one, level 3 always chooses the "optimal" move, and level 2 has several different modes that are randomly selected when the player selects that difficulty - including 50/50 between random move and optimal move orprioritizing the edges (but not corners). It was a lot of fun coming up with the options for the computer opponent to say - many are references to memes or my favorite fictional universes. Of the completed projects on this page, this is definitely the one that took the longest - and I still sometimes add more options for what the computer opponent can say when I think of them. This project also gave me the fun piece of knowledge that there is a rickroll python package. 

Generative AI (ChatGPT - I can't remember which version, but based on the when this was made it was probably 5.0 and/or 5.1) was used to figure out the logic for the level 3 computer opponent (I then modified this logic for the level 2 computer opponent), as well as figuring out how to allow for LaTeX symbols to be valid options for the player(s).

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

<!--### Currently Unamed Space Game
There is no code for this yet as it is primarily juat a concept and I have a couple different versions of it in my head as possibilities, but the idea is for a game (either turn-based or real-time) that has you commanding a space ship (or maybe several) in sci-fi style space battles albeit with (more or less) real-world physics. The plan would be to use vectors - in Python terms a list of 3 numbers - and vector operations to control movement. Additonally, the player wouldn't "move" from the perspective of the game, I think it would be easier to program if the player is fixed at the center of a spherical space and their "acceleration" and "velocity" were just added to other ships when they move. I will add more to this when I eventually get around to starting making it. -->
