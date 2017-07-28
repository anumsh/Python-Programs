"""
program to calculate the harmonic sum of n-1. 
The harmonic sum is the sum of reciprocals of the positive integers. 
"""

def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))
    
print(harmonic_sum(7))
print(harmonic_sum(4))
