from collections import Counter
def main():
    cases = int(input())

    for case in range(1, cases+1):
        info = input().split()
        N = int(info[0])
        trace = 0
        r = 0
        c = 0
        matrix = []
        for y in range(N):
            row = [int(x) for x in input().split()]
            matrix.append(row)
            trace += matrix[y][y]
            count_dict = dict(Counter(row))
            if len(count_dict.keys()) != N:
                r += 1


        for i in range(N):
            nums = []
            for j in range(N):
                nums.append(matrix[j][i])
            count_dict = dict(Counter(nums))
            if len(count_dict.keys()) != N:
                c += 1

        print("Case #{}: {} {} {}".format(case, trace, r, c))

if __name__ == '__main__':
    main()