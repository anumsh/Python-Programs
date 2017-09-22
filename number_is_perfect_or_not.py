# Write a Python function to to determine if a number is a perfect number.
"""
Perfect number number that is half the sum of all of its positive divisors
(including itself).

for example : if the number is 6:

1 is divisible by 6
2 is divisible by 6
3 is divisible by 6
4 is not divisible by 6

even 1+2+3=6 which is also divisible by 6

"""
def perfect_number(n):
           sum=0
           for x in range(1,n):
                      if n % x ==0:
                                 sum += x
           if (sum == n):
                      return "number is perfect"
           else:
                      return "number is not perfect"
           
print perfect_number(6)
print perfect_number(18)

string="string_like_this"
print string.title()
