# reverse the string 
# 1st method using slice

'''
def string_reverse(string1):
    return string1[::-1]

print string_reverse('hello')

'''

# 2nd method through list

def reverse(list):
     rlist = []
     i = len(list) - 1
     print i
     while i >= 0:
             rlist.append(list[i])
             i = i - 1
     return rlist
     
print reverse("anum")

