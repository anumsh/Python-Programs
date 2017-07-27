# program to get the sum of a non-negative integer.

def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))

print(sumDigits(345))
print(sumDigits(45))
