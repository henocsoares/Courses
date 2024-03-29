'''
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two
decimal places.
'''

import math

integer = 0

while integer <= 500:
  integer = int(input("Enter an integer higher than 500: "))

sqrt = math.sqrt(integer)

print(f"The square root of {integer} is: {sqrt:.2f}!")
