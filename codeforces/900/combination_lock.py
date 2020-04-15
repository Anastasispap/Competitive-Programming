def main():
    disks = int(input())
    original = input()
    combination = input()

    total = 0
    for i in range(disks):
        option1 = abs(int(original[i]) - int(combination[i]))
        option2 = abs((min(int(original[i]), int(combination[i])) + 10) - max(int(original[i]), int(combination[i])))
        total += min(option1, option2)
    print(total)


if __name__ == '__main__':
    main()