def main():
    string = input()
    if '+' not in string:
        print(string)
    else:
        string = string.split('+')
        string.sort()
        summation = ''
        for x in string:
            summation += x +'+'
        print(summation[:-1])


if __name__ == '__main__':
    main()