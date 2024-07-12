from SPClient import SPClient
from MusicMap import MusicMap

TRACKS_MAX_RANGE = 1000

def main():
    spc = SPClient()
    map = MusicMap()

    map.add_tracks(spc.get_user_saved_tracks(TRACKS_MAX_RANGE))
    map.print_artist_tracks()

main()
