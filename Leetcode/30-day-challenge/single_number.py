def main():
    nums = [int(x) for x in input().split()]
    for num in nums:
        if nums.count(num) == 1:
            print(num)

if __name__ == '__main__':
    main()