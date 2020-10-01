# reverse the string 
# 1st method using slice

'''
def string_reverse(string1):
    return string1[::-1]

print string_reverse('hello')

'''

# 2nd method through list
'''
def reverse(list):
     rlist = []
     i = len(list) - 1
   
     while i >= 0:
             rlist.append(list[i])
             i = i - 1
     return rlist
     
print (reverse([5,4,3,2,1]))
'''

# 3rd Method using function- reverse().
def list_reverse(l):
    l.reverse()
    return l
l = [1,2,3,4,5]
print(list_reverse(l))



