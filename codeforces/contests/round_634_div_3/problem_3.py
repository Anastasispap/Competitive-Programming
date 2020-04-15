def main():
    cc = int(input())
    
    for i in range(cc):
        n = int(input())
        nums = [int(x) for x in input().split()]
        nums_set = set(nums)

        cnt_max = 0
        for num in nums_set:
            if nums.count(num) > cnt_max:
                cnt_max = nums.count(num)

        if cnt_max > n//2:
            cnt_max = n//2
        print(cnt_max)


                

if __name__ == '__main__':
    main()
