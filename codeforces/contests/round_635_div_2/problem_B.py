def main():
    cc = int(input())

    for i in range(cc):
        h, n, m = [int(j) for j in input().split()]

        if h > 20:
            for k in range(n):
                h = h//2 + 10

        if h - 10*m <= 0:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()