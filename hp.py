import math
# [******   ]

def hp_bar (current,full):
    out = "hp: ["
    stars = int(math.ceil(current/4.0))
    spaces = int(math.ceil(full /4.0))
    spaces -= stars
    out += "*" * stars
    out += " " * spaces
    out += "]"
    print (out)



hp_bar (100,100)
hp_bar (10,100)
hp_bar (1,100)
hp_bar (0,100)
