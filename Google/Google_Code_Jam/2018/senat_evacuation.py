def main():
    cases = int(input())

    letters = [chr(i+65) for i in range(26)]
    for i in range(1, cases+1):
        num_of_parties = int(input())
        P = [int(x) for x in input().split()]
        plan = ''

        if sum(P) >= 4 and num_of_parties > 2:
            while sum(P) > 0:
                most_sen = max(P)
                index = P.index(most_sen)
                P[index] -= 1
                letter = letters[index]
                plan = plan + letter
        else:
            plan = 'AB BA'
        print("Case #{}: {}".format(i, plan))

if __name__ == '__main__':
    main()