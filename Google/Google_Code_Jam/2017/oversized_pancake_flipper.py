def main():
    cases = int(input())

    for i in range(1, cases+1):
        info = input().split()
        row = info[0]
        K = info[1]
        if len(row) == row.count('+'):
            num = 0


        print("Case #{}: {}".format(i, num))


if __name__ == '__main__':
    main()