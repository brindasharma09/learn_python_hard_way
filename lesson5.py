# \n -use- to send the nest character in a new line
# \n\n= double means leaving 2 lines space in between

days= ' mon tue wed thurs fri sat sun '
months = 'Jan\nFeb\n\nMarch\nApril\nMay\nJune\nJuly\nAugust'

print "here are the days:", days
print "here are the days: %s" %days

print "some of the months:\n", months


print " I am 6'2\\ tall."
print "I am 6\'2 tall."  # "\'tells there is a ' quote "
print "I am 6\"2 tall."  # "\" tells there is a double quote in between the string"

print "I am 6'2\t tall."# \t- is to give a tab space
print "I am \r tall" #output- is just "tall"

print " myname\r brinda"

print "I am \a  cat"
print "I am8\r cat"  #carriage return (\r) - returns back character after /r
# in above sentence it gives cat8 - because there is no space betweeb 8 and /r and it is numeric
