# program to find substring in string

def isSubstring(s,s1):
  if s1 in s:
    return True

print isSubstring("anumsharma","ar")

#######  Another Method  #####

def isSubstring(s,s1):
  if s.find(s1) != -1:
    return True

print (isSubstring("anumsharma","ar"))
