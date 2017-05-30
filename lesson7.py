from sys import argv #import is a way to add modules to script from python dataset
# sys is a module
script, first, second, third = argv
#argv- arguement variable- variable holds arguements
#in line3- it is assigning arguements to diff. variables

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#Run this script: python lesson7.py first 2nd 3rd
#run with : python lesson7.py apple orange grapes
#This applies whenver there is argv

# see the difference between raw_input() and argv , both are used to input
#from users
