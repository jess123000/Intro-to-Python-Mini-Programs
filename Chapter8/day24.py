def main():

    weight = 0
    totalWeight = 0
    total = 0
    while weight != "":
        weight = int(input("What was the weight of the grade as an integer? "))
        grade = float(input("What did you get on it as a decimal? "))
        if weight != "":
            total = total + weight * grade
            totalWeight += weight
        else:
            weight = 100 - totalWeight
            total = total + weight * grade
    print("Your final grade is", total)

if __name__ == "__main__":
    main()