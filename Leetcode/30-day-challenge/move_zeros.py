def main():
    nums = [int(x) for x in input().split()]
    zeros = nums.count(0)

    for i in range(zeros):
        nums.remove(0)
    for i in range(zeros):
        nums.append(0)
    print(nums)

if __name__ == '__main__':
    main()