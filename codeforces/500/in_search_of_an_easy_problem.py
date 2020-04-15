
def main():
    _ = int(input())
    answers = [int(x) for x in input().split()]
    if 1 in answers:
        print('HARD')
    else:
        print('EASY')


if __name__ == '__main__':
    main()