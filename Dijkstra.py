# Python program for Dijkstra's single source 
# shortest path algorithm.
from heapq import heappush, heappop
from collections import defaultdict 

# Class to represent a graph 
class Graph: 

    def __init__(self, vertices): 
        self.V = vertices # No. of vertices 
        self.graph = [] # default dictionary to store graph 

	# function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
		
	# utility function used to print the solution 
    def printArr(self, dist): 
        print("Vertex Distance from Source") 
        for i in range(self.V): 
            print("% d \t\t % d" % (i, dist[i]))
    
    # The main function that finds shortest distances from src to 
	# all other vertices using Dijkstra's algorithm.
    def Dijkstra(self, source):
        distances = {}
        predecessors = {}
        seen = {source: 0} # seen is a dictionary with 
        priority_queue = [(0, source)]

        while priority_queue:
            v_dist, vertex = heappop(priority_queue) # 
            distances[vertex] = v_dist # 

            for w in self.graph[vertex]: # Iterate over every vertex in the graph
                vw_dist = distances[vertex] + 1
                if w not in seen or vw_dist < seen[w]:
                    seen[w] = vw_dist
                    heappush(priority_queue, (vw_dist,w))
                    predecessors[w] = vertex

        self.printArr(distances)


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
# Print the solution 
g.Dijkstra(0)


#print(g) # {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}
#print(dijkstra(g,'A'))# {'A': 0, 'B': 1, 'C': 1, 'D': 2}, {'B': 'A', 'C': 'A', 'D': 'B'}


