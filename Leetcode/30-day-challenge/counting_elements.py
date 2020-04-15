from collections import Counter


def main():
    nums = [int(x) for x in input().split()]
    val_cnts = Counter(nums).values()
        
    cnt = 0
    for num in nums:
        if num+1 in nums:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
