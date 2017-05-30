my_name = 'Brinda Sharma'
my_age = 24
my_height = 164
my_weight = 189
my_eyes = 'blue'
my_teeth = 'yellow'
my_hair = 'brown'

#  %s- it is to insert string in a sentence
#  %d- it is to insert numeric number
# in line 13 % my_name - it contains the string that has to be inserted in the
  #sentence

print "let us talk about %s. " % my_name
print "let us talk about my height %d." % my_height
print "let us talk about my weight %d." % my_weight
print " he has got %s eyes and %d height" % (my_eyes, my_height)
print "his teeth is really %s and hair color is %s." % (my_teeth, my_hair)
print "the addition of my height %d , my weight %d and my age %d is %d." %(
my_height, my_weight, my_age, my_height + my_weight + my_age)
x = "There are %d types of people" % 10

print "i said: %r" %x # output : i said: 'There are 10 types of people'
# %r --take in the raw form

print "i said : %s" %x #i said : There are 10 types of people
