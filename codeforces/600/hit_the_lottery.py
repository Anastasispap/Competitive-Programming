nums = [100, 20, 10, 5, 1]


def main():
    n = int(input())

    k = 0
    for i in nums:
        y = n // i
        k += y
        n = n - i*y
        i += 1
    print(k)




if __name__ == '__main__':
    main()