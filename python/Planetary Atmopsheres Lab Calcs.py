# -*- coding: utf-8 -*-
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