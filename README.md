# Divvy Bike Project

## 1 Globally shortest path (for evaluation of our method) (GSP)
Use Bellman-Ford shortest path algorithm
#### Input: 
##### For distance based shortest path:
*distance matrix, starting station, destination station*
##### For time based shortest path:
*time matrix, starting station, destination station*
#### Output: 
*shortest path and the shortest distance (or time)*


## 2 Locally shortest path (LSP)
#### Input: 
*distance matrix, time matrix, starting station s, destination station d*
#### Output: 
*path, distance for each edge in the path, time for each edge in the path*
### Algorithm: 
#### 1. Create a graph from the time matrix and distance matrix
#### 2. Initialization: set next station as (s)
- 1). Find all the stations which can be reached in 30 minutes from the station (s), and put them in a set (P) (excludes s)
- 2). Find the station (m) which is closest to the destination station (d) from the set (P)
- 3). Set s = m, and repeat 1) to 2) until s == d, which means the next station (s) is the destination station (d)


## 3 Evaluation of Our Algorithm (Compare with GSP algorithm)
There are 41609 pairs of stations which are far away more than 30 minutes.
#### Comparasion with distance based GSP
- 1). Average travelling distance: LSP - GSP = 0.48566 kilometers.
- 2). Average travelling time: LSP - GSP = -3.35 minutes.
#### Comparasion with time based GSP
- 1). Average travelling distance: LSP - GSP = -2.88435 kilometers.
- 2). Average travelling time: LSP - GSP = 11.59 minutes.
