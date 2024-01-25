""" A program that gives the user a safe password through randomization """

"""Password should be longer than 12 characters, should contain numerals, letters, capitals, and escape characters"""

import re 
import random

numerals = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
escape = ['!','@','#','%','&','*','=',]

first_list = []
start = 0
while start < 3:
    first_list.append(random.choice(numerals))
    first_list.append(random.choice(letters))
    first_list.append(random.choice(capitals))
    first_list.append(random.choice(escape))
    start = start + 1    

random.shuffle(first_list)

for x in first_list:
    print(x,end='')
print("\n")
