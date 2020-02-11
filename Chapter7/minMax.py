def main():

    #Create the list of user numbers
    numbers = input("Please input your integers: ")
    numbersList = numbers.split(" ")
    numbersListNew = []
    for i in numbersList:
        numbersListNew.append(int(i))
    max = numbersListNew[0]
    min = numbersListNew[0]
    for item in numbersListNew:
        if numbersListNew[item - 1] >= max:
            max = numbersListNew[item - 1]
        if numbersListNew[item - 1] <= min:
            min = numbersListNew[item - 1]
    print(f"The maximum value is {max}, and the minimum value is {min}")

if __name__ == "__main__":
    main()