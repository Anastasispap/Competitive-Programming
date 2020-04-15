def main():
    _ = int(input())
    nums = [int(x) for x in input().split()][::-1]

    max_cnt = 1
    cnt = 1
    top = nums.pop()
    while nums:
        num = nums.pop()
        if top <= num:
            cnt += 1
        else:
            cnt = 1
        top = num
        max_cnt = max(max_cnt, cnt)

    print(max_cnt)



if __name__ == '__main__':
    main()