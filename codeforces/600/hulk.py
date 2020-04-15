def main():
    layers = int(input())
    string = ''

    if layers > 1:
        for i in range(1, int(layers)+1):
            if i == int(layers):
                if i % 2 != 0:
                    string += 'I hate it'
                else:
                    string += 'I love it'
            else:
                if i % 2 == 0:
                    string += 'I love that '
                else:
                    string += 'I hate that '
    else:
        string = 'I hate it'

    print(string)


if __name__ == '__main__':
    main()