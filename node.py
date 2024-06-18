from enum import Enum


class NodeColors(Enum):
    GRAY = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5
    INDIGO = 6
    PURPLE = 7

class Node():
    __id_index = 0

    def __init__(self):
        Node.__id_index += 1
        self.__id = Node.__id_index
        self.__connections = []
        self.color = NodeColors.GRAY

    def get_connections(self):
        return self.__connections

    def add_connection(self, connection):
        if connection not in self.__connections:
            self.__connections.append(connection)

    def remove_connection(self, connection):
        self.__connections.remove(connection)

    def get_id(self):
        return self.__id

class ArtistNode(Node):
    def __init__(self, name="", genres=[]):
        super().__init__()
        self.__name = name
        self.__genres = genres
        self.color = NodeColors.BLUE

    def __str__(self):
        return f"{self.__name}"

    def get_name(self):
        return self.__name

    def get_genres(self):
        return self.__genres

    def add_genres(self, genres):
        return self.__genres.extend(genres)

class GenreNode(Node):
    def __init__(self, name=""):
        super().__init__()
        self.__name = name
        self.color = NodeColors.YELLOW

    def __str__(self):
        return f"{self.__name}"

    def get_name(self):
        return self.__name

class TrackNode(Node):
    def __init__(self, title="", artists=[]):
        super().__init__()
        self.__title = title
        self.__artists = artists
        self.color = NodeColors.INDIGO

    def __str__(self):
        return f"{self.__title} | {', '.join(f'{x.get_name()}' for x in self.__artists)}"
