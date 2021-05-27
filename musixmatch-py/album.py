import requests
from endpoints import Endpoints


class Album:
    """
    Get this list of albums and tracks from their musixmatch album id
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def album(self, album_id):
        """
        Lists the information about an album from the musixmatch album id

        :param album_id:    The musixmatch album id
        :type album_id:     int

        :return: The album details
        """
        if not isinstance(album_id, int):
            return "the id should be an integer"
        x = requests.get(
            f"{Endpoints.base_url}album.get?apikey={self.api_key}&album_id={album_id}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        if x.json()["message"]["header"]["status_code"] == 404:
            return f"No album with given ID:{album_id} found"
        return x.json()

    def album_track(self, album_id, f_has_lyrics=1, page=1, page_size=10):
        """
        Lists the tracks of an album

        :param album_id:        The musixmatch album id
        :type album_id:         int
        :param f_has_lyrics:    Filters the tracks with lyrics only (0 or 1), defaults to 1
        :type f_has_lyrics:     int, Optional
        :param page:            Define the page number for paginated results, defaults to 1
        :type page:             int, Optional
        :param page_size:       Define the page size for paginated results. Range is 1 to 100, defaults to 10
        :type page_size:        int, Optional

        :return:                List of tracks in album
        """
        if not isinstance(album_id, int):
            return "the id should be an integer"
        x = requests.get(
            f"{Endpoints.base_url}album.tracks.get?apikey={self.api_key}&album_id={album_id}&f_has_lyrics={f_has_lyrics}&page={page}&page_size={page_size}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        if x.json()["message"]["header"]["status_code"] == 404:
            return f"No album with given ID:{album_id} found"
        return x.json()
