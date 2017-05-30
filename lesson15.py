#practise everything learnt till now

print 'You \'d need to know \" bout escapes with \\ that do \n newlines and \t t'
#\'- to tell it is a '
#\" - to tell it is a "
#\\-one \ in sentence
#\n-this is for newline
#\t-tab space

poem = """
\t The lovely World with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and required an explananation \n\t\twhere there is none.
"""

print poem

#using %s in a sentence-to return a string value

five = 10 - 2 + 3 - 6
print "this should be five : %s" %five

#function creation and function returning value

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates
started = 10000
jelly_beans, jars, crates = secret_formula(started)#calling a function and storing values in 3 names

#jelly_beans is only inside secret_formula function.it is not defined outside the function.
#therefore, to use it in print statement we need to call the function to store value in jelly_bean variable
#Therefore call the function - scret_formula(started) and it stores the values in 3 different names
#the names are jelly_beans, jars and crates




print " We have beans: %d, jars: %d, crates: %d" %(jelly_beans, jars , crates)
#we can also print it

started = started/10
print " We have beans: %d, jars: %d, crates: %d" %(secret_formula(started))
#here i used the function to insert all the values
