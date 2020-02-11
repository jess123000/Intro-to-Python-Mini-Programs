#Alex Harris
#CS160 9am

from math import *

def squareAndRoot(number):

    square = number ** 2
    squareRoot = sqrt(number)
    return square, squareRoot

def main():

    number = int(input("Please enter an integer: "))
    square, squareRoot = squareAndRoot(number)
    print("The number squared is", square, "and the number's square root is", squareRoot)

main()