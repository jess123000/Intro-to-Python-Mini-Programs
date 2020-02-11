def main():
    times = int(input("How many times would you like to go through the program: "))
    result = 0
    for i in range(1, times*2, 4):
        result = result + 4 /(i)
        result = result - 4 / (i+2)
    print("The sum with", times,"terms is", result)

main()