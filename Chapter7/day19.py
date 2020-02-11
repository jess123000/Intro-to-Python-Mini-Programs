def hasThe(userInput) -> bool:

    userInput.lower()
    userList = userInput.split()
    for item in userList:
        if item == 'the':
            return True
    return False

#-----------------------------

def main():

    userInput = input("Please enter your string: ")
    if hasThe(userInput):
        print("This statement has the in it")
    else:
        print("This statement does not have the in it")

if __name__ == '__main__':
    main()