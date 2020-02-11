#Alex Harris
#CS160 9am

def allPositive(numbers: float) -> bool:

    #Split the input into a list
    numberList = numbers.split(" ")
    #Prepare the new list
    newNumberList = []

    #change the numbers to floats and add them to the new list
    for i in numberList:
        newNumberList.append(float(i))

    #Evaluate each number
    for x in newNumberList:
        if x < 0:
            return False
    return True

#-------------------------------------------------------------------

def main():

    #Get the users numbers
    userNumbers = input("Please enter your non-zero numbers separated by a space: ")
    #call the function and send the numbers
    if allPositive(userNumbers):
        print("All positive")
    else:
        print("Some non-positive")

if __name__ == '__main__':
    main()