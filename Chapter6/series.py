#Alex Harris
#CS160 9am

def series(terms):

    sum = 0
    #calculate the sum of the number of terms
    for i in range(1, terms + 1):
        sum = sum + i / (i + 1)

    return sum

def main():

    #get user input and call the series function
    terms = int(input("Please enter the number of terms you want: "))
    sum = series(terms)
    print(sum)

main()