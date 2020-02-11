def stringToNumericList(numbers):

    numberList = numbers.split(" ")
    newNumberList = []
    sum = 0
    for i in numberList:
        newNumberList.append(float(i))
    for n in newNumberList:
        sum = sum + newNumberList[n]
    return sum

def main():

    userNumbers = input("Input your numbers separated by a space ")
    sum = stringToNumericList(userNumbers)
    print(sum)

main()