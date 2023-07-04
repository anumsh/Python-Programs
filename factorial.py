def factorial(n):
  if n==0:
    return 1
  elif n<0:
    return "number is in negative can't do factorial"
  else:
    return (n * (factorial(n - 1)))
  
  
print factorial(-6)

#another way of find factorial

def f(n):
    fact=1
    while n>1:
        fact=fact*n
        n=n-1
    print( fact)

f(5)
