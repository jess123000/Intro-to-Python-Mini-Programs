def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** .5), 2):
            if n % i == 0:
                return False
        return True

def main():
    userInt = int(input("Enter an integer to test: "))
    print(isPrime(userInt))

if __name__ == "__main__":
    main()