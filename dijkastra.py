import sys;

class Graph():
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[0 for column i range(vertices)] for row in range(vertices)]
    
    def solution(self, distance):
        for node in range(self.V):
            print(node, distance[node])

    

    def minDistance(self, distance, setVertices):
        min = sys.maxsize