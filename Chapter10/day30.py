from random import randrange

def main():

    games = int(input("How many games would you like to play? "))
    average = 0

    for i in range(games):
        cherries = 10
        spins = 0

        while cherries > 0:
            move = randrange(1, 8)
            spins += 1
            if move == 1:
                cherries -= 1
            elif move == 2:
                cherries -= 2
            elif move == 3:
                cherries -= 3
            elif move == 4:
                cherries -= 4
            elif (move == 5 or move == 6) and cherries <= 8:
                cherries += 2
            elif (move == 5 or  move == 6) and (cherries == 9 or cherries == 10):
                cherries = 10
            elif move == 7:
                cherries = 10
            # if cherries > 0:
            #     if move == 1 or move == 2 or move == 3 or move == 4:
            #         print(f"Spun {move}, cherries left: {cherries}.")
            #     elif move == 5:
            #         print(f"Spun Dog, cherries left: {cherries}.")
            #     elif move == 6:
            #         print(f"Spun Bird, cherries left: {cherries}.")
            #     elif move == 7:
            #         print(f"Spun Spill, cherries left: {cherries}.")
            # elif cherries <= 0:
            #     if move == 1 or move == 2 or move == 3 or move == 4:
            #         print(f"Spun {move}, cherries left: 0.")
            #     elif move == 5:
            #         print(f"Spun Dog, cherries left: 0.")
            #     elif move == 6:
            #         print(f"Spun Bird, cherries left: 0.")
            #     elif move == 7:
            #         print(f"Spun Spill, cherries left: 0.")

        average += spins

    average /= games
    print(average)

if __name__ == "__main__":
    main()