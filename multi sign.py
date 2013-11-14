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

sign (["hi"])
sign (["you stole my baby",
       "i'm mad at you now"])
sign (["      R.I.P.",
       "    1990-2013 ",
       "Fred F. McFredricson"])

print ("########") # x = 0
print ("#      #") # x = 1
print ("#  hi  #") # x = 2  lines[0]
print ("#  hi  #") # x = 3  lines[1]
print ("#  hi  #")
print ("#      #")
print ("########")

