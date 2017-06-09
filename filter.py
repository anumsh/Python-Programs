# The built-in filter() function operates on any iterable type (list, tuple, string, etc).

# Python Filter with Number
numbers=[1, 6, 3, 8, 4, 9]

def lessThanFive(element):
           return element < 5

print filter(lessThanFive, numbers)  # [1, 3, 4]


a = [1,2,4,1,2,3]
s = set(a)
print s
def check(n):
   if n in s:
      return True
   else:
      return False

print filter(check, a)  #[1, 2, 4, 1, 2, 3]
"""
filter() takes two args: (fn, sequence), and returns a list.
The filter() will return all items from the list a which return True
when passed to the function check() which will check if the value
is in the set, s. Since all the numbers in the set come from the
values list, all of the original values in the list will return True.
"""

# Python Filter with String
names = ('angel', 'anushka', 'anum', '')

print filter(None, names)  # ('angel', 'anushka', 'anum')

#  Python Filter with a Function
def startsWithA(element):
           if len(element) > 0:
                      return element[0] == 'a'
           return False

print filter(startsWithA, names) # ('angel', 'anushka', 'anum')
