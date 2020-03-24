import heapq
# importing networkx  
import networkx as nx 
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt 

g = nx.Graph() 
  
g.add_edge(1, 2) 
g.add_edge(1, 5) 
g.add_edge(1, 6) 
g.add_edge(2, 3) 
g.add_edge(2, 1) 
g.add_edge(2, 7) 
g.add_edge(3, 4) 
g.add_edge(3, 2) 
g.add_edge(3, 8) 
g.add_edge(4, 5) 
g.add_edge(4, 3) 
g.add_edge(4, 9) 
g.add_edge(5, 1) 
g.add_edge(5, 4) 
g.add_edge(5, 10) 
g.add_edge(6, 1) 
g.add_edge(6, 8) 
g.add_edge(6, 9) 
g.add_edge(7, 2) 
g.add_edge(7, 9) 
g.add_edge(7, 10) 
g.add_edge(8, 3) 
g.add_edge(8, 10) 
g.add_edge(8, 6) 
g.add_edge(9, 4) 
g.add_edge(9, 6) 
g.add_edge(9, 7) 
g.add_edge(10, 5) 
g.add_edge(10, 7) 
g.add_edge(10, 8) 

nx.draw(g, with_labels = True)

plt.show()