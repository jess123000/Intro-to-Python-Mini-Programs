#Alex Harris
#CS160 9am

def main():

    #Ask the users temperature
    temperature = float(input("Please enter your temperature: "))

    #Evaluate if they have a temperature
    if temperature >= 99:
        print("You have a fever")
    else:
        print("You do not have a fever")

main()