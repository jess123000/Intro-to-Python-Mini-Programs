def main():
    chirps = eval(input("Please enter the the number of chirps per minute: "))
    fahrenheit = 10 / 9 * chirps + 280 / 9
    print("The temperature in Fahrenheit is ", fahrenheit, "degrees.")

main()