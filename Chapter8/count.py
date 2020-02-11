#Alex Harris
#CS160 9am

def main():

    #user input and check if the input is a string
    try:
        userNumber = int(input("Please enter an integer: "))
    except ValueError:
        userNumber = int(input("Invalid integer. Please enter an integer: "))

    #set the totals
    numbersTotal = 1
    total = userNumber

    #go until the total is 17
    while total <= 17:
        userNumber = int(input("Please enter an integer: "))
        total += userNumber
        #increment the total of numbers
        numbersTotal += 1
    print("The total is", total, "and", numbersTotal, "numbers were entered.")

if __name__ == "__main__":
    main()