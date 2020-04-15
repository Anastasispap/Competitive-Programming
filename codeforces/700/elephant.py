steps = [5, 4, 3, 2, 1]


def main():
    coord = int(input())
    k = 0
    for i in steps:
        y = coord // i
        k += y
        coord = coord - i * y
        i += 1
    print(k)


if __name__ == '__main__':
    main()