def borderPattern(size):
  size = 5
  inner_size = size - 2
  print ('*' * size)
  for i in range(inner_size):
    print ('*' + '  ' * inner_size + '*')
  print ('*' * size)
  
      
print borderPattern(5)

"""
output:

*****
*      *
*      *
*      *
*****


"""
