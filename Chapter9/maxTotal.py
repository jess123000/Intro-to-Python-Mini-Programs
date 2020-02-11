#Alex Harris
#CS160 9am

def main():

    userNumber = int(input("enter a number: "))
    total = userNumber
    totalTimes = 1
    while totalTimes < 5:
        userNumber = int(input("enter a number: "))
        total += userNumber
        totalTimes += 1
        if total > 21:
            break
    print(f"the total is {total}")

if __name__ =="__main__":
    main()