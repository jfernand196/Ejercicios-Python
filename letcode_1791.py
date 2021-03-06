# There is an undirected star graph consisting of n nodes labeled from 1 to n. 
# A star graph is a graph where there is one center node and exactly n - 1 edges that connect 
# the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is
#  an edge between the nodes ui and vi. Return the center of the given star graph.

#  Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
#  Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
# Example 2:

# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

edges = [[1,2],[2,3],[4,2]]
cont = 0
cont1 = 0
for i in range(len(edges)):
    for o in [0,1]:
        if edges[0][0] == edges[i][o]:
            cont +=1
        elif edges[0][1] == edges[i][o]:
            cont1 +=1
if cont > cont1:
    print(edges[0][0])
else:
    print(edges[0][1])

# Solucion 2

# print(edges[0][0]) if edges[0][0] in edges[1] else print(edges[0][1])

#Solucion 3

# e1 = edges[0]
# e2 = edges[1]
# if e1[0] in e2:
#     print(e1[0])
# print(e1[1])
