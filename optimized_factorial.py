def factorial(a, n):
    if n < 2:
        return a
    else:
        return (factorial(n*a, n-1))


print(factorial(1, 4))
