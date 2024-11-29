# Algorithms

## Binary Search

Search for an element in a SORTED array by splitting the array in half and checking if the median = target

```
def binary_search(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return True
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False

//target 8, [1,2,3,4,5,6,7,8,9,10]
//[6,7,8,9,10]
//return [8]
```

## Merge Sort

Split the list in 2 halves all the way down to 1 element. Then recombines it back.

```

```

# Dijkstras

Visit all veritces and find the path with minimum distance

```py
class Graph:
	def __init__(self):
		self.graph = {}
	def add_edges(self, u, v):
		if u in self.graph:
			self.graph[u].add(v)
		else:
			self.graph[u] = {v} #set
		#add edges to both nodes
		if v in self.graph:
			self.graph[v].add(u)
		else:
			self.graph[v] = {u}

def get_min_dist_node(dict, unvisited):
	min_dist = float("inf")
    min_place = None
    for place in unvisited:
        if distances[place] < min_dist:
            min_dist = distances[place]
            min_place = place
    return min_place

```
