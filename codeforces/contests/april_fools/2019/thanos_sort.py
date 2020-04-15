def main():
    length = int(input())
    nums = [int(x) for x in input().split()]

    while sorted(nums) != nums:
        nums.pop()
        reversed(nums)
        nums.pop()
        reversed(nums)

    print(len(nums))

if __name__ == '__main__':
    main()