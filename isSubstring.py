#Method 1: program to find substring in string
'''
def isSubstring(s,s1):
  if s1 in s:
    return True

print isSubstring("anumsharma","ar")
'''

#Method 2 : program to find substring using find().
def sub(s1,s2):
    if s1.find(s2) != -1:
        return ("It contains the given substring") 
        
    else:
        return ("It doesn\'t contains the given substring ") 
    
    
s1 = input("Enter the main string: ")
s2 = input("Enter the substring: ")
print(sub(s1,s2))
  
