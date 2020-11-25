""" #Adjacency List of the Node
class AdjNode: 
    def __init__(self, data):
        self.vertex = data 
        self.next = None


#Graph to represent the adjacency lists. 

class Graph: 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]* self.V
    
    def add_edge(self, source, destination):
        
        #add node to the source
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        #Add the source node to the destination as it's a uni-direction graph 

        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list = ".format(i),end = "")
            temp = self.graph[i]
            while temp: 
                print("-> {} ".format(temp.vertex),end= "")
                temp = temp.next
            print("\n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,1)
    graph.add_edge(3,4)
    graph.add_edge(4,1)

    graph.print_graph()

 """

"""
{
    1:[2,3],
    2:[1,3],
    3:[1,2,4],
    4:[3]
}
"""

#SECOND Method:: USing dict 

class Graph: 
    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict: 
            self.graph_dict[node] = [neighbour]
        else: 
            self.graph_dict[node].append(neighbour)


    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node")



