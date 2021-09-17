class Media:
    def __init__(self, media_id, name, url):
        self.media_id = media_id
        self.name = name
        self.url = url

class Room:
    def __init__(self, title, creator, url, **kwargs):
        self.title = title
        self.creator = creator
        self.url = url

