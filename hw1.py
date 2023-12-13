'''
File: hw1.py
Homework 1 assignemnt
Niharika Agrawal
CSC 161
'''

from turtle import *

def main():
    print("This program drawes a snowflake")
    color("blue")

    n = int(input("How many arms to draw? "))

    for i in range(n):
        forward(100)
        backward(100)
        left(360/n)
    done()

main()
#you can also delete the above line of code and directly input main into
#the shell, this just makes it easier. both ways work.
