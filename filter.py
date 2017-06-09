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
