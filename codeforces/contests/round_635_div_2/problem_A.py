def main():
    cc = int(input())

    for i in range(cc):
        a, b, c, d = [int(x) for x in input().split()]

        print("{} {} {}".format(b, c, c))


if __name__ == '__main__':
    main()