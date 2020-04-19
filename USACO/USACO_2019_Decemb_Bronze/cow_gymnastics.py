def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    

def main():
    fin = open("gymnastics.in", "r")
    fout = open("gymnastics.out", "w")

    k, n = map(int, fin.readline().split())
    max_pairs = int(factorial(n)/(factorial(n-2)*2))
    nums = [int(x) for x in fin.readline().split()]
    for i in range(1, k):
        cnt = 0
        for x in fin.readline().split():
            if nums.index(int(x)) < cnt:
                max_pairs -= 1
            cnt += 1

    fout.write(str(max_pairs))
        

if __name__ == '__main__':
    main()
