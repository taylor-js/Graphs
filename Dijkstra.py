from heapq import heappush, heappop
from collections import defaultdict 

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
                
    def dijkstra(self, source):
        distances = {}
        predecessors = {}
        seen = {source: 0}
        priority_queue = [(0, source)]

        while priority_queue:
            v_dist, VT = heappop(priority_queue)
            distances[VT] = v_dist

            for w in self.graph[VT]:
                vw_dist = distances[VT] + 1
                if w not in seen or vw_dist < seen[w]:
                    seen[w] = vw_dist
                    heappush(priority_queue, (vw_dist,w))
                    predecessors[w] = VT

        self.printArr(distances)

g = Graph(5)
g.addEdge(0, 1, 1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, 3) 
# Print the solution 
g.dijkstra(0)


#print(g) # {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}
#print(dijkstra(g,'A'))# {'A': 0, 'B': 1, 'C': 1, 'D': 2}, {'B': 'A', 'C': 'A', 'D': 'B'}


