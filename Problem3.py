import sys
    
def isPrime(x):
    for iterate in range(x)[2:int(x**.5)+1]:
        if not x%iterate:
            return False
    return True
    
def main():
#io
    try:
        product = int(input("Which number would you like to factor?"))
    except ValueError:
        print("This is not a natural number!")
        sys.exit(0);
    
#computation    
    answer = 1 #always valid
    while product != 1:
        smallest=2 #smallest prime factor (pf)
        while product%smallest:
            smallest+=1
        if isPrime(smallest):
            if smallest>answer: # we want, in truth, the biggest pf, not the smallest
                answer=smallest
        product=product/smallest # look for next smallest pf
#        
    print(answer)
    
if __name__ == "__main__":
    main()