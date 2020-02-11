#Alex Harris
#CS 160 9am

def main():
    times = int(input("Enter an integer: "))
    result = 0
    for i in range(times):
        result = result + 1/(i+1)
    print("The sum of the harmonic series with", times,"terms is", result)

main()