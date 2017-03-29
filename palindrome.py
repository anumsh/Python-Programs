def palindrome(n):
  m=n 
  a=0
  while(m!=0):
    a=m %10 + a*10
    m=m/10
    
  if (n == a):
    return "it is a palindrome number"
  else:
    return "it is not palindrome number"
    
print palindrome(156)
