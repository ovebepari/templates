""" The main Graph ADT for personal use

Graph Abstarct Data Structure implementation
borrowed from geeksforgeeks. This file isn't
meant to be edited unless proven buggy.

Only for use as an imported module.

"""
from collections import defaultdict

class Graph:
    """ The Graph class

    The base ADT that will be used to create new Graph
    objects. Editing not advised.

    """

    def __init__(self):
        'Method for initializing an empty graph'
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        'Method used to add eges to the graph'
        self.graph[u].append(v)

    def addEdge_file(self, path):
        """Takes input from file.

        Path is provided by the method argument.
        Input should be provided as Adjacency List.

        """
        with open(path, 'r') as File:
            for line in File.readlines():
                ints = list(map(int, line.strip().split())) 
                u = ints[0]
                v = ints[1:]
                for i in v:
                    self.addEdge(u, i)

    def BFS(self, start):
        'Method for Bredth First Search'

        visited = [False] * (len(self.graph) + 1)

        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.pop(0)
            print(start, end=" ")

            for i in self.graph[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self, start):
        'Method for Depth First Search'

        visited = [False] * (len(self.graph) + 1)

        stack = []
        stack.append(start)
        visited[start] = True

        while stack:
            start = stack.pop()
            print(start, end=" ")

            for i in self.graph[start]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True
