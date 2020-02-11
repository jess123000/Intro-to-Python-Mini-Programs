#Alex Harris
#CS 160 9am

def main():
    #get user input
    int1 = int(input("What is the first even integer? "))
    int2 = int(input("What is the second even integer? "))
    evenNumbers = (int2 - int1) / 2 + 1
    print("There are", int(evenNumbers), "even numbers.")


main()