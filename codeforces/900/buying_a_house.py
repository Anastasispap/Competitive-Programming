def main():
    info = input().split()
    house_prices = [int(x) for x in input().split()]

    n = int(info[0])
    m = int(info[1])
    k = int(info[2])
    min_distance = 10**10
    for i in range(len(house_prices)):
        if house_prices[i] < k and house_prices[i] != 0:
            distance = abs(i+1-m)*10
            if min_distance > distance:
                min_distance = distance

    print(min_distance)

if __name__ == '__main__':
    main()