lineAmount = 5
space = int(lineAmount / 2)
stars = 1

for a in range(lineAmount):
    dir = -1
    if a < int(lineAmount / 2):
        dir = 1

    for b in range(space):
        print(" ", end = "")
    space = space - 1 * dir
    for c in range(stars):
        print("x", end = "")
    stars = stars + 2 * dir
    print("")
#for d in range(3):
#    for e in range(space):
#        print(" ", end = "")
#    space = space + 1
#    for f in range(stars):
#        print("x", end = "")
#    stars = stars - 2
#    print("")