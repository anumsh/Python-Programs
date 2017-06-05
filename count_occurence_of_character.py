#Count occurrence of a character in a Python string

sentence='The Udacity Udacity'

def count_chars(s):
        s=s.lower()
        count=list(map(s.count,s))
        return (max(count))

print count_chars(sentence)
