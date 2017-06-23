"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
a = raw_input("enter the number")
n1 = int( "%s" % a )
print n1
n2 = int( "%s%s" % (a,a) )
print n2
n3 = int( "%s%s%s" % (a,a,a) )
print n3
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print n4
print n1+n2+n3+n4
