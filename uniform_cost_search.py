from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self, directed): 
        """True if Graph is directed otherwise it takes False"""
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        """Add Edges between two nodes along 
        with weight as Algorithm is of UCS"""
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        """Takes the two nodes as parameters and returns UCS PATH"""
        visited = []  
        queue = PriorityQueue()
        queue.put((0, current_node))
        
        while not queue.empty():
            item = queue.get()
            current_node =  item[1]

            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                    
                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))



g = Graph(False)

g.graph =  defaultdict(list)
g.add_edge('J', 'K', 146)
g.add_edge('J', 'E', 105)
g.add_edge('J', 'I', 172)
g.add_edge('I', 'C', 102)
g.add_edge('I', 'A', 109)
g.add_edge('C', 'D', 126)
g.add_edge('C', 'B', 171)
g.add_edge('G', 'C', 140)
g.add_edge('G', 'D', 123)
g.add_edge('F', 'G', 88)
g.add_edge('F', 'H', 130)
g.add_edge('G', 'H', 99)
g.add_edge('K', 'L', 152)
g.add_edge('L', 'O', 97)
g.add_edge('O', 'M', 100)
g.add_edge('M', 'N', 67)
g.add_edge('H', 'N', 80)
g.add_edge('D', 'F', 111)
g.add_edge('A', 'D', 43)
g.add_edge('D', 'F', 111)
g.add_edge('E', 'A', 133)
g.add_edge('K', 'E', 146)
g.add_edge('E', 'L', 110)
g.add_edge('A', 'O', 151)
g.add_edge('D', 'O', 136)
g.add_edge('D', 'M', 200)


print("Uniform Cost Search:")
g.ucs('J', 'N')



