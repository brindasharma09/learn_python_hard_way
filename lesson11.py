#copy one file to another location

from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Coping from %s to %s" %(from_file, to_file)

#opening the file
in_file = open(from_file)# in_file is an object created
indata = in_file.read()

print "the output file is %d bytes long"  %len(indata)

print "Does the output file esists? %r"  %exists(to_file)
# exists- to tell whether file exists or not

raw_input()
#to give a file input
out_file  = open(to_file, 'w')
out_file.write(indata)

print" All done"

out_file.close()
in_file.close()
