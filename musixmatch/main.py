from charts import Charts
from tracks import Track
from matcher import Matcher
from artist import Artist
from album import Album


class Musixmatch(Charts, Track, Matcher, Artist, Album):
    def __init__(self, api_key):
        Charts.__init__(self, api_key)
        Track.__init__(self, api_key)
        Matcher.__init__(self, api_key)
        Artist.__init__(self, api_key)
        Album.__init__(self, api_key)
