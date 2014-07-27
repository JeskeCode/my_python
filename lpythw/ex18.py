# this one is like your script argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
	
# ok, that *args is acutally pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes on arguments
def print_none():
    print "I am nothing'."

print_two("Jason","Jeske")
print_two_again("Jason","Jeske")
print_one("First!")
print_none()	
