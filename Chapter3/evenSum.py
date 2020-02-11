#Alex Harris
#CS 160 9am

def main():
    #user input
    int1, int2 = eval(input("Enter the two even numbers separated by a coma with the smaller number first: "))
    evenSum = 0
    #calculate how many times the loop needs to run
    for i in range(int1, int2+1, 2):
        evenSum = evenSum + i
    print("The sum of the evens between", int1, "and", int2, "is", evenSum)

main()