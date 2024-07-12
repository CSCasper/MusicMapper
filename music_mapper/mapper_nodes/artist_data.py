from typing import List, Dict, Any


class ExternalURL:
    def __init__(self, spotify: str):
        self.spotify = spotify

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            spotify=data["spotify"]
        )


class Followers:
    def __init__(self, href: str, total: int):
        self.href = href
        self.total = total

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            href=data["href"],
            total=data["total"]
        )


class Image:
    def __init__(self, url: str, height: int, width: int):
        self.url = url
        self.height = height
        self.width = width

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            url=data["url"],
            height=data["height"],
            width=data["width"]
        )


class Artist:
    def __init__(self, external_urls: ExternalURL, followers: Followers, genres: List[str], href: str, id: str, images: List[Image], name: str, popularity: int, type: str, uri: str):
        self.external_urls = external_urls
        self.followers = followers
        self.genres = genres
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.popularity = popularity
        self.type = type
        self.uri = uri

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            external_urls=ExternalURL.from_dict(data["external_urls"]),
            followers=Followers.from_dict(data["followers"]),
            genres=data["genres"],
            href=data["href"],
            id=data["id"],
            images=[Image.from_dict(image) for image in data["images"]],
            name=data["name"],
            popularity=data["popularity"],
            type=data["type"],
            uri=data["uri"]
        )
