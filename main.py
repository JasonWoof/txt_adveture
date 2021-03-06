import sys 
import random
import math
import time

room = {}
word = "yes"

def slow_print (text):
    for c in text:
        sys.stdout.write (c)
        sys.stdout.flush ()
        time.sleep (.02)
    print('')
    time.sleep (.5)
def uwin ():
    slow_print ("You win!")
    time.sleep(4)
    exit ()
def maybewin ():
    if not ("hp" in monster):
        uwin ()
    
def hp_bar (current,full):
    out = "hp: ["
    stars = int(math.ceil(current/4.0))
    spaces = int(math.ceil(full /4.0))
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
            slow_print ("#"*width)
        elif x == 1 or x == hight - 2:
            spaces = width - 2
            slow_print ("#" + (" " * spaces) + "#")
        else:
            spaces = longest - len(lines[x - 2])
            slow_print ("#  " + lines[x - 2] + (" " * spaces) + "  #")

def esc (words) :
    global room
    slow_print("Fred escaped the dungeon you get 50 points")
    change_room(outside)
def help_command (words) :
    slow_print("This is a text-adventure game. You direct Fred by typing commands.\n")
    slow_print("Start your command with a verb, like: \"get\", \"kill\", \"jump\" or \"climb\".")
    slow_print("Examples: \"kill rat\", \"climb rope\"")
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
            slow_print("Fred climbed out of the dungeon.")
            change_room (outside)
        else:
            slow_print("Fred climbed the ladder and has a look around.")
    else:
        if search_inventory(fred, "ladder") != None :
            slow_print("Fred can't climb a ladder while he's holding it.")
        else:
            slow_print("Theres nothing to climb here.")
            
def swing (attacker, defender) :
    if random.randint(1,100) > 30:
        if search_inventory (attacker, "sword") != None:
            max_damage = attacker ["power"] + 70
        else: # found sword
            max_damage = attacker ["power"]
        dam = random.randint(max_damage /2, max_damage)
        defender["hp"] = defender["hp"] - dam
        slow_print("{0}{1} hit {2}{3} for {4} hp.".format(attacker["article"].capitalize(), attacker["name"], defender["article"], defender["name"], dam))
        if defender["hp"] < 1 :
            slow_print("{0}{1} dies.".format(defender["article"].capitalize(), defender["name"]))
            del defender["hp"]
            defender["name"] = "corpse of " + defender["article"] + defender["name"]
    else:
        slow_print ("{0}{1} tries to hit {2}{3} and misses.".format(attacker["article"].capitalize(), attacker["name"], defender["article"], defender["name"]))
def get (words) :
    words.pop(0)
    thing = " ".join(words)
    for idx,item in enumerate (room["inventory"]) :
        if thing == item["name"] :
            if "hp" in item :
                slow_print("The {0} does not want to be picked up.".format(item["name"]))
                swing(item, fred)
                return
            else:
                fred["inventory"].append(item)
                del room["inventory"] [idx]
                slow_print("Fred picked up the {0}.".format(item["name"]))
                return
    slow_print("there is no {0} here".format(thing))
def enter_dungeon () :
    dungeon ["inventory"].append({ "name": "rat", "article": "the ", "hp": 50, "power": 50})
def kill(words) :
    for item in room["inventory"] :
        if "hp" in item :
            swing(fred, item)
            if "hp" in item: #if he's still alive
                swing(item, fred)
                if not "hp" in fred:
                    sign(["      R.I.P.",
                          "    1990-2013 ",
                          "Fred F. McFredricson"])
                    time.sleep(4)
                    exit()
                else: # monster just hit you
                    if room == outside and random.randint(1,100) > 25:
                        slow_print("The blow knocks fred back and fred falls back in the dungeon.")
                        change_room(dungeon)
            return
    slow_print("nothing to kill here")
souls = {
    "jump": "Fred jumped " + str(random.randint(6,20)) + " inches."
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
monster = {
    "name": "scary monster",
    "article": "the ",
    "hp": 120,
    "power": 100
}

outside = {
    "commands": {
    },
    "description": "Fred is now in a forest",
    "inventory": [
        monster

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

slow_print("Built at Northstar!\n")

help_command([])
print('')

while True:
    time.sleep (.5)
    print('')
    print(room["description"])
    print_inventory("Things Fred sees here",room)
    hp_bar (fred["hp"],120)
    print_inventory("Inventory",fred)
    sys.stdout.write("Type a command and press enter: ")
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
        s = s.format(command)
        slow_print(command + "? " + s)

    maybewin()
# print random.random()

