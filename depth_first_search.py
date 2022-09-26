#Adm no 112827




graph1 = {
    'J':['K','E','I'],
    'K':['E','L'],
    'E':['A','L'],
    'I':['A','C'],
    'A':['O','D'],
    'C':['D','B'],
    'G':['C','D'],
    'B':['G'],
    'F':['G','H'],
    'D':['O','M','F'],
    'H':['N'],
    'L':['O'],
    'O':['M'],
    'M':['N'],
    'N':[]
}
 
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph,k, visited)
    return visited
 
visited = dfs(graph1,'J', [])
print("Depth First Search:",visited)