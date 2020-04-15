def main():
    info = input().split()
    num1 = int(info[0])
    num2 = int(info[1])

    for i in range(num2):
        if num1 % 10 == 0:
            num1 = int(num1 / 10)
        else:
            num1 = num1 - 1

    print(num1)


if __name__ == '__main__':
    main()
