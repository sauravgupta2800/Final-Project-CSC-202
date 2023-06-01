# a_definitions.py
## author - nick s.
## contains all student defined definitions

import numpy as np

class Track:
    # name: any # TODO
    # artist: any # TODO
    # artist_id: any # TODO
    # album: any # TODO
    # album_id: any # TODO
    # url: any # TODO
    # id: any # TODO
    # popularity: any # TODO
    # explicit: any # TODO
    # valence: any # TODO
    # arousal: any # TODO

    # TODO
    def __init__(self, data: dict):
        return

    def __repr__(self):
        msg: str = f'  name => {self.__getattribute__("name")}\n'
        for attr in dir(self):
            if attr[0] != '_' and attr != 'name':
                msg += f'  {attr} => {self.__getattribute__(attr)}\n'
        return msg


class Node:
    # value: type # TODO
    # point: type # TODO
    
    # TODO
    def __init__(self):
        return


class PlaylistGraph:
    # nodes: any # TODO contains the actual nodes
    # tracks: any # TODO contains the actual tracks
    
    # keeps track of nodes already visited (given)
    visited: list
    
    # records distances (given)
    matrix: np.ndarray
    
    # for reconstructing plot at the end
    connected: np.array
    
    # the number of nodes in the graphs (# of tracks)
    n: int

    def __init__(self, tracks: list):
        self.tracks = tracks
        self.nodes = list()

        for track in tracks:
            t: Track = track
            self.nodes.append(Node(t))

        n: int = len(self.nodes)
        self.matrix = np.zeros(shape=(n, n))
        self.connected = list()
        self.visited = list()
        self.n = n
        for i, v in enumerate(self.nodes):
            for j, w in enumerate(self.nodes):
                if v == w:
                    self.matrix[i, j] = 0 # sys.float_info.max
                else:
                    self.matrix[i, j] = np.linalg.norm(v.point - w.point)

    def __repr__(self):
        msg: str = str()
        for row in range(self.n):
            msg += f'{row}\t{self.matrix[row, :]}\n'
        msg += 'tracks:\n'
        for i, track in enumerate(self.tracks):
            msg += f'{i}    ({track.valence:2.2f}, {track.arousal:2.2f}) {track.name} - {track.artist}\n'
        return msg
