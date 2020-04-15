def main():
    cases = int(input())
    nums = [0]
    for x in input().split():
        nums.append(int(x))
    copy = nums
    for i in range(1, cases+1):
        copy[nums[i]] = i

    print(nums)


if __name__ == '__main__':
    main()