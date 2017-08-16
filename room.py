"""
This is a game called 'The Room.' It is a text-based game.
"""

import os

clear = lamda: os.system('cls')



print "You wake up in a dark room. Where is the light?"
print "What would you like to do? \n"

clear()

print "(enter the number of the option you'd like to choose)"


def wake_up():
    opts = {1:'Stand up.', 2:'Go back to sleep.'}

    user_input = raw_input(str(opts) + "\n")
    while True:
        if int(user_input) == 1:
            print "Great, now you're STANDING in a dark room."
            raw_input('...')
            standing_1()
            break
        elif int(user_input) == 2:
            print "Okay, thanks for playing."
            raw_input('...')
            break
        elif int(user_input) == 75:
            print "YOU CHOSE THE MAGIC NUMBER! YOU WIN! \n Thanks for playing!"
            raw_input('...')
            break
        else:
            print "Enter a real option, smart alec."
            user_input = raw_input(str(opts) + "\n")

def closet_1():
    pass

def standing_1():
    print "Where do you want to go?"
    opts = {1:'Left', 2:'Right', 3:'Forward', 4:'Backward'}

    user_input = raw_input(str(opts) + "\n")
    while True:
        if int(user_input) == 1:
            print "You slowly make your way to your left in the dark. There's nothing here so far. You keep walking..."
            raw_input('...')
            print "You bump into something about waist high. It feels like... a desk? This seems promising."
            raw_input('...')
            desk_1() #ADD THIS!
            break
        elif int(user_input) == 2:
            print "You slowly make your way to your right in the dark."
            raw_input('...')
            print "BUMP. Just a wall here."
            break
        elif int(user_input) == 3:
            print "You stumble forward in the dark. There's nothing here so far. You keep walking..."
            raw_input('...')
            print "THUMP. Well, there's a wall. Or a door??"
            closet_1() #ADD THIS!
            break
        elif int(user_input) == 4:
            print "Well, now you're back on the bed! What next?"
            wake_up()
            break
        else:
            print "Come on, really?"
            user_input = raw_input(str(opts) + "\n")

def desk_1():
    print "You're at a desk. What would you like to do?"
    opts = {1:'Sit Down', 2:'Feel around on the surface', 3:'Feel around for drawers', 4:'Go back to the center of the room'}

    user_input = raw_input(str(opts) + "\n")
    while True:
        if int(user_input) == 1:
            print "You feel around in the dark for the chair and sit down. Comfy!"
            raw_input('...')
            desk_1()
            break
        elif int(user_input) == 2:
            print "You "
            raw_input('...')
            print "BUMP."
            raw_input('...')
            standing_1()
            break
        elif int(user_input) == 3:
            print "You st"
            raw_input('...')
            print "THUMP."
            closet_1() #ADD THIS!
            break
        elif int(user_input) == 4:
            print "Well"
            wake_up()
            break
        else:
            print "This is just getting old."
            user_input = raw_input(str(opts) + "\n")

wake_up()
