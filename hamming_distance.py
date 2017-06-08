# hamming distance - he Hamming distance between two strings of equal length
# is the number of positions at which the corresponding symbols are different

def hamming(s1,s2): 
    if len(s1) != len(s2): 
        return ("length of the two strings are not equal") 
    else:
        sum=0
        for c1,c2 in zip(s1,s2):
          #print "c1 -------------",c1
          #print "c2 ----------",c2
          if c1 != c2:
            sum = sum + 1 
        return sum

print hamming("karolin","kathoin")  # 3
print hamming("1011100","1111111")  # 3
print hamming("1238273837","463743746") #length of the two strings are not equal

