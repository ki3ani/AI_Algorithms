from collections import deque

class Graph:
   

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristics
    def h(self, n):
        H = {
        'A': 221,
        'B': 350,
        'C': 400,
        'D': 326,
        'E': 500,
        'F': 209,
        'G': 188,
        'H': 92,
        'I': 499,
        'J': 621,
        'K': 668,
        'L': 300,
        'M': 78,
        'N': 0,
        'O': 170
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
      

        open_list = set([start_node]) #open_list for nodes that have been visited but not yet explored
        closed_list = set([]) #closed_list for nodes that have already been visited and explored

     
        g = {} #distances to start node

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('A_Star Search: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

#Driver_Code

graph_nodes = {
    'J':[('K',146),('E',105),('I',172)],
    'K':[('E',146),('L',152)],
    'E':[('A',133),('L',110)],
    'I':[('A',109),('C',102)],
    'A':[('O',151),('D',43)],
    'C':[('D',126),('B',171)],
    'G':[('C',140),('D',123)],
    'B':[('G',171)],
    'F':[('G',88),('H',130)],
    'D':[('O',136),('M',200),('F',111)],
    'H':[('N',80)],
    'L':[('O',97)],
    'O':[('M',100)],
    'M':[('N',67)],
}

graph1 = Graph(graph_nodes)

graph1.a_star_algorithm('J', 'N')

