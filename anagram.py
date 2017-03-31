def is_anagram(s1, s2):
    s1 = list(s1)
    print s1
    s2 = list(s2)
    print s2
    s1.sort()
    print s1
    s2.sort()
    print s2
    return s1 == s2

def anagram_finder(s, t):
    match_length = len(t)
    print "match  string length",match_length
    pattern_length = len(s)
    print "string length", pattern_length
    for i in range(pattern_length - match_length + 1):
        print i
        print s[i: i+match_length]
        print t
        if is_anagram(s[i: i+match_length], t):
            return True
    return False

print is_anagram("urhget", "teghur")
print anagram_finder("udacity","adc")
