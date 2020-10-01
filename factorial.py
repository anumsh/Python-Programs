# program to find factorial of a number.
def factorial(n):                               # funtion to calculate factorial.
  if n==0:
    return 1
  elif n<0:
    return "number is in negative can't do factorial"
  else:
    return (n * (factorial(n - 1)))
  

n = int(input("Enter the number: "))           #taking input from the user.
print factorial(n)
