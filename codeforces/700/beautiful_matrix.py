def main():
    row = 0
    col = 0
    for i in range(5):
        zeros = input().split()
        if '1' in zeros:
            row = i
            col = zeros.index('1')
    print(abs(row - 2) + abs(col - 2))


if __name__ == '__main__':
    main()