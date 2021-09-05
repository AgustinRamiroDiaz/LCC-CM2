# %%
from graph import Graph
from copy import deepcopy
# %%


class Poset:
    def __init__(self, graph: Graph) -> None:
        self.graph = deepcopy(graph)

    def maximal_elements(self):
        result = set()
        for vertex in self.graph.getVertices():
            if not self.graph.outgoing_neighbours_of_vertex(vertex):
                result.add(vertex)

        return result

    def minimal_elements(self):
        result = set()
        for vertex in self.graph.getVertices():
            if not self.graph.incoming_neighbours_of_vertex(vertex):
                result.add(vertex)

        return result

    def has_bottom(self):
        return len(self.minimal_elements()) == 1

    def has_top(self):
        return len(self.maximal_elements()) == 1
# %%
