def main():
    cases = int(input())
    for i in range(cases):
        info = [int(x) for x in input().split()]

        if sum(info) % 3 == 0:
            print("YES")
        elif sum(info) :
            print("NO")


if __name__ == '__main__':
    main()