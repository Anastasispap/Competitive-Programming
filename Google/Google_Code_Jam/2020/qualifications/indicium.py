def main():
    cases = int(input())

    for case in range(1, cases + 1):
        info = input().split()
        N = int(info[0])
        K = int(info[1])

        if N == 2:
            if K == 4 or K == 2:
                return True
            return False
        else:
            if N*(N+1)//2 == K:
                return True


if __name__ == "__main__":
    if main():
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
