import sys

from matrix import Matrix  # Assuming matrix.py is in the same directory


class Graph:
    """
    A simple Graph class using an adjacency matrix for representation.
    Assumes unweighted graphs for Boolean Matrix Multiplication purposes.
    """

    def __init__(self, num_nodes, directed=False):
        """
        Initializes a graph with a given number of nodes.
        Nodes are 0-indexed (0 to num_nodes-1).
        num_nodes: The number of nodes in the graph.
        directed: True if the graph is directed, False otherwise (default).
        """
        if not isinstance(num_nodes, int) or num_nodes <= 0:
            raise ValueError("Number of nodes must be a positive integer.")

        self.num_nodes = num_nodes
        self.directed = directed
        # Initialize adjacency matrix with all zeros
        self.adj_matrix = Matrix(
            [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        )

    def add_edge(self, u, v):
        """
        Adds an edge between node u and node v.
        For unweighted graphs, we set the entry to 1.
        u, v: Node indices (0-indexed).
        """
        if not (0 <= u < self.num_nodes and 0 <= v < self.num_nodes):
            raise IndexError(
                f"Nodes {u}, {v} are out of bounds for {self.num_nodes} nodes."
            )

        self.adj_matrix[u][v] = 1
        if not self.directed:
            self.adj_matrix[v][u] = (
                1  # For undirected graphs, add edge in both directions
            )

    def remove_edge(self, u, v):
        """
        Removes an edge between node u and node v.
        u, v: Node indices (0-indexed).
        """
        if not (0 <= u < self.num_nodes and 0 <= v < self.num_nodes):
            raise IndexError(
                f"Nodes {u}, {v} are out of bounds for {self.num_nodes} nodes."
            )

        self.adj_matrix[u][v] = 0
        if not self.directed:
            self.adj_matrix[v][u] = 0

    def has_edge(self, u, v):
        """
        Checks if an edge exists between node u and node v.
        Returns True if an edge exists, False otherwise.
        """
        if not (0 <= u < self.num_nodes and 0 <= v < self.num_nodes):
            raise IndexError(
                f"Nodes {u}, {v} are out of bounds for {self.num_nodes} nodes."
            )
        return self.adj_matrix[u][v] == 1

    def get_adjacency_matrix(self):
        """Returns the adjacency matrix of the graph."""
        return self.adj_matrix

    def __str__(self):
        """Returns a string representation of the graph's adjacency matrix."""
        s = f"Graph (Nodes: {self.num_nodes}, Directed: {self.directed})\n"
        s += "Adjacency Matrix:\n"
        s += str(self.adj_matrix)
        return s


# Basic test for Graph class (if run directly)
if __name__ == "__main__":
    print("--- Testing Graph Class ---")

    # Undirected Graph
    g_undirected = Graph(4)
    g_undirected.add_edge(0, 1)
    g_undirected.add_edge(1, 2)
    g_undirected.add_edge(2, 3)
    g_undirected.add_edge(0, 3)  # Added a cycle
    print(g_undirected)
    print(f"Has edge (0, 1)? {g_undirected.has_edge(0, 1)}")  # Expected: True
    print(
        f"Has edge (1, 0)? {g_undirected.has_edge(1, 0)}"
    )  # Expected: True (undirected)
    print(f"Has edge (0, 2)? {g_undirected.has_edge(0, 2)}")  # Expected: False

    print("\n--- Testing Directed Graph ---")
    g_directed = Graph(3, directed=True)
    g_directed.add_edge(0, 1)
    g_directed.add_edge(1, 2)
    print(g_directed)
    print(f"Has edge (0, 1)? {g_directed.has_edge(0, 1)}")  # Expected: True
    print(f"Has edge (1, 0)? {g_directed.has_edge(1, 0)}")  # Expected: False (directed)
