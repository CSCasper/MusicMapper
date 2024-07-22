from typing import List, Dict, Any


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


class ExternalURL:
    def __init__(self, spotify: str):
        self.spotify = spotify

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            spotify=data["spotify"]
        )


class Artist:
    def __init__(self, external_urls: ExternalURL, href: str, id: str, name: str, type: str, uri: str):
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.name = name
        self.type = type
        self.uri = uri

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            external_urls=ExternalURL.from_dict(data["external_urls"]),
            href=data["href"],
            id=data["id"],
            name=data["name"],
            type=data["type"],
            uri=data["uri"]
        )


class Album:
    def __init__(self, album_type: str, total_tracks: int, external_urls: ExternalURL, href: str, id: str, images: List[Image], name: str, release_date: str, release_date_precision: str, restrictions: Dict[str, Any], type: str, uri: str, artists: List[Artist]):
        self.album_type = album_type
        self.total_tracks = total_tracks
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.restrictions = restrictions
        self.type = type
        self.uri = uri
        self.artists = artists

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            album_type=data["album_type"],
            total_tracks=data["total_tracks"],
            # makes the JSON file annoying, can re-add if needed. Update constructor as well.
            # available_markets=data["available_markets"],
            external_urls=ExternalURL.from_dict(data["external_urls"]),
            href=data["href"],
            id=data["id"],
            images=[Image.from_dict(image) for image in data["images"]],
            name=data["name"],
            release_date=data["release_date"],
            release_date_precision=data["release_date_precision"],
            restrictions=data.get("restrictions", {}),
            type=data["type"],
            uri=data["uri"],
            artists=[Artist.from_dict(artist) for artist in data["artists"]]
        )


class Track:
    def __init__(self, album: Album, artists: List[Artist], disc_number: int, duration_ms: int, explicit: bool, external_ids: Dict[str, str], external_urls: ExternalURL, href: str, id: str, linked_from: Dict[str, Any], restrictions: Dict[str, Any], name: str, popularity: int, preview_url: str, track_number: int, type: str, uri: str, is_local: bool):
        self.album = album
        self.artists = artists
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.linked_from = linked_from
        self.restrictions = restrictions
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri
        self.is_local = is_local

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            album=Album.from_dict(data["album"]),
            artists=[Artist.from_dict(artist) for artist in data["artists"]],
            # makes the JSON file annoying, can re-add if needed. Update constructor as well.
            # available_markets=data["available_markets"],
            disc_number=data["disc_number"],
            duration_ms=data["duration_ms"],
            explicit=data["explicit"],
            external_ids=data["external_ids"],
            external_urls=ExternalURL.from_dict(data["external_urls"]),
            href=data["href"],
            id=data["id"],
            linked_from=data.get("linked_from", {}),
            restrictions=data.get("restrictions", {}),
            name=data["name"],
            popularity=data["popularity"],
            preview_url=data["preview_url"],
            track_number=data["track_number"],
            type=data["type"],
            uri=data["uri"],
            is_local=data["is_local"]
        )