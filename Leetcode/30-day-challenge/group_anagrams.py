from collections import defaultdict


def main():
    words = input().split()
    print(words)
    temp = defaultdict(list)
    for x in words:
        temp[str(sorted(x))].append(x)

    anagrams = list(temp.values())
    return anagrams


if __name__ == '__main__':
    main()