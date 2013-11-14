def square (size):
    width = size * 2
    for x in range(0, size):
        if x == 0 or x == size - 1:
            print ("#"*width)
        else:
            spaces = width - 2
            print ("#" + (" " * spaces) + "#")
square (4)
square (10)
square (15)

print ("######")
print ("#    #")
print ("#    #")
print ("######")
