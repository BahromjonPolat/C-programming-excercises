
"""
Created on Wed Apr 21 14:45:57 2021
@title: Pythagoras Theorem
@author: Bahromjon Po'lat

c^2 = a^2 + b^2

"""

for c in range(1, 100):
    for b in range(c):
        for a in range(b):
            
            if (c ** 2 == (b ** 2 + a ** 2)):
                print(f"({a}, {b}, {c})")

