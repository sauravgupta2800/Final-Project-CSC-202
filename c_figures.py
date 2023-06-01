
import matplotlib.pyplot as plt
import numpy as np
from a_definitions import PlaylistGraph, Track
from b_operations import get_closest_connected


# the maximum length of a song title for using the legend
MAX_NAME_LEN: int = 20


# input: a title
# output: (None)
#         set the plot's title,
#         draws an x and y axes,
#         sets the labels, etc.
def setup_plot(title: str):
    # TODO
    return


# input: a graph
# output: (None)
#         plots each track's (valence, arousal) pairs
def plot_tracks(graph: PlaylistGraph, path: list):
    for i, song in enumerate(path):
        t: Track = graph.tracks[song]
        # TODO
    return


# input: a graph
# output: (None)
#         plots each track's (valence, arousal) pairs
#         and the MST with a numbered label representing
#         the order the edge was added to the MST
def plot_min_span_tree(graph: PlaylistGraph, path: list):
    # set the title
    plt.title('Stapleton - Min Span Tree')
    
    # reset the graph's connected list
    graph.connected = list()
    
    # looping over each node's ID in the found path
    for i, track in enumerate(path):
        if i + 1 >= len(path):
            break
        
        # if the root hasn't been visited yet
        if len(graph.connected) == 0:
            A: int = path[0] # the first index
            B: int = path[1] # the second index

            # point a
            p_a: np.ndarray = graph.nodes[A].point
            
            # point b
            p_b: np.ndarray = graph.nodes[B].point

            # TODO plot x1, y1
            x1, y1 = [p_a[0], p_b[0]], [p_a[1], p_b[1]]
            # TODO add the edge's number to the plot halfway between points a and b

            t: Track = graph.tracks[A]
            # TODO plot the root of the MST as a red cross

            t: Track = graph.tracks[B]
            # TODO plot the second value in the MST
            # TODO and indices A, B to the graph's connected list
        else:
            B: int = path[i + 1]
            A: int = get_closest_connected(graph, B)
            t: Track = graph.tracks[B]

            p_a: np.ndarray = graph.nodes[A].point
            p_b: np.ndarray = graph.nodes[B].point

            # TODO plot x1, y1
            x1, y1 = [p_a[0], p_b[0]], [p_a[1], p_b[1]]
            # TODO add the edge's number to the plot halfway between points a and b
            # TODO plot the track
