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
"""
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

"""



# Create a graph 
# now create a dict with graph elements: 
graph_element = {"a":["b","c"],"b":["a","d"],"c" : ["a", "d"],"d" : ["e"], "e" : ["d"]}


#Dispaly 

class graph():
    def __init__(self, gdict):
        if gdict is None: 
            gdict = []
        self.gdict = gdict

    def getvertices(self):
        return list(self.gdict.keys())

    def getedges(self):
        edgename = []
        for v in self.gdict:
            for nv in self.gdict[v]:
                if {nv,v} not in edgename:
                    edgename.append({v,nv})
        return edgename
    
    def addEdge(self, edge):
        edge = set(edge)
        v1,v2 = tuple(edge)
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else: 
            self.gdict[v1] = [v2]


g = graph(graph_element)
g.addEdge({"a","c"})
g.addEdge({"a","e"})

print(g.getedges())