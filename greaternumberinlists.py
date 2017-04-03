list =[3,5,6,7,17]
max_num=list[0]
for num in range(1,len(list)):
  if list[num]> max_num:
    max_num=list[num]
print max_num
