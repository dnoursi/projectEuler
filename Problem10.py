def isPrime(x):
    for iterate in range(x)[2:int(x**.5)+1]:
        if not x%iterate:
            return False
    return True

def main():
    sum = 0
    for n in range(2,2000000):
        if(n % 1000 == 0):
            print(n)

        if isPrime(n):
            sum += n
    print(sum)

def altMain(): # thought this would be faster ... it isn't
    primes = []
    for n in range(2,2000000):

        #if(n % 1000 == 0):
        #    print(n)

        isPrime = True
        for prime in primes:
            if n % prime == 0:
                isPrime = False
        if isPrime:
            primes.append(n)
    print(sum(primes))

if __name__ == "__main__":
    naiveMain()
    main()
