#for command line arguements in python-sys.argv
from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)
#seek(0) is used to position a file to the beginning point


def print_line(line_count,f):
    print line_count, f.readline()

current_file = open(input_file)
#current file is the object


print_all(current_file)
rewind(current_file)

current_line = 1
print_line(current_line, current_file)

current_line = 2
print_line(current_line, current_file)
