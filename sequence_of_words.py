"""
Question:
Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.
"""
items=[x for x in raw_input().split(',')]   #h,r,y,i,o,d,a,b
items.sort()
print ','.join(items)  # a,b,d,h,i,o,r,y
