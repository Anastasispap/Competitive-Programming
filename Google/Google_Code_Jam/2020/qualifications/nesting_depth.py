def main():
    cases = int(input())

    for case in range(1, cases+1):
        string = input()
        output = ''
        nums = [int(i) for i in string]
        nums.reverse()
        num = nums.pop()
        output += '('*num + str(num)

        while len(nums) > 0:
            last_digit = int(output[-1:])
            num = nums.pop()
            if num < last_digit:
                output += ')' * (last_digit-num) + str(num)
            elif num > int(last_digit):
                output += '(' * (num-last_digit) + str(num)
            else:
                output += str(num)
        output += ')'*int(output[-1:])
        print("Case #{}: {}".format(case, output))

if __name__ == '__main__':
    main()