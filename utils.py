import json
from a_definitions import Track


def load_file(file_path: str) -> dict:
    file = open(file_path)
    data = json.load(file)
    file.close()

    tracks = [ Track(data['tracks'][i]) for i in range(len(data['tracks']))]
    data['tracks'] = tracks
    return data


def load_tracks(file_path: str = 'data/weekly_playlist.json',
                start_idx: int=0, end_idx: int=0) -> dict:
    data: dict = load_file(file_path)
    n: int = len(data['tracks'])

    if start_idx >= n or start_idx < 0:
        start_idx = 0
    if end_idx >= n or end_idx < start_idx:
        end_idx = n;

    data['tracks'] = data['tracks'][start_idx:end_idx]
    print_dataset(data)
    return data


def print_dataset(data: dict):
    for key, value in data.items():
        if not isinstance(value, list):
            print(f'{key} => {value}')
        else:
            print(f'{key} =>')
            for track in value:
                print(track)
