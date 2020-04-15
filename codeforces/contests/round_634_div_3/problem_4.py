def main():
    cc = int(input())
    
    for i in range(cc):
        table = []
        for i in range(3):
            for j in range(3):
                row = input()        
                row = list(row)
                if row[i+j*3] == '1':    
                    num = '2'
                else:
                    num = '1'
                row[i+j*3] = num
                print(''.join(row))
                    
if __name__ == '__main__':
    main()
