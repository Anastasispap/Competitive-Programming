def main():
    cases = int(input())
    k = 0
    for i in range(cases):
        nums = input().split()
        if nums.count('1') > 1:
            k += 1

    print(k)

if __name__ == '__main__':
    main()