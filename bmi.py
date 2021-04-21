#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:04:03 2021

@title BMI (Body Mass Index)

@author: Bahromjon Po'lat
"""


weight = float(input('Enter your weight: '))
height = float(input('Enter your height in meter: '))
index = weight / (height**2)

if index < 18.5 and index > 0:
    print("{:.2f} -> Underweight".format(index))
    
elif (index >= 18.5 and index <= 25):
    print("{:.2f} -> Normal".format(index))

elif (index > 25 and index <= 30):
    print("{:.2f} -> Overweight".format(index))
  
elif (index > 30 and index <= 34.9):
    print(f"{:.2f} -> Obese".format(index))

else:
    print("{:.2f} -> Extremely obese".format(index))
