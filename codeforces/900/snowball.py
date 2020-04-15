def main():
    info = input().split()
    w = int(info[0])
    h = int(info[1])
    info = input().split()
    u1 = int(info[0])
    d1 = int(info[1])
    info = input().split()
    u2 = int(info[0])
    d2 = int(info[1])

    while h > 0:
        w += h
        if d1 == h:
            w -= u1
        elif d2 == h:
            w -= u2
        h -= 1

    print(w)


if __name__ == '__main__':
    main()