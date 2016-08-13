def isPrime(x):
  if(x<2):
    return False
  for iterate in range(x)[2:int(x**.5)+1]:
    if not x%iterate:
      return False
  return True

def f(a,b,n):
  return (n**2 + a*n + b)

def main():
  max = 1
  maxTuple=(1,1)
  for a in range(-1000,1000):
    for b in range(-1001,1001):
      n = 30 #to save time
      while isPrime(f(a,b,n)):
        if n > max:
          max = n
          maxTuple = (a,b)
        n+=1
  print(max, maxTuple)

if __name__ == "__main__":
  main()
