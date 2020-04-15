def main():
    r_file = open('beautiful_strings.txt', 'r')
    w_file = open('beautiful_string_output.txt', 'a')

    cases = int(r_file.readline())
    nums = [x for x in range(1, 27)]
    nums.reverse()
    letters = [chr(x+64) for x in range(1, 27)]
    for i in range(1, cases+1):
        letter_cnt = []
        sum = 0
        string = r_file.readline().upper()

        for char in letters:
            a = string.count(char)
            if a != 0:
                letter_cnt.append(a)
        letter_cnt.sort()
        letter_cnt.reverse()
        for j in range(len(letter_cnt)):

            sum = sum + letter_cnt[j]*nums[j]

        w_file.write('Case #{}: {}\n'.format(i, sum))

if __name__ == '__main__':
    main()