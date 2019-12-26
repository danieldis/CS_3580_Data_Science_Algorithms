#Daniel Salmond
#CS 3580 
# Assignment #1 

#Part 0
print("Daniel I Salmond")


#Part 1
import math
from math import *

temp = str(math.factorial(100))
totalCount = 0
for c in temp:
    totalCount = totalCount + int(c)
    
print("Part1: ", totalCount),

#Part 2

counter = 2
a = 0
b = 1
c = 1

while len(str(c)) < 1000:
    counter = counter + 1
    a = b
    b = c
    c = a + b

print("Part2: ", counter),


#Part 3

def palindromeCheck(n):
    forward = str(n)
    reverse = ""
    for i in range (len(forward) - 1, -1, -1):
        reverse += forward[i]
    return reverse == forward
def biggestPalindrome():
    palindrome = -1
    for i in range (999, 99, -1):
        for j in range (i, 99, -1):
            if palindromeCheck(i * j) and i * j > palindrome:
                palindrome = i * j
    return palindrome;
print("Part3: ", biggestPalindrome()),











