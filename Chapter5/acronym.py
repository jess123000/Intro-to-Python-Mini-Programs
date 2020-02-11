#Alex Harris
#CS160 9am

def main():

    #get user's input
    words = input("Please enter your phrase: ")

    #get the acronym
    acronym = ''.join(word[0] for word in words.upper().split())

    #Print the acronym
    print("The acronym is", acronym)

main()

