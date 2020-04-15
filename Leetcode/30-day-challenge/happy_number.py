def isHappy(x):
    previous = []
    while True:
        x = add(x)
        if x == 1:
            return True

        if x in previous:
            return False
        previous.append(x)




def add(x):
    total = 0
    for i in str(x):
        total += int(i)**2
    return total


def main():
    num = int(input())
    print(isHappy(num))

if __name__ == '__main__':
    main()