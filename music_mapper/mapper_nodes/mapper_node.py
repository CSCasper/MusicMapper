import json
from enum import Enum

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

    def __init__(self, id="", tag="", data=None):
        self._connected_nodes = []
        self.tag = tag
        self._id = id
        self._data = data
        self.color = NodeColors.GRAY
        
    def get_id(self):
        return self._id

    def get_connections(self):
        """Returns a copy of the list of nodes which have a connection to this node

        Returns:
            List: connections to other nodes
        """
        return self._connected_nodes.copy()

    def is_connected(self, node):
        """Returns whether or not node is the connected node list

        Args:
            node (Node): Node to check for connection

        Returns:
            bool: True - Connected | False - Not connected
            
        Raises:
            TypeError: invalid type
        """
        return node in self._connected_nodes

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
            self._connected_nodes.append(node)
        if not node.is_connected(self):
            node.add_connection(self)

    def remove_connection(self, node):
        """Removes a connection from a node if it exists

        Args:
            node (Node): Node to remove
        """
        if not isinstance(node, Node):
            raise TypeError
        if node in self._connected_nodes:
            self._connected_nodes.remove(node)
    
    def to_dict(self):
        """Returns a dictionary representation of the node

        Returns:
            dict: dictionary representation of the node
        """
        return {
            "Connections": self.get_connection_ids(),
            "Data": self._data
        }
        
    def to_json(self):
        """Returns a JSON representation of the node

        Returns:
            str: JSON representation of the node
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def get_connection_ids(self):
        """Returns a list of connection ids

        Returns:
            List: list of connection ids
        """
        return [f"{node.tag}_{node.get_id()}" for node in self._connected_nodes]

class TrackNode(Node):
    """Creates a MusicMap Track node
    
    Args:
        Node (Node): Inherited Node class
    """
    def __init__(self, title="", artists=None, id="", data=None):
        super().__init__(id, "Track", data)
        self._title = title
        self._artists = artists if artists else []
        self.color = NodeColors.INDIGO

    def __str__(self):
        return f"{self._title} | {', '.join(f'{x.get_name()}' for x in self._artists)}"

    def get_artists(self):
        """Returns a list of artists on the track

        Returns:
            List: list of artist nodes 
        """
        return self._artists.copy()

    def add_artists(self, *artists):
        """Adds valid artist nodes to the track

        Returns:
            List: genre nodes that were successfully added
        """
        added_artists = [artist for artist in artists if isinstance(artist, ArtistNode)]
        for artist in added_artists:
            self.add_connection(artist)
        self._artists.extend(added_artists)
        return added_artists.copy()
    
    def has_artist(self, artist_id):
        """Returns whether or not the artist is on the track

        Args:
            artist_id (str): artist id

        Returns:
            bool: True - Artist is on track | False - Artist is not on track
        """
        return artist_id in [artist.id for artist in self._artists]

    def get_title(self):
        """Get the title of the track

        Returns:
            str: track title
        """
        return self._title

    def set_title(self, title):
        """Set the title of the track

        Args:
            title (str): title to set

        Raises:
            TypeError: invalid type
        """
        if not isinstance(title, str):
            raise TypeError
        self._title = title

class ArtistNode(Node):
    """Creates an MusicMap Artist node

    Args:
        Node (Node): Inherited Node class
    """
    def __init__(self, name="", genres=None, id="", data=None):
        super().__init__(id, "Artist", data)
        self._name = name
        self._genres = genres if genres else []
        self.color = NodeColors.BLUE

    def __str__(self):
        """Returns a string representation of the MapperNode object.

        Returns:
            str: The name of the MapperNode.
        """
        return f"{self._name}"

    def get_name(self):
        """Return the name of the artist

        Returns:
            string: artist name
        """
        return self._name
  
    def set_name(self, name):
        """Sets the name of the artist

        Args:
            name (str): name of the artist to be set

        Raises:
            TypeError: invalid type
        """
        if not isinstance(name, str):
            raise TypeError
        self._name = name

    def get_genres(self):
        """Return a list of genres that belong to the artist

        Returns:
            List: list of genre nodes
        """
        return self._genres.copy()

    def add_genres(self, *genres):
        """Adds valid genres to the artist

        Returns:
            List: genre nodes that were successfully added
        """
        added_genres = [genre for genre in genres if isinstance(genre, GenreNode)]
        for genre in added_genres:
            self.add_connection(genre)
        self._genres.extend(added_genres)
        return added_genres.copy()

class GenreNode(Node):
    """Creates a MusicMap Genre node

    Args:
        Node (Node): Inherited Node class
    """
    def __init__(self, name="", id=""):
        super().__init__(id, "Genre", None)
        self._name = name
        self.color = NodeColors.YELLOW

    def __str__(self):
        return f"{self._name}"

    def get_name(self):
        """Get the name of the genre

        Returns:
            str: genre name
        """
        return self._name
    
    def set_name(self, name):
        """Set the name of the genre

        Args:
            name (str): name to set
            
        Raises:
            TypeError: invalid type
        """
        if not isinstance(name, str):
            raise TypeError
        self._name = name