def main():
    info = input().split()
    num_of_problems = int(info[0])
    extra_min = int(info[1])

    total_time = 4*60 - extra_min


    for i in range(1, num_of_problems+1):
        if i == num_of_problems:
            return i
        elif i*(i + 1)*(5 / 2) <= total_time < (i + 2)*(i + 1)*(5 / 2):
            return i


if __name__ == '__main__':
    print(main())