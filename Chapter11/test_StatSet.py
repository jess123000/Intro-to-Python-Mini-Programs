#Alex Harris
#CS160 9am

#you might have to change this import statement for it to work on your end
from Chapter11.StatSet import *

def main():
    #create the instance of the class
    nums = StatSet()
    number = input("Enter a number: ")
    #Keep adding numbers until nothing is typed
    while number != '':
        x = float(number)
        nums.addNumber(x)
        number = input("Enter a number (<Enter> to quit): ")

    #output all the testings of the class
    print("Numbers Entered:", nums.count())
    print("Mean:", nums.mean())
    print("Median:", nums.median())
    print("Standard Deviation:", nums.stdDev())
    print("Max:", nums.max())
    print("Min:", nums.min())

if __name__ == "__main__":
    main()