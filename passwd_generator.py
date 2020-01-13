#!/bin/python3
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'

length = input()
length = int(length)
for p in range(3):
  # variable to store password
  password = ''
  for c in range(length):
    # Add character to specified by number in range
    password += random.choice(chars)
  
  # print characters from chars
  print(password)
