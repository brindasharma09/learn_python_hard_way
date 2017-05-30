#Combining argv and raw_input

from sys import argv

script, user_name = argv
prompt = 'ans plz'

print "Hi %s I'm the %s script" % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s" %(user_name)
lives = raw_input(prompt)

print "What kind of computer you have?"
computer = raw_input(prompt)

print "basically answer is : %r %r %r " %(likes, lives, computer)

#argv- gives input befor running the script and #raw_input() in between
#when the script is running
