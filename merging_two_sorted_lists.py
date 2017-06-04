# Merging two sorted list

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
c= []

# 1st method
"""
while  a and  b:
           if a[0] < b[0]:
                      c.append(a.pop(0))
           else:
                      c.append(b.pop(0))

print c +a + b
"""
# 2nd method

a.extend(b)
c= sorted(a)
print c
           
                      
           
