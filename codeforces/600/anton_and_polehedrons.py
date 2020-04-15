def main():
    cases = int(input())

    num = 0
    for i in range(cases):
        string = input()
        if string == 'Icosahedron':
            num += 20
        elif string == 'Cube':
            num += 6
        elif string == 'Octahedron':
            num += 8
        elif string == 'Dodecahedron':
            num += 12
        else:
            num += 4

    print(num)

if __name__ == '__main__':
    main()