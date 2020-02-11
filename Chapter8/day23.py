def main():

    n = 1
    m = 0
    for a in range(1, 10000):
        i = a
        while i != 1:
            if i % 2 == 0:
                i /= 2
            else:
                i = i * 3 + 1
            n += 1
        if n >= m:
            m = n
    print(m)

if __name__ == "__main__":
    main()