#Alex Harris
#CS160 9am

def main():

    #get user's name and make it all lowercase
    name = input("Please enter your name: ")
    name = name.lower()

    #initialize number
    number = 0
    #go through each letter of the name
    for ch in name:
        #add the letter number to the total
        number = number + (ord(ch) - 96)

    print("your number is", number)

main()