def main():
    games = int(input())
    string = input()
    danik = string.count('D')
    anton = string.count('A')

    if danik > anton:
        print("Danik")
    elif anton > danik:
        print('Anton')
    else:
        print("Friendship")

if __name__ == '__main__':
    main()