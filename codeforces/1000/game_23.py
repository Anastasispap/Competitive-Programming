def main():
    m, n = [int(x) for x in input().split()]

    if n / m % 2 != 0 or n/m % 3 != 0:
        return -1
    else:
        num = 3
        x = n//m
        steps = 0

        while x != 1:
            if x % num != 0:
                if num == 3:
                    num = 2
                else:
                    num = 3
            else:
                x = x//num
                steps += 1
    print(steps)



if __name__ == '__main__':
    main()