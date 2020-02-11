#Alex Harris
#CS160 9am

def cardInfo(cardNumber):

    #create the deck
    suits = ["c", "s", "h", "d"]
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #get the rank, suit, and value of the card
    cardRank = cardNumber % 13
    value = value[cardRank]
    cardRank = ranks[cardRank]
    cardSuit = cardNumber // 13
    cardSuit = suits[cardSuit]


    return cardRank, cardSuit, value

def main():

    #go through each card and output a value
    for i in range(0, 52):
        cardRank, cardSuit, value = cardInfo(i)
        #Line everything up properly
        print(f"{i:>2} {value:>2} {cardRank:>02}{cardSuit}.gif")

main()