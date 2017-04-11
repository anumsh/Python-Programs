def anagram(s, t):
    string = len(s)
    substring = len(t)
    # edge conditions
    if substring == 0:
        return True
    if substring > string:
        return False
    # store substring in dictionary diction
    substringdiction = dict()
    for c in t:
        substringdiction[c] = substringdiction.get(c, 0) + 1

    # loop s
    for i in range(string):
        stringdiction = {}
        for j in range(i, i + substring):
            # this substring !=substringdiction case, break
            if s[j] not in substringdiction:
                break
            # store each substring in dictionary stringdiction
            else:
                stringdiction[s[j]] = stringdiction.get(s[j], 0) + 1
        # stringdiction==substringdiction means one anagram of t is the substring of s, return True
        if stringdiction == substringdiction:
            return True
    # not found stringdiction=substringdiction in the loop
    return False

print anagram("udacity","ty")
print anagram("udacity"," ")
print anagram("udacity","mnbgfdfdsfsdfgsgdfg12121")
