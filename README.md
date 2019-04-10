# Divvy Bike Project

## 1 Globally shortest path (for evaluation of our method)
### 1) use time to weight edge
### 2) use distance to weight edge

## 2 Locally shortest path
**(Input: starting station s, destination station d)
**(Output: path, distance and time for each edge in the path)
### Algorithm: 
#### 1. Create a graph from the time matrix and distance matrix
#### 2. Initialization: set next station as (s)
- 1). Find all the stations which can be reached in 30 minutes from the station (s), and put them in a set (P) (excludes s)
- 2). Find the station (m) which is closest to the destination station (d) from the set (P)
-  3). Set s = m
- Repeat 1) to 3) until s == d, which means the next station (s) is the destination station (d)


