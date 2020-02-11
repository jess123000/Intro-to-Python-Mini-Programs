#Alex Harris
#CS 160 9 a.m.

def main():
    #get the first number
    x = eval(input("enter #1: "))
    #get the second number
    y = eval(input("enter #2: "))
    #get the third number
    z = eval(input("enter #3: "))
    #calculate the average
    average = (x + y + z) / 3
    #output the average
    print("the average of", x, y, z, "is", average)

main()