#Alex Harris
#CS160 9am

def main():

    #Get the user's first sentence
    userSentence = input("enter a sentence: ")
    #get the list of sentences ready
    usersSentences = []
    #add the first sentence to the list
    usersSentences.append(userSentence)

    #while loop that stops when the sentence is empty
    while userSentence != "":
        #get and add another sentence
        userSentence = input("enter a sentence: ")
        usersSentences.append(userSentence)

    #print all the sentences with a space
    print(' '.join(usersSentences))

if __name__ == "__main__":
    main()