def bigger(a,b):
  if a>b:
    return a
  else:
    return b

def biggest(a,b,c):
   return bigger(a,bigger(b,c))
   
print biggest(3,7,1)
