from collections import defaultdict

def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)): 
        for j in range(len(a[i])): 
            if a[i][j]== 1: 
                adjList[i].append(j) 
    return adjList 

a = [
     [0, 1, 0, 0, 0, 0, 0, 1, 0], 
     [1, 0, 1, 0, 0, 0, 0, 1, 0], 
     [0, 1, 0, 1, 0, 1, 0, 0, 1], 
     [0, 0, 1, 0, 1, 1, 0, 0, 0], 
     [0, 0, 0, 9, 0, 1, 0, 0, 0], 
     [0, 0, 1, 1, 1, 0, 1, 0, 0], 
     [0, 0, 0, 0, 0, 1, 0, 1, 1], 
     [1, 1, 0, 0, 0, 0, 1, 0, 1], 
     [0, 0, 1, 0, 0, 0, 1, 1, 0] 
]

AdjList = convert(a) 
print("Adjacency List:") 
# print the adjacency list 
for i in AdjList: 
	print(i, end ="") 
	for j in AdjList[i]: 
		print(" -> {}".format(j), end ="") 
	print() 

