"""
    Helper functions for the eventual portfolio
"""
import spotipy


def get_playlist_tracks(playlist, sp, batch_size = 100, offset = 0):
    tracks = []
    while True:
        new_tracks = sp.playlist_tracks(playlist, fields='items', limit=batch_size, offset=offset, )['items']
        if not len(new_tracks):
            break
        tracks += [t["track"] for t in new_tracks]
        offset += batch_size
    return tracks


def get_playlist_audio_features(playlist, sp):
    tracks = get_playlist_tracks(playlist, sp)
    track_name_id = dict([(track['name'], track['id']) for track in tracks])

    track_names = track_name_id.keys()
    track_audio_features = sp.audio_features(list(track_name_id.values()))

    playlist_audio_features = dict(zip(track_names, track_audio_features))
    return playlist_audio_features
