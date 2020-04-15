def main():
    cc = int(input())

    for i in range(cc):
        candies = int(input())
        if candies == 1 or candies == 2:
            print(0)
            continue
        if candies % 2 == 0:
            candies -= 1
        print(candies//2)


if __name__ == '__main__':
    main()
