#read the file
from os.path import exists
print "type the filename "

file= raw_input("> ")
if exists(file):
    openit=open(file,"r")
    print openit.read()
else:
    print "no such file"
    
