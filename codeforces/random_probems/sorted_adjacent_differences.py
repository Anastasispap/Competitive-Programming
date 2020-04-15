def main():
    cc = int(input())
    for i in range (cc):
        _ = int(input())
        nums = [int(x) for x in input().split()]
        output = ''
        nums.sort()
        for num in nums:
            if num > 0:
                nums.remove(num)



if __name__ == '__main__':
    main()
