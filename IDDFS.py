graph = {
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

path = list()

def DFS(currentNode,destination,graph,maxDepth,curList):
    print("Checking for destination",currentNode)
    curList.append(currentNode)
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,graph,i,curList):
            return True
    return False
#Setup a limit aswell
if not iterativeDDFS('J','N',graph,10):
    print("Path is not available")
else:
    print("A path has been found")
    print("The IDDFS path is:",path.pop())