# Divvy Bike Project

## 1 Globally shortest path (for evaluation of our method)
### 1) use time to weight edge
### 2) use distance to weight edge

## 2 Locally shortest path
Algorithm:
1. Set starting station as s
2. Find all the stations which can be reached in 30 minutes from the station (s), and put them in a set (P) as well as th starting station
3. Find the station m which is closest to the destination station (d)
   if( m is the starting station):
       return the shortest path (s -> d)
   else:
       return (set m as s, repeat 2, 3)
       

# To be continued
