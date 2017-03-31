# program to find if the number or aplhabet appear twice in word or in number

inp=list("anumsharma usa")
result = []
n = len(inp)
print n
for i in range(n):
  print " i is ",i
  count = 0
  for j in range(i):
      print "value of j is ",j
      print "input i",inp[i]
      print "input j",inp[j]
      if inp[i] == inp[j]:
          count += 1
          print "count is ",count
          if count == 2:
            break
  if count == 1:
      result.append(inp[i])
print(result)
