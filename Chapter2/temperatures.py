#Alex Harris
#CS 160 9 a.m.

def main():
    #for loop of celsius numbers
    for i in range (11):
        #calculate fahrenheit
        c = i * 10
        f = c * 9 / 5 + 32
        #print the celsius then put a comma next to the number to make it look nicer
        print(c, end="")
        print(",", f)

main()