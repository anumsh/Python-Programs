# Simple program to print the pyramid pattern in python
# input :
# Enter a number3
# Output:
#
#   *
#  * *
# * * *
a = int(input("Enter a number"))
for i in range(1, a+1):
    print(" " * (a - i), "* " * i)