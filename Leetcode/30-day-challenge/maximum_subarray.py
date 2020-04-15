def main():
    a = [int(x) for x in input().split()]
    total_max = a[0]
    max_now = a[0]

    for i in range(1, len(a)):
        max_now = max(a[i], max_now + a[i])
        total_max = max(total_max, max_now)
    return total_max

if __name__ == '__main__':
    print(main())