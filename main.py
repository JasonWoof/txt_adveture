import sys 
import random

room = {}
word = "yes"

def esc(words) :
    global room
    print("you escaped the dungeon you get 50 points")
    change_room (outside)
def change_room (dest) :
    global room
    room = dest
    if "on_enter" in room :
        room["on_enter"]()
def attack(words) :
    print("you do some damage")
def climb (words) :
    global room
    print("you climbed out of the dungeon")
    change_room (outside)
def swing (attacker, defender) :
    if 70 < random.randint (1,100):
        dam = random.randint(attacker ["power"] /2, attacker ["power"])
        defender["hp"] = defender["hp"] - dam
        print("{0} hit {1}{2} for {3} hp".format(attacker["name"], defender["article"], defender["name"], dam))
        if defender["hp"] < 1 :
            print("the {0} dies".format (defender ["name"]))
            del defender["hp"]
            defender["name"] = "corpse of " + defender["name"]
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
                return 
def enter_dungeon () :
    dungeon ["inventory"].append ({ "name": "rats","article": "the ", "hp": 50, "power": 50})
def kill(words) :
    for item in room["inventory"] :
        if "hp" in item :
            swing(fred, item)
            if "hp" in item: #if he's still alive
                swing(item, fred)
                if fred["hp"] < 1 :
                    print("you die")
                    exit ()
                else: # monster just hit you
                    if room == outside and random.randint(1,100) > 25:
                        print ("the blow knocks you back and you fall back in the dungeon")
                        change_room (dungeon)
            return
    print("nothing to kill here")
souls = {
    "jump": "you jumped " + str(random.randint(6,20)) + " inches"
}
commands = {
    "kill": kill,
    "get": get,
    "take": get
}

dungeon = {
    "commands": {
        "esc": esc,
        "climb": climb
    },
    "on_enter": enter_dungeon,
    "description": "you are in a dungeon you have a broadsword a dirk and some armor what do you do",
    "inventory": [
        { "name": "ladder" },
        { "name": "rusty old sword"}
    ]
}
fred = {
    "article": "",
    "name": "you",
    "hp": 120,
    "power": 100,
    "inventory": []
}

outside = {
    "commands": {
        "attack": attack
    },
    "description": "you are now in a forest",
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

while True:
    print()
    print(room["description"])
    stuff = []
    for item in room["inventory"] :
        stuff.append(item["name"])
    print("things you see here: " + ", ".join(stuff))
    stuff = []
    for item in fred["inventory"] :
        stuff.append(item["name"])
    print("you have: " + ", ".join(stuff))
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

