
def main():
    cases = int(input())

    for i in range(1, cases+1):
        N = int(input())
        P = input()
        
        path = P.replace('E', 'n')
        path = path.replace('S', 'E')
        path = path.replace('n', 'S')

        print('Case #{}: {}'.format(i, path))

main()
