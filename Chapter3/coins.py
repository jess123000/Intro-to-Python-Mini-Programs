#Alex Harris
#CS 160 9am

def main():
    #get user input
    numberOfCoins = int(input("Please the amount of cents you have between 0 and 99 "))
    #reassgin for later use of this number
    startingNumber = numberOfCoins
    #calculate number of quarters needed
    numberOfQuarters = numberOfCoins // 25
    #subtract the coins we just took out in quarters
    numberOfCoins = numberOfCoins - 25 * numberOfQuarters
    #calculate number of dimes
    numberOfDimes = numberOfCoins // 10
    #subtract again
    numberOfCoins = numberOfCoins - 10 * numberOfDimes
    #calculate nickels
    numberOfNickels = numberOfCoins // 5
    #subtarct again
    numberOfCoins = numberOfCoins - 5 * numberOfNickels
    #calculate pennies
    numberOfPennies = numberOfCoins
    #output of all coins
    print(startingNumber, "of coins would give you", numberOfQuarters, "quarters", numberOfDimes, "dimes",
          #wrap line for nicer code
          numberOfNickels, "nickels and", numberOfPennies, "pennies.")

main()