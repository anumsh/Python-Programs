# Difference between remove, del and pop on lists

a = [5,6,7,7,8]  # list

# remove() removes the first matching value, not a specific index

a.remove(7)

print a # [5, 6, 7, 8]

# Both del and pop work on index

a1=[5,6,7,7,8]
del a1[2]

print a # [5, 6, 7, 8]

a1.pop(1)

print a1 # [5, 7, 8]
