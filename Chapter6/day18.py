def sumN(terms: int) -> int:

    sumOfTerms = 0
    for i in range(terms):
        sumOfTerms = sumOfTerms + (i + 1)
    return sumOfTerms

def sumNCubed(terms: int) -> int:

    sumOfNumsCubed = 0
    for i in range(terms):
        sumOfNumsCubed = sumOfNumsCubed + (i + 1) ** 3
    return sumOfNumsCubed

def altSumNSquared(terms: int) -> int:

    sumSquared = 0
    for i in range(terms):
        sumSquared = sumSquared + ((i + 1) ** 2) * (-1) ** (i)
    return sumSquared

def sumOfSums(terms: int) -> int:

    sumOfSums = 0
    equation = 0
    for i in range(terms):
        for n in range(i + 1):
            equation += n
        sumOfSums += equation
        equation = 0
    return sumOfSums

def main():

    userTerms = int(input("Please input the number of terms you would like: "))

    sumOfNums = sumN(userTerms)
    sumOfNumsCubed = sumNCubed(userTerms)
    sumSqaured = altSumNSquared(userTerms)
    sumOfSumOfNums = sumOfSums(userTerms)

    print(f"the sum of the number of terms is {sumOfNums}, the sum of the number of terms cubed is {sumOfNumsCubed},"
          f"the alternating sum of the squares is {sumSqaured}, and the sum of the sum of the terms is {sumOfSumOfNums}")

main()