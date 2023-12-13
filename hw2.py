'''
Niharika Agrawal
CSC 161
Homework 2: Numbers
Find a square root using the secant method
'''

import math

def main():

    #step 1: print introduction
    print("This program calculates the square root of a given number using the secant method.")

    #step 2: prompt user for value a to find square root of a
    A = int(input("What is the number for which you want to calculate the square root? "))

    #step 3: prompt user for number of times to improve the guess
    n = int(input("How many iterations do you want to use? "))

    #step 4: calculate guesses based on above input
    x0 = float(A/5)
    x1 = float(A/10)

    #assign rest of variables
    true = math.sqrt(A)
    aprox = 0
    diff = 0

    #step 5: apply secant method
    for i in range(n):
        aprox = x0 - (x0**2 - A)/(x0 + x1)
        x1 = x0
        x0 = aprox
        diff = abs(true - aprox)

        #step 6 part 1: print table showing guess number
        statement = (str(i+1) + " " + str(float(aprox)) + " " + str(float(diff)))
        print(statement)

        finalA = str(float(A))
        finalG = str(float(aprox))
        finalD = str(float(diff))

    #step 6 part 2: print final calculation
    print("My guess for the square root of " + finalA + " is " + finalG)
    print("The difference between my guess and the real result is " + finalD)

main()
