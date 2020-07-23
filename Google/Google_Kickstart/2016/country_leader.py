def main():
    t = int(input())
    for case in range(t):
        
        n = int(input())
        
        u_size = []
        names = []

        for i in range(n):
            name = input()
            chars = set([])

            for c in name:
                if(not c.isspace()):
                    chars.add(c)

            names.append(name)
            u_size.append(len(chars))

        max_s = max(u_size)
        f_names = []
        for i in range(len(u_size)):
            if(max_s == u_size[i]):
                f_names.append(names[i])

        print(min(f_names))


if __name__ == "__main__":
    main()
