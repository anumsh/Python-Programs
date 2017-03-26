# Program to display the Fibonacci sequence up to n-th term where n is provided by the user



def fibonacci(n):
    # first two terms
    n1 = 0
    n2 = 1
    count = 2
    if n <= 0:
       print("Please enter a positive integer")
    elif n == 1:
       print("Fibonacci sequence ",n)
       print(n1)
    else:
       print("Fibonacci sequence",n)
       print(n1,",",n2)
    while count < n:
       n3= n1 + n2
       # update values
       n1 = n2
       n2 = n3
       count += 1
       return n
       
    

print fibonacci(10)
