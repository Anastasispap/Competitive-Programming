def main():
    string = input()
    unique_chars = len(set(string))
    if unique_chars % 2 == 1:
        return "male"
    else:
        return "female"


if __name__ == '__main__':
    if main() == "female":
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
