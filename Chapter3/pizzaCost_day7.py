import math

def main():
    price, diameter = eval(input("Please enter the price of the pizza and it's diameter separated by a comma: "))
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    pricePerInch = price / area
    print("The price per square inch of your pizza is $", end="")
    print(round(pricePerInch, 2))

main()