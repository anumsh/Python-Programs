# write file

print "type the filename"

filename= raw_input("filename please")
target = open(filename,"w")
target.truncate()

print "three lines"
line1= raw_input("line 1...")
line2=raw_input("line2 ...")
line3=raw_input("line3....")


# write on file

target.write(line1)
target.write("\n")
                
target.write(line2)
target.write("\n")
                
target.write(line3)
target.write("\n")

# close the file

target.close()
