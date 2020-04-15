def main():
    cc = int(input())
    
    for i in range(cc):
        string = ''
        n, a, b = [int(x) for x in input().split()]
        for i in range(97, 97+b):
            string += chr(i)

        


if __name__ == '__main__':
    main()
