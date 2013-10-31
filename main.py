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
def get (words) :
    thing = words[1]
    for item in room["inventory"] :
        if thing == item["name"] :
            fred ["inventory"].append(item)
def enter_dungeon () :
    dungeon ["inventory"].append ({ "name": "rats", "hp": 50, "power": 50})
def kill(words) :
    global room
    for item in room["inventory"] :
        if "hp" in item :
            if 70 < random.randint (1,100):
                dam = random.randint(fred ["power"] /2, fred ["power"])
                item["hp"] = item["hp"] - dam
                print("you hit the {0} for {1} hp".format(item["name"],dam))
                if item["hp"] < 1 :
                    print("the {0} dies".format (item ["name"]))
                    del item["hp"]
                    item["name"] = "corpse of " + item["name"]

            else:
                print ("you missed")
            if "hp" in item: #if he's still alive
                if random.randint(1,100) > 25:
                    dam = random.randint(item ["power"] /2, item ["power"])
                    fred["hp"] = fred["hp"] - dam
                    print("the {0} hits you for {1} hp".format(item["name"], dam))
                    if fred["hp"] < 1 :
                        print("you die")
                        exit ()
                    else:
                        if room == outside and random.randint(1,100) > 25:
                            print (" the blow knocks you back and you fall back in the dungeon")
                            change_room (dungeon)
                else:
                    print("the {0} misses".format (item["name"]))
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
    "name": "fred",
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
        { "name": "scary monster", "hp": 120, "power": 100 }
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

