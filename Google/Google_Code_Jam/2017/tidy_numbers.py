import os


def main():
    r_file = open('B-large-practice.in', 'r')
    if 'output.txt' in os.listdir():
        os.remove('output.txt')
    w_file = open('output_large.txt', 'a')

    cases = int(r_file.readline())
    for i in range(1, cases+1):
        num = r_file.readline().split()[0]
        max_num = ''
        flag = False
        if len(num) > 1:
            for j in range(len(num)-1):
                if num[j] > num[j+1]:
                    max_num = max_num + str(int(num[j]) - 1) + '9' * (len(num)-1-j)
                    flag = True
                    break
                else:
                    max_num += num[j]
            if j == len(num)-2 and not flag:
                max_num += num[-1:]
        else:
            max_num = num
        w_file.write('Case #{}: {}\n'.format(i, int(max_num)))

if __name__ == '__main__':
    main()