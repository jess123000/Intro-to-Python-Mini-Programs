def main():

    sentence = input("Please input your sentence: ")
    sentenceSplit = sentence.split(" ")
    size = len(sentenceSplit)
    average = 0
    for i in range(size):
        average = average + len(sentenceSplit[i])
    average = average / size
    print("The average amount of letters is", f"{average:<1.2f}")

main()