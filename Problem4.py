def isPalindrome(inp):
    ls = str(inp)
    brek = round(len(ls)/2)
    comp = list(ls[:brek])
    comp.reverse()
    if len(ls)%2==0:
        return comp == list(ls[brek:])
    else:
        return comp == list(ls[brek+1:])

def main():
    numbers = "9876543210"
    myLs = [x+y+z for x in numbers for y in numbers for z in numbers]
    #list comprehensions <3
    answer=0
    for first in myLs:
        for second in myLs:
            if (int(first)*int(second)>answer) & (isPalindrome(int(first)*int(second))):
                answer=int(first)*int(second)
    print(isPalindrome(4774),answer)

if __name__ == "__main__":
    main()
