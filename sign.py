def sign (text):
    width = len(text)+6
    hight = 5
    for x in range(0, hight):
        if x == 0 or x == hight - 1:
            print ("#"*width)
        elif x == 2:
            print ("#  " + text + "  #")
        else:
            spaces = width - 2
            print ("#" + (" " * spaces) + "#")
sign ("hi")
sign ("you stole my baby")
sign ("i like cheese")

print ("########")
print ("#      #")
print ("#  hi  #")
print ("#      #")
print ("########")

