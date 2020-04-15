def main():
    cases = int(input())
    X = 0
    for i in range(cases):
        info = input()
        if '--' in info:
            X -= 1
        else:
            X += 1
    print(X)

if __name__ == '__main__':
    main()