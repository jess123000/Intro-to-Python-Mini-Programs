#Alex Harris
#CS160 9am

def validDate(userDate) -> bool:

    #Split the into a list for easy access
    userDateList = userDate.split("/")
    intUserDate = []

    #change the list to numbers
    for i in userDateList:
        intUserDate.append(int(i))

    #Check if the date is valid in several methods
    if intUserDate[0] > 12:
        return False
    elif intUserDate[0] < 1:
        return False
    elif intUserDate[0] == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if intUserDate[1] != 31:
            return False
    elif intUserDate[0] == 4 or 6 or 9 or 11:
        if intUserDate[1] != 30:
            return False
    elif intUserDate[0] == 2:
        if intUserDate[1] != 28 or 29:
            return False
    else:
        return True

#-----------------------------------------------------------------

def main():

    #get the user's date
    userDate = input("Please enter your date in the form month/day/year: ")

    #Print the results of the function
    if validDate(userDate):
        print("Your date is valid")
    else:
        print("Your date is not valid")

if __name__ == "__main__":
    main()