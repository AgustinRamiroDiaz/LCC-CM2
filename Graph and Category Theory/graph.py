# %%
from abc import ABC


# %%


class Graph(ABC):
    def addVertex(self, vertex):
        raise NotImplementedError

    def addEdge(self, edge):
        raise NotImplementedError

    def incoming_neighbours_of_vertex(self, vertex):
        raise NotImplementedError

    def outgoing_neighbours_of_vertex(self, vertex):
        raise NotImplementedError

    def getVertices(self):
        raise NotImplementedError

    def searchShortestPath(self, initialVertex, finalVertex):
        queue = [[initialVertex]]
        while queue:
            path = queue.pop(0)
            if path[-1] == finalVertex:
                return path
            else:
                lastVertexNeighbours = self.outgoing_neighbours_of_vertex(
                    path[-1])
                for neighbour in lastVertexNeighbours:
                    if neighbour not in path:
                        queue.append(path + [neighbour])

        return None


class DefaultGraph(Graph):
    def __init__(self, vertices: set, edges: set) -> None:
        self.vertices = vertices
        self.edges = edges
        assert(self.edgesConsistency())

    def getVertices(self):
        return self.vertices

    def edgesConsistency(self):
        for edge in self.edges:
            if edge[0] not in self.vertices or edge[1] not in self.vertices:
                print(f'This edge iw wrong :( {edge}')
                return False
        return True

    def incoming_neighbours_of_vertex(self, vertex):
        neighbours = set()
        for edge in self.edges:
            if vertex == edge[1]:
                neighbours.add(edge[0])
        return neighbours

    def outgoing_neighbours_of_vertex(self, vertex):
        neighbours = set()
        for edge in self.edges:
            if vertex == edge[0]:
                neighbours.add(edge[1])
        return neighbours

    def addVertex(self, vertex):
        self.vertices.add(vertex)

    def addEdge(self, edge):
        assert(edge[0] not in self.vertices or edge[1] not in self.vertices)
        self.edges.add(edge)

    def removeVertex(self, vertex):
        self.vertices.discard(vertex)
        edgesToRemove = []
        for edge in self.edges:
            if edge[0] == vertex or edge[1] == vertex:
                edgesToRemove.append(edge)
        for edge in edgesToRemove:
            self.edges.remove(edge)

    def removeEdge(self, edge):
        self.vertices.discard(edge)

    def reverse(self):
        reversed_edges = {edge[::-1] for edge in self.edges}

        return DefaultGraph(self.vertices, reversed_edges)
