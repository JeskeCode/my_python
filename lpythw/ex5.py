my_name = 'Jason Van Jeske'
my_age = 44 # a lie
my_height = 80 # not sure
my_weight = 180 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Lets's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d punds heavy." % my_weight
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get in exactly right
print "If I add %d %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
