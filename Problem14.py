def findLength(n):
    l = 1
    while(n != 1):
        l += 1
        if(n % 2):
            n = 3*n + 1
        else:
            n = n / 2
    return l

def main():
    maxLength = (1,1) # (number, length)
    for begin in range(1,1000001):
        print(begin)
        l = findLength(begin)
        if( l > maxLength[1]):
            maxLength = (begin,l)
    print(maxLength)

if __name__ == "__main__":
    main()
