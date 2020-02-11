#Alex Harris
#CS160 9am

def removeBracket(user):

    #check if the first character in the string is a bracket
    for c in user:
        if c == "[":
            #turn the string into a list for mutability
            newString = list(user)

            #remove the brackets
            newString.remove("[")
            newString.remove("]")

            #join the string back together
            newString = "".join(newString)
            return newString
        else:
            return user

#------------------------------------------------------------------

def main():

    #get the user's input
    userInput = input("Input your string: ")

    #call the function
    newString = removeBracket(userInput)

    #print the new string
    print(newString)

if __name__ == "__main__":
    main()