print "mary had a little lamb"
print "its fleece was as whits as %s" % 'snow'
print "." * 10

end1 = 's'
end2 = 'an'
end3 = 'k'
end4 = 'a'
end5 = 'lp'

print end1 + end2 +end3 + end4 + end5


#more complex string formatting

formatter = "% r %r %r"
# %r prints everything in raw form

print formatter % (1, 2, 3)      #numbers
print formatter % ('one', 'two', 'three') #strings
print formatter % ( True, False, True) #boolean
print formatter % ('i love nona', 'nona loves me', 'we kiss each other')
#Python recognizes True and False as keywords representing the concept of true and false. If you put quotes around them then
#they are turned into strings and won't work. 
