# program for fibonacci series

def fibonacci(n):
  a=1
  b=1 
  for i in range(n):
    temp=a 
    a=b 
    b = temp + a 
    print str(a)
  return a
  
print fibonacci(5)
