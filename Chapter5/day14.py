def main():

    word = input("Enter a word: ")
    newWord = ""

    for ch in (word):
        newWord = newWord + chr(ord(ch)+1)

    print(newWord)

main()