#!/usr/bin/env python

### EDIT THIS PART ###
startDrinks = 99
drinkSpeed = 1
drink = "beer"

### THIS IS WHERE THE ACTION IS ###
for q in range(startDrinks, 0, -drinkSpeed):
    # prep
    if q == 1:
        b = "bottle"
    else:
        b = "bottles"
    if drinkSpeed == 1:
        it = "it"
    else:
        it = "them"
    if (q - drinkSpeed) > 1:
        b2 = "bottles"
    else:
        b2 = "bottle"

    print str(q) + " " + b + " of " + drink + " on the wall, " + str(q) + " " + b + " of " + drink + "."

    if drinkSpeed > q:
        print "Hold on there! You're drinking too fast!"
        print " "
        print "No more bottles of " + drink + " on the wall, no more bottles of " + drink + "."
        print "Go to the store and buy some more, " + str(startDrinks) + " bottles of " + drink + " on the wall."
        exit
    else:
        if (q - drinkSpeed) == 0:
            print "Take " + str(drinkSpeed) + " down and pass " + it + " around, no more bottles of " + drink + " on the wall."
            print " "
            print "No more bottles of " + drink + " on the wall, no more bottles of " + drink + "."
            print "Go to the store and buy some more, " + str(startDrinks) + " bottles of " + drink + " on the wall."
        else:
            print "Take " + str(drinkSpeed) + " down and pass " + it + " around, " + str(q - drinkSpeed) + " " + b2 + " of " + drink + " on the wall."
            print " "
