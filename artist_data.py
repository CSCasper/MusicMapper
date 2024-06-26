class Artist:
    def __init__(self, external_urls, followers, genres, href, id, images, name, popularity, type, uri):
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

    def __repr__(self):
        return (f"Artist(external_urls={self.external_urls}, followers={self.followers}, genres={self.genres}, "
                f"href={self.href}, id={self.id}, images={self.images}, name={self.name}, popularity={self.popularity}, "
                f"type={self.type}, uri={self.uri})")
