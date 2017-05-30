#functions can also return a value
#practising with functions

def add(a,b):
    print "adding %d + %d" %(a,b)
    return a + b

def subtract(a,b):
    print "subtracting %d - %d" %(a,b)
    return a - b
#return statement calculates/returns value using the function
def multiply(a,b):
    print "multiply %d * %d" %(a,b)
    return a * b

def divide(a,b):
    print "divide %d / %d" %(a,b)
    return a/b

age = add(3,5)
height = subtract(78,4)
weight = multiply(90, 2)
iq = divide(100,2)

print (" age is %d, height is %d, weight is %d, iq is %d") %(age, height, weight, iq)
#printing all the values returned by the functions
