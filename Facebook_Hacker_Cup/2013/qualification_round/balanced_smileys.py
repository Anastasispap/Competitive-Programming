def isBalanced(message):
    minOpen = 0
    maxOpen = 0

    for i in range(len(message)):
        if message[i] == '(':
            maxOpen += 1
            if i == 0 or message[i-1] != ':':
                minOpen += 1
        elif message[i] == ')':
            minOpen = max(0, minOpen-1)
            if i == 0 or message[i-1] != ':':
                maxOpen -= 1
                if maxOpen < 0:
                    break
    if maxOpen >= 0 and minOpen == 0:
        return "YES"
    else:
        return "NO"


def main():
    cases = int(input())
    print(cases)
    for i in range(1, cases+1):
        string = input()
        isBalanced(string)


if __name__ == '__main__':
    main()