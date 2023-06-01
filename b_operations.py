import sys
import numpy as np


# given
def get_distance(point_a: np.ndarray, point_b: np.ndarray) -> float:
    delta: float = point_a - point_b
    return np.linalg.norm(delta)


# input: a graph, a target node's index
# output: true if the target has not been visited, false otherwise
def can_visit(graph, target: int) -> bool:
    # TODO
    return False


# input: a graph, a target node's index
# output: none
#     behavior: will crash if we try to visit a node twice
def set_visited(graph, source: int, target: int):
    # TODO
    return


# input: a graph, a target node's index
# output: a row of the adjacency matrix containing the distance
#         from the current node to each other node.
def get_adjacent(graph, node_num: int) -> np.ndarray:
    # a matrix of all zeros
    tmp_matrix: np.ndarray = np.zeros(shape=(graph.n, graph.n))

    # for each row
    for i in range(graph.n):
        # for each jth column in row i
        for j in range(graph.n):
            # the main diagonal
            if j == i:
                tmp_matrix[i, j] = 0 # TODO
            
            # a node has already been visited
            elif j in graph.visited:
                tmp_matrix[i, j] = 0 # TODO
            
            # visiting a new node
            else:
                point_a: np.ndarray = graph.nodes[i].point
                point_b: np.ndarray = graph.nodes[j].point
                tmp_matrix[i, j] = 0 # TODO
    
    distances = tmp_matrix[node_num, :]
    return distances


# input: a graph, a target node's index
# output: the index of the closest node in the MST
#     note - used for reconstructing the figure
def get_closest_connected(graph, node_num: int) -> int:
    # a matrix of all zeros
    tmp_matrix: np.ndarray = np.zeros(shape=(graph.n, graph.n))

    # for each row
    for i in range(graph.n):
        # for each jth column in row i
        for j in range(graph.n):
            # if j is not connected or on the main diagonal
            if j not in graph.connected or i == j:
                tmp_matrix[i, j] = 0 # TODO
            
            # else compute the distance
            else:
                point_a: np.ndarray = graph.nodes[i].point
                point_b: np.ndarray = graph.nodes[j].point
                tmp_matrix[i, j] = 0 # TODO

    # find the shortest node
    distances: np.ndarray = tmp_matrix[node_num, :]
    result: int = np.argmin(distances)

    assert node_num not in graph.connected
    # TODO add the new node to the graph's connected list
    return result

