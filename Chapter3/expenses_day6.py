def main():
    miles = eval(input("How many miles have you driven this month? "))
    mpg = eval(input("What is your average MPG? "))
    for i in range (41):
        costPerGallon = 2 + .05 * i
        gallons = miles / mpg
        monthlyCost = gallons * costPerGallon
        print(monthlyCost)

main()