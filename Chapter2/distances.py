#Alex Harris
#CS 160 9 a.m.

def main():
    #for loop of kilometers numbers
    for i in range (21):
        km = i * 5
        #calculate miles
        mi = km * .621371
        #print the miles then put a comma next to the number to make it look nicer
        print(km, end="")
        print(",", mi)

main()