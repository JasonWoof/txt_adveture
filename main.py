import sys 
import random

room = {}
word = "yes"

def esc() :
    global room
    print "you escaped the dungon you get 50 points"
    room = outside
def change_room() :
    global room
    print "you go outside"
    room = outside
def attack() :
    print "you do some damage"
souls = {
    "jump": "you jumped " + str(random.randint(6,20)) + " inches"
}
dungeon = {
    "commands": {
        "esc": esc,
        "change": change_room
    },
    "description": "you are in a dungeon you have a broadsword a dierk and some armor what do you do"
}

outside = {
    "commands": {
             

    },
    "description": "you are now in a forest"
}

room = dungeon

while True:    
    print room["description"]
    command = sys.stdin.readline().strip()
    words = command.split(' ')
    verb = words[0]
    if verb in souls:
        print souls[verb]
    elif verb in room["commands"]:
        room["commands"][verb]()
    else:
        print "you said " + command

# print random.random()

