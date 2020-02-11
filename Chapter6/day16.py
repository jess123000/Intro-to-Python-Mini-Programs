def song(animal, sound):

    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a", animal)
    print("E-I-E-I-O")
    print("With a", sound + "-" + sound, "here")
    print("And a", sound + "-" + sound, "there")
    print("Here a", sound, "there a", sound)
    print("Everywhere a", sound + "-" + sound)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()

def main():

    animals = ["snake", "cow", "pig", "dog", "cat"]
    sounds = ["hiss", "moo", "oink", "bark", "meow"]

    for i in range(0, 5):
        song(animals[i], sounds[i])

main()