import sys 
import random
import math

room = {}
word = "yes"

def hp_bar (current,full):
    out = "hp: ["
    stars = math.ceil(current/4.0)
    spaces = math.ceil(full /4.0)
    spaces -= stars
    out += "*" * stars
    out += " " * spaces
    out += "]"
    print (out)
def print_inventory (label,container):
    stuff = []
    for item in container["inventory"] :
        stuff.append(item["name"])
    print(label + ": " + ", ".join(stuff))

def sign (lines):
    longest = 0
    for line in lines:
        if len(line)> longest:
                longest = len(line)
    width = longest +6
    hight = 4 + len(lines)
    for x in range(0, hight):
        if x == 0 or x == hight - 1:
            print ("#"*width)
        elif x == 1 or x == hight - 2:
            spaces = width - 2
            print ("#" + (" " * spaces) + "#")
        else:
            spaces = longest - len(lines[x - 2])
            print ("#  " + lines[x - 2] + (" " * spaces) + "  #")

def esc(words) :
    global room
    print("Fred escaped the dungeon you get 50 points")
    change_room (outside)
def help_command (words) :
    print ("start your command with a verb get, kill, jump, climb.")
    print ("examples: \"kill rat\", \"climb rope\"")
def change_room (dest) :
    global room
    room = dest
    if "on_enter" in room :
        room["on_enter"]()
def search_inventory (thing, name) :
    if "inventory" in thing :
        for idx,item in enumerate (thing["inventory"]) :
            if item["name"] == name :
                return idx
    return None
def climb (words) :
    global room
    if search_inventory (room, "ladder") != None :
        if room is dungeon :
            print("Fred climbed out of the dungeon")
            change_room (outside)
        else:
            print("Fred climbed the ladder and has a look around")
    else:
        if search_inventory(fred, "ladder") != None :
            print("Fred can't climb a ladder while he's holding it")
        else:
            print("theres nothing to climb here")
            
def swing (attacker, defender) :
    if random.randint(1,100) > 30:
        if search_inventory (attacker, "sword") != None:
            max_damage = attacker ["power"] + 70
        else: # found sword
            max_damage = attacker ["power"]
        dam = random.randint(max_damage /2, max_damage)
        defender["hp"] = defender["hp"] - dam
        print("{0} hit {1}{2} for {3} hp".format(attacker["name"], defender["article"], defender["name"], dam))
        if defender["hp"] < 1 :
            print("the {0} dies".format (defender ["name"]))
            del defender["hp"]
            defender["name"] = "corpse of " + defender["article"] + defender["name"]
    else:
        print ("{0}{1} tries to hit {2}{3} and misses".format(attacker["article"], attacker["name"], defender["article"], defender["name"]))
def get (words) :
    words.pop(0)
    thing = " ".join(words)
    for idx,item in enumerate (room["inventory"]) :
        if thing == item["name"] :
            if "hp" in item :
                print ("the {0} does not want to be picked up".format(item["name"]) )
                swing (item, fred)
            else:
                fred ["inventory"].append(item)
                del room["inventory"] [idx]
                print ("Fred picked up the {0}".format(item["name"]))
                return 
def enter_dungeon () :
    dungeon ["inventory"].append ({ "name": "rat","article": "the ", "hp": 50, "power": 50})
def kill(words) :
    for item in room["inventory"] :
        if "hp" in item :
            swing(fred, item)
            if "hp" in item: #if he's still alive
                swing(item, fred)
                if not "hp" in fred:
                    print("fred died.")
                    sign (["      R.I.P.",
                           "    1990-2013 ",
                           "Fred F. McFredricson"])
                    exit ()
                else: # monster just hit you
                    if room == outside and random.randint(1,100) > 25:
                        print ("the blow knocks fred back and fred falls back in the dungeon")
                        change_room (dungeon)
            return
    print("nothing to kill here")
souls = {
    "jump": "fred jumped " + str(random.randint(6,20)) + " inches"
}
commands = {
    "kill": kill,
    "attack": kill,
    "get": get,
    "take": get,
    "help": help_command,
    "?": help_command,
    "": help_command
}

dungeon = {
    "commands": {
        "esc": esc,
        "climb": climb
    },
    "on_enter": enter_dungeon,
    "description": "Fred is in a dungeon.",
    "inventory": [
        { "name": "ladder" },
        { "name": "sword"}
    ]
}
fred = {
    "article": "",
    "name": "Fred",
    "hp": 120,
    "power": 40,
    "inventory": []
}

outside = {
    "commands": {
    },
    "description": "fred is now in a forest",
    "inventory": [
        {
            "name": "scary monster",
            "article": "the ",
            "hp": 120,
            "power": 100
        }
    ]
}

change_room (dungeon)

sass = [
    "Whatchoo talkin' 'bout, foo?",
    "Speak English, child!",
    "Shut up!",
    "Huh??",
    "How about no.",
    "How about I {0} your face!",
    "That's not my job, I'm just the narrator!",
    "That ain't right!"
]

print("this text game was built at northstar\n")

help_command([])
print ()

while True:
    print()
    print(room["description"])
    print_inventory ("things Fred sees here",room)
    hp_bar (fred["hp"],120)
    print_inventory ("inventory",fred)
    print ("type a command and press enter")
    command = sys.stdin.readline().strip()
    words = command.split(' ')
    verb = words[0]
    if verb in room["commands"]:
        room["commands"][verb](words)
    elif verb in commands:
        commands[verb](words)
    elif verb in souls:
        print(souls[verb])
    else:
        s = sass[random.randint(0, len(sass) - 1)]
        s = s.format (command)
        print(command + "? " + s)

# print random.random()

