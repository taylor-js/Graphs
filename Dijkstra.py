from heapq import heappush, heappop

def dijkstra(graph, source):
    distances = {}
    predecessors = {}
    seen = {source: 0}
    priority_queue = [(0, source)]

    while priority_queue:
        v_dist, V = heappop(priority_queue)
        distances[V] = v_dist

        for w in graph[V]:
            vw_dist = distances[V] + 1
            if w not in seen or vw_dist < seen[w]:
                seen[w] = vw_dist
                heappush(priority_queue, (vw_dist,w))
                predecessors[w] = V
    return distances, predecessors
    
g = {'A': set(['B', 'C']),
     'B': set(['A', 'D', 'E']),
     'C': set(['A', 'F']),
     'D': set(['B']),
     'E': set(['B', 'F']),
     'F': set(['C', 'E'])}

print(g) # {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}
print(dijkstra(g,'A'))# {'A': 0, 'B': 1, 'C': 1, 'D': 2}, {'B': 'A', 'C': 'A', 'D': 'B'}


