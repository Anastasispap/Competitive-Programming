def main():
    _ = int(input())
    values = [int(x) for x in input().split()]
    values = sorted(values)

    max_coins = 1
    total = values[0]
    values.remove(total)
    for val in values:
        if total <= sum(values):
            max_coins += 1
            total += val
            values.remove(val)

    print(max_coins)


if __name__ == '__main__':
    main()