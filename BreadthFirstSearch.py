# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
from heapq import heappush, heappop
# This class represents a directed graph 
# using adjacency list representation 
class Graph:

	# Constructor 
    def __init__(self,vertices): 
		# default dictionary to store graph 
        self.V = vertices # No. of vertices 
        self.graph = [] # default dictionary to store graph 
        #self.graph = defaultdict(list) 
	# function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
		#self.graph[u].append(v) 

	# Function to print a BFS of graph 
    def BreadthFirstSearch(self, s):
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph))
        # Create a queue for BFS 
        queue = [] 
        # Mark the source node as 
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True

        while queue: 

            # Dequeue a vertex from 
            # queue and print it 
            s = queue.pop(0) 
            print(s, end = " ") 

            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

# Driver code 

# Create a graph given in 
# the above diagram 
g = Graph(6)
g.addEdge(0, 1, 3)
g.addEdge(0, 2, 2)
g.addEdge(1, 2, 4)
g.addEdge(1, 4, 1)
g.addEdge(1, 3, 5)
g.addEdge(2, 4, 3)
g.addEdge(3, 4 ,7)
g.addEdge(4, 6, 2)
g.addEdge(5, 1, 1)
g.addEdge(5, 6, 8)
print("Following is Breadth First Traversal (starting from vertex 2)") 
g.BreadthFirstSearch(0) 