
"""
By using list comprehension, please write a program to print the list after
removing the value 24 in [12,24,35,24,88,120,155].
"""


lists = [12,24,35,24,88,120,155]
lists= [x for x in lists if x!=24]
print lists  # [12, 35, 88, 120, 155]

"""
write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
"""

lst = [5,6,77,45,22,12,24]
lst = [x for x in lst if x%2!=0]
print lst # [5, 77, 45]


"""
program to print the list after removing delete numbers which are divisible
by 5 and 7 in [12,24,35,70,88,120,155].
"""

lst = [12,24,35,70,88,120,155]
lst = [x for x in lst if x%5!=0 and x%7!=0]
print lst # [12, 24, 88]
