def main():

    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    userInput = int(input("Enter your number: "))
    userInput = userInput - 1
    userRank = userInput % 13
    userSuit = userInput // 13

    print("Your card is the", ranks[userRank], "of", suits[userSuit])

main()