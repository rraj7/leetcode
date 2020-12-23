import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'Y'))




package main

import (	"fmt"	"sort"	"strconv")

type Graph struct {	Edges []*Edge	
	Nodes []*Node}

type Edge struct {	Source *Node
		Destination  *Node	Weight   int
	}

type Node struct {	Name string }

const Infinity = int(^uint(0) >> 1)

func (g *Graph) AddEdge(Source, Destination *Node, Weight int) {
	edge := &Edge{
		Source: Source,
		Destination:  Destination,
		Weight:   Weight,
	}

	g.Edges = append(g.Edges, edge)
	g.AddNode(Source)
	g.AddNode(Destination)
}


func (g *Graph) AddNode(node *Node) {
	var ifNodeExists bool
	for _, n := range g.Nodes {
		if n == node {
			ifNodeExists = true
		}
	}

	if !ifNodeExists {
		g.Nodes = append(g.Nodes, node)
	}
}


func (g *Graph) String() string {
	var s string

	s += "Edges:\n"
	for _, edge := range g.Edges {
		s += edge.Source.Name + " -> " + edge.Destination.Name + " = " + strconv.Itoa(edge.Weight)
		s += "\n"
	}
	s += "\n"

	s += "Nodes: "
	for i, node := range g.Nodes {
		if i == len(g.Nodes)-1 {
			s += node.Name
		} else {
			s += node.Name + ", "
		}
	}
	s += "\n"

	return s
}


func (g *Graph) Dijkstra(startNode *Node) (shortestPathTable string) {


	WeightTable := g.NewWeightTable(startNode)

	
	var visited []*Node

	
	for len(visited) != len(g.Nodes) {

	
		node := getClosestNonVisitedNode(WeightTable, visited)

	
		visited = append(visited, node)

	
		nodeEdges := g.GetNodeEdges(node)

		for _, edge := range nodeEdges {
		distanceToNeighbor := WeightTable[node] + edge.Weight


			if distanceToNeighbor < WeightTable[edge.Destination] {
				WeightTable[edge.Destination] = distanceToNeighbor
			}
		}
	}

	for node, Weight := range WeightTable {
		shortestPathTable += fmt.Sprintf("Shortest Distances from points %s to %s = %d\n", startNode.Name, node.Name, Weight)
	}

	return shortestPathTable
}
func (g *Graph) NewWeightTable(startNode *Node) map[*Node]int {
	WeightTable := make(map[*Node]int)
	WeightTable[startNode] = 0

	for _, node := range g.Nodes {
		if node != startNode {
			WeightTable[node] = Infinity
		}
	}

	return WeightTable
}

func (g *Graph) GetNodeEdges(node *Node) (edges []*Edge) {
	for _, edge := range g.Edges {
		if edge.Source == node {
			edges = append(edges, edge)
		}
	}

	return edges
}

func getClosestNonVisitedNode(WeightTable map[*Node]int, visited []*Node) *Node {
	type WeightTableToSort struct {
		Node *Node
		Weight int
	}
	var sorted []WeightTableToSort


	for node, Weight := range WeightTable {
		var isVisited bool
		for _, visitedNode := range visited {
			if node == visitedNode {
				isVisited = true
			}
		}

		if !isVisited {
			sorted = append(sorted, WeightTableToSort{node, Weight})
		}
	}
	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i].Weight < sorted[j].Weight
	})

	return sorted[0].Node
}

func main() {
	a := &Node{Name: "Kruthika's abode"}
	b := &Node{Name: "Brian's apartment"}
	c := &Node{Name: "Greg's casac"}
	d := &Node{Name: "Wesley's condo"}
	e := &Node{Name: "Matt's pad"}
	f := &Node{Name: "Mark's crib"}
	g := &Node{Name: "Bryce's den"}
	h := &Node{Name: "Mike's digs"}
	i := &Node{Name: "Cam's dwelling"} 
	j := &Node{Name: "Nathan's flat"}

	graph := Graph{}
	graph.AddEdge(a, c, 9)
	graph.AddEdge(a, b, 4)
	graph.AddEdge(c, b, 18)
	graph.AddEdge(c, d, 8)
	graph.AddEdge(b, d, 4)
	graph.AddEdge(d, e, 2)
	graph.AddEdge(d, g, 30)
	graph.AddEdge(d, f, 10)
	graph.AddEdge(f, g, 1)
	graph.AddEdge(g, f, 2)
	graph.AddEdge(h, i, 4)


	fmt.Println(graph.Dijkstra(a))
}