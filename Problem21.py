d = {}

def compute(n):
    d[n] = 1
    for iterate in range(2,int(n ** .5)):
        if n % iterate == 0:
            d[n] += iterate + (n//iterate)

def divisors(n):
    if n not in d.keys():
        compute(n)
    if(d[n] in d.keys()):
        return n == d[d[n]]
    else:
        if(d[n] <= 10000):
            compute(d[n])
            return n == d[d[n]]
        else:
            return False
            
def main():
    sum=0
    for iterate in range(1,10000):
        if divisors(iterate):
            sum += iterate
    print(sum)
    
if __name__ == "__main__":
    main()
