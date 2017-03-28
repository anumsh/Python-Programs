def factorial(n):
  if n==0:
    return 1
  elif n<0:
    return "number is in negative can't do factorial"
  else:
    return (n * (factorial(n - 1)))
  
  
print factorial(-6)
