def shift(string, b):
    for i in range(b):        
        num = string[0]
        string.remove(num)
        string.append(num)
    return string
def main():
    string = input()

    shift = [[1, 1], [1, 1], [0, 2], [1, 3]]

    string = list(string)

    for lst in shift:
        a, b = lst
        if a == 0:
            string = shift(string, b)
        else:
            string = string[::-1]
            shift(string, b)
            string = string[::-1]
    print(''.join(string))

if __name__ == '__main__':
    main()
