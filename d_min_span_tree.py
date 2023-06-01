import matplotlib.pyplot as plt
import utils
import numpy as np
import matplotlib.pyplot as plt

from a_definitions import PlaylistGraph
from b_operations import get_adjacent
from b_operations import can_visit, set_visited
from c_figures import setup_plot
from c_figures import plot_tracks, plot_min_span_tree


def print_keys_of_dataset(data: dict):
    print('keys inside of dict...')
    for k in data.keys():
        print(f'    {k}')


# parameters
MAX_NAME_LEN = 20
FILE_PATH = 'data/weekly_playlist.json'
FIGURE = 'figs/test.png'
START_IDX: int = 12
END_IDX: int = 20


# step 0 - load the data
data: dict = utils.load_tracks(FILE_PATH, start_idx=START_IDX, end_idx=END_IDX)
print_keys_of_dataset(data)
utils.print_dataset(data)
graph = PlaylistGraph(data['tracks'])


# step 1 - initializing parameters
init_song: int = 0
set_visited(graph, init_song, init_song)
search_space = None # TODO
path = None


# step 3 - connecting nodes to the MST
while len(search_space) > 0:
    path = search_space.pop()

    # source is the previously visited node
    source = None # TODO
    
    # get the distances to each neighbor
    neighbors = None # TODO

    # grab the closest neighbor's index
    min_idx: int = np.argmin(neighbors)

    # if we can visit there....
    if can_visit(graph, min_idx):
        print(f'{neighbors} : {min_idx}')
        # set the closest neighbor to visited
        # add the closest neighbor to the path
        # add the path back into the search space


# printing the result
print(path)

# step 3 - making the figures
setup_plot('Stapleton - Tracks')
# plot_tracks(graph, path) # TODO
# plot_min_span_tree(graph, path) # TODO

# step 4 - profit
