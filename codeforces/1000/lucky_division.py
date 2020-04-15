def main():
    num = int(input())
    divisors = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

    for divisor in divisors:
        if num % divisor == 0:
            return "YES"
    return "NO"

if __name__ == '__main__':
    print(main())