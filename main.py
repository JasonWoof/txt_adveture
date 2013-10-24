import sys 
import random

room = {}
word = "yes"

def esc() :
    global room
    print("you escaped the dungeon you get 50 points")
    room = outside
def change_room() :
    global room
    print("you go outside")
    room = outside
def attack() :
    print("you do some damage")
souls = {
    "jump": "you jumped " + str(random.randint(6,20)) + " inches"
}
def kill() :
    for item in room["inventory"] :
        if "hp" in item :
            if 70 < random.randint (1,100):
                dam = random.randint(50,100)
                item["hp"] = item["hp"] - dam
                if item["hp"] < 1 :
                    print("the monster dies")
                    del item["hp"]
                    item["name"] = "corpse of " + item["name"] 
                else :
                    print("you hit for {0} hp".format(dam))
            else:
                print ("you mised")
            if "hp" in item: #if he's still alive
                if random.randint(1,100) > 25:
                    print("u got your *** kicked")
                else:
                    print("that dumb *** monster missed")
            return
    print("nothing to kill here")
    
commands = {
    "kill": kill,
}

dungeon = {
    "commands": {
        "esc": esc,
        "change": change_room
    },
    "description": "you are in a dungeon you have a broadsword a dirk and some armor what do you do",
    "inventory": [
        { "name": "ladder" },
        { "name": "rats"},
        { "name": "rusty old sword"}
    ]
}

outside = {
    "commands": {
        "attack": attack
    },
    "description": "you are now in a forest",
    "inventory": [
        { "name": "scary monster", "hp": 120 }
    ]
}

room = dungeon

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
    command = sys.stdin.readline().strip()
    words = command.split(' ')
    verb = words[0]
    if verb in room["commands"]:
        room["commands"][verb]()
    elif verb in commands:
        commands[verb]()
    elif verb in souls:
        print(souls[verb])
    else:
        s = sass[random.randint(0, len(sass) - 1)]
        s = s.format (command)
        print(command + "? " + s)

# print random.random()

