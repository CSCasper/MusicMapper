from enum import Enum

SIMPLE_GENRES = ["rock", "rap", "trap", "step", "ambient",
                 "soul", "pop", "house", "dnb"]


class NodeColors(Enum):
    """Color options for a Node

    Available colors: GRAY, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, PURPLE
    
    Args:
        Enum (int): Color
    """
    GRAY = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5
    INDIGO = 6
    PURPLE = 7

class Node():
    """Creates a basic MusicMap node

    Returns:
        Node: basic MusicMap node
    """
    __id_index = 0

    def __init__(self):
        Node.__id_index += 1
        self.__id = Node.__id_index
        self.__connected_nodes = []
        self.color = NodeColors.GRAY

    def get_id(self):
        """Returns Node id

        Returns:
            int: id
        """
        return self.__id

    def get_connections(self):
        """Returns a copy of the list of nodes which have a connection to this node

        Returns:
            List: connections to other nodes
        """
        return self.__connected_nodes.copy()

    def is_connected(self, node):
        """Returns whether or not node is the connected node list

        Args:
            node (Node): Node to check for connection

        Returns:
            bool: True - Connected | False - Not connected
            
        Raises:
            TypeError: invalid type
        """
        return node in self.__connected_nodes

    def add_connection(self, node):
        """Adds a node to the connection list if it doesn't already exist in the collection

        Args:
            node (Node): Node to add
        
        Raises:
            TypeError: invalid type
            
        """
        if not isinstance(node, Node):
            raise TypeError

        if not self.is_connected(node):
            self.__connected_nodes.append(node)
        if not node.is_connected(self):
            node.add_connection(self)
        print(f"Node ({type(self).__name__}) {self.get_id()} -> \
            Node ({str(type(node).__name__)}) {node.get_id()}")

    def remove_connection(self, node):
        """Removes a connection from a node if it exists

        Args:
            node (Node): Node to remove
        """
        if not isinstance(node, Node):
            raise TypeError
        if node in self.__connected_nodes:
            self.__connected_nodes.remove(node)

    def get_id(self):
        """Return the Node id

        Returns:
            int: Unique ID for the node
        """
        return self.__id

class ArtistNode(Node):
    """Creates an MusicMap Artist node

    Args:
        Node (Node): Inherited Node class
    """
    def __init__(self, name="", genres=None):
        super().__init__()
        self.__name = name
        self.__genres = genres if genres else []
        self.color = NodeColors.BLUE

    def __str__(self):
        return f"{self.__name}"

    def get_name(self):
        """Return the name of the artist

        Returns:
            string: artist name
        """
        return self.__name
  
    def set_name(self, name):
        """Sets the name of the artist

        Args:
            name (str): name of the artist to be set

        Raises:
            TypeError: invalid type
        """
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    def get_genres(self):
        """Return a list of genres that belong to the artist

        Returns:
            List: list of genre nodes
        """
        return self.__genres.copy()

    def add_genres(self, *genres):
        """Adds valid genres to the artist

        Returns:
            List: genre nodes that were successfully added
        """
        added_genres = [genre for genre in genres if isinstance(genre, GenreNode)]
        for genre in added_genres:
            self.add_connection(genre)
        self.__genres.extend(added_genres)
        return added_genres.copy()

class GenreNode(Node):
    """Creates a MusicMap Genre node

    Args:
        Node (Node): Inherited Node class
    """
    def __init__(self, name=""):
        super().__init__()
        self.__name = name
        self.color = NodeColors.YELLOW

    def __str__(self):
        return f"{self.__name}"

    def get_name(self):
        """Get the name of the genre

        Returns:
            str: genre name
        """
        return self.__name
    
    def set_name(self, name):
        """Set the name of the genre

        Args:
            name (str): name to set
            
        Raises:
            TypeError: invalid type
        """
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

class TrackNode(Node):
    """Creates a MusicMap Track node
    
    Args:
        Node (Node): Inherited Node class
    """
    def __init__(self, title="", artists=None):
        super().__init__()
        self.__title = title
        self.__artists = artists if artists else []
        self.color = NodeColors.INDIGO

    def __str__(self):
        return f"{self.__title} | {', '.join(f'{x.get_name()}' for x in self.__artists)}"

    def get_artists(self):
        """Returns a list of artists on the track

        Returns:
            List: list of artist nodes 
        """
        return self.__artists.copy()

    def add_artists(self, *artists):
        """Adds valid artist nodes to the track

        Returns:
            List: genre nodes that were successfully added
        """
        added_artists = [artist for artist in artists if isinstance(artist, ArtistNode)]
        for artist in added_artists:
            self.add_connection(artist)
        self.__artists.extend(added_artists)
        return added_artists.copy()

    def get_title(self):
        """Get the title of the track

        Returns:
            str: track title
        """
        return self.__title

    def set_title(self, title):
        """Set the title of the track

        Args:
            title (str): title to set

        Raises:
            TypeError: invalid type
        """
        if not isinstance(title, str):
            raise TypeError
        self.__title = title
