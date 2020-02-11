#Alex Harris
#CS160 9am

def main():

    #prep the tries
    totalTries = 0

    while True:
        #get user's numbers
        userNumber = float(input("Enter a number between 1 and 10: "))
        #accumlate the totalTries
        totalTries += 1
        #if the user number is between 1 and 10 exit the loop
        if 1 <= userNumber <= 10:
            break

    #check how many times and output times
    if totalTries == 1:
        print("It took you 1 time to enter a valid value.")
    else:
        print(f"it took you {totalTries} times to enter a valid value.")

if __name__ == "__main__":
    main()