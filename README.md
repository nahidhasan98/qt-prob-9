## Problem:
- Given some pair of cities and distances between them, the problem is to find the shortest possible route with distance that visits every city exactly once.
- City 1 [Rabat] can be considered as the starting point.
- Since the route is cyclic, we can consider any point as a starting point.

  

## Todo:
We have to find out
- the shortest possible route and
- the distance

where, every cities is visited exactly once.

  
## Perception:
- Since the route is cyclic, so we can start from any city which will give us best result
- and visit one by one and go through all other cities until we reaches the previous one we started from.

##### For example:
If there are 4 cities ( A, B, C, D ),
```
A ------ B
|        |
|        |
D ------ C
```
- we can start from ```A``` and visit like: 
-- ```A -> B -> C -> D``` (clockwise) or ```A -> D -> C -> B``` (anti-clockwise).

or

- we can start from ```B``` and visit like:
-- ```B -> C -> D -> A``` (clockwise) or ```B -> A -> D -> C``` (anti-clockwise).

or 

vice-versa.

So, we can see that, we have to eliminate exactly one distance from given set of distance. As we want to minimize the distance, so it is clear to eliminate a bigger distance to get the best result.

## Idea for Solution:
We will take input and determine the maximum distance that have between two cities. We will eliminate this distance means we will not go through between these two cities as it will give us higher cost. So, we will avoid this route.
And we will start from any one city between these two cities and will traverse towards the lower cost distances.

## Implementation:
Solution provided in ```app.py``` file.

## Run the code:
Simply run the code using the following command 
```bash
py app.py
```
Then input the routes with distances one by one. After providing the input, it will output the result in the console.
