from sys import argv

script, filename = argv

txt = open(filename,'w') #txt is now a object, open() function returns an object
#file is open to write

txt.truncate()
#truncate empties the file

line1 = raw_input("line1:")
line2 = "this is line2:xxx"

txt.write(line1)# write() function is the class of which txt is an object, txt.write()
txt.write("\n")
txt.write(line2)

txt.close()
