#!/usr/bin/env python

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "What there's not 10 thingsin that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Girl", "Boy"]

while len(stuff) != 10:
    nex_one = more_stuff.pop()
    print "Adding: ", nex_one
    stuff.append(nex_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

