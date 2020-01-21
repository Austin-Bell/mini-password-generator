#!/bin/python3
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'

print("==========Password Generator==========")

length = input("Password length: ")
length = int(length)

numPasswords = input("Number of passwords: ")
numPasswords = int(numPasswords)


print('\nhere are your passwords:')

for pwd in range(numPasswords):
  # variable to store password
  password = ''
  for c in range(length):
	  
	# Add character to specified by number in range
	  password += random.choice(chars)
  
  # print characters from chars
  print(password)

print("===============================")
