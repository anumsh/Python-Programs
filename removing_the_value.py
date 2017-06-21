
"""
By using list comprehension, please write a program to print the list after
removing the value 24 in [12,24,35,24,88,120,155].
"""


lists = [12,24,35,24,88,120,155]
lists= [x for x in lists if x!=24]
print lists  # [12, 35, 88, 120, 155]
