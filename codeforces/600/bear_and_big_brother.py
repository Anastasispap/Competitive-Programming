
def main():
    info = input().split()
    lim = int(info[0])
    bob = int(info[1])

    k = 1
    while lim <= bob:
        lim = lim * 3
        bob = bob * 2
        if lim <= bob:
            k += 1

    print(k)

if __name__ == '__main__':
    main()