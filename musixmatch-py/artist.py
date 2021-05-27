import requests
from endpoints import Endpoints


class Artist:
    """
    Gives information about artist and there albums, tracks etc
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def artist_id(self, id):
        """
        Gives information about the artist from there musixmatch artist id

        :param id:  The artist musixmatch id
        :type id: int

        :return:    The artist data
        """
        if not isinstance(id, int):
            return "the id should be an integer"
        x = requests.get(
            f"{Endpoints.base_url}artist.get?apikey={self.api_key}&artist_id={id}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        return x.json()

    def artist_search(self, name, page=1, page_size=10):
        """
        Search and gives details of an artist by there name

        :param name:        The artist name
        :type name:         str
        :param page:        Define the page number for paginated results, defaults to 1
        :type page:         int, Optional
        :param page_size:   Define the page size for paginated results. Range is 1 to 100. defaults to 10
        :type page_size:    int, Optional

        :return:            The artist detail
        """
        x = requests.get(
            f"{Endpoints.base_url}artist.search?apikey={self.api_key}&q_artist={name}&page={page}&page_size={page_size}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        return x.json()

    def artist_album(
        self, artist_id, group_album_name=1, release="desc", page=1, page_size=10
    ):
        """
        Get the album discography of an artist

        :param artist_id:           The artist musixmatch id
        :type artist_id:            int
        :param group_album_name:    Group by Album Name(0 or 1), defaults to 1
        :type group_album_name:     int, Optional
        :param release:             Sort by release date (asc|desc)
        :type release:              str, Optional
        :param page:                Define the page number for paginated results, defaults to 1
        :type page:                 int, Optional
        :param page_size:           Define the page size for paginated results. Range is 1 to 100. defaults to 10
        :type page_size:            int, Optional

        :return:                    Get the album of artist
        """
        if not isinstance(artist_id, int):
            return "the id should be an integer"
        x = requests.get(
            f"{Endpoints.base_url}artist.albums.get?apikey={self.api_key}&artist_id={artist_id}&s_release_date={release}&g_album_name={group_album_name}&page={page}&page_size={page_size}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        return x.json()

    def artist_related(self, artist_id, page=1, page_size=10):
        """
        Get a list of artists somehow related to a given one.

        :param artist_id:           The artist musixmatch id
        :type artist_id:            int
        :param page:                Define the page number for paginated results, defaults to 1
        :type page:                 int, Optional
        :param page_size:           Define the page size for paginated results. Range is 1 to 100. defaults to 10
        :type page_size:            int, Optional

        :return:                    The artist details
        """
        if not isinstance(artist_id, int):
            return "the id should be an integer"
        x = requests.get(
            f"{Endpoints.base_url}artist.related.get?apikey={self.api_key}&artist_id={artist_id}&page={page}&page_size={page_size}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        return x.json()
