# bubble sort
# list- 34,56,71,3,19,5

def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp


alist= list()
number=raw_input("enter the elements")

for i in range(int(number)):
    n=raw_input("number: ")
    alist.append(int(n))

print "the unsorted array"

print alist

bubbleSort(alist);

print "sorted array"

print alist
    
