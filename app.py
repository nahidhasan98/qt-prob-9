# getting the number of path/connection/distances
totalPath = int(input("First enter the number of distances: "))

# innitializing default value
maxDistance = -1
startingPos = 0
paths = []

# taking input
for i in range(totalPath):
    cityFrom = input()
    cityTo = input()
    distance = int(input())

    paths.append({"from": cityFrom, "to": cityTo, "distance": distance})

    if distance > maxDistance:
        maxDistance = distance
        startingPos = i

# taking input done
# we got the starting position/city

# now traversing from starting city
visitingSequence = []
shortestDistance = 0

# taking starting city
visitingSequence.append(paths[startingPos]["to"])

# now traversing the right part
for i in range(startingPos+1, totalPath):
    visitingSequence.append(paths[i]["to"])
    shortestDistance += paths[i]["distance"]

# now traversing the left part
for i in range(0, startingPos):
    visitingSequence.append(paths[i]["to"])
    shortestDistance += paths[i]["distance"]

# printing result
# shortest route
print("Shortest route:")
for i in range(len(visitingSequence)):
    print(visitingSequence[i], end='')

    if i != len(visitingSequence)-1:
        print(" -> ", end='')
print()

# shortest distance
print("Shortest distance =", shortestDistance)


# input:
"""
20
Rabat
Sueca
1063
Sueca
Rudow
2656
Rudow
Mosu
1352
Mosu
Le Plessis Trevise
1841
Le Plessis Trevise
Kang Dong
61
Kang Dong
Nezahualcóyotl
1634
Nezahualcóyotl
Lindenwold
151
Lindenwold
Queanbeyan
285
Queanbeyan
Saint Chamond
146
Saint Chamond
Cheektowaga
11
Cheektowaga
Tirupati
380
Tirupati
Snezhinsk
2547
Snezhinsk
Glazov
2524
Glazov
Gaoyou
97
Gaoyou
Nola
6999
Nola
Rutigliano
63
Rutigliano
Colombo
105
Colombo
Meckenheim
244
Meckenheim
Hamburg
502
Hamburg
Rabat
30
"""