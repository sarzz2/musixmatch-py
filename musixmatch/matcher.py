import requests
from endpoints import Endpoints


class Matcher:
    """
    Matches the lyrics and returns the information
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def match_lyrics(self, lyrics, artist):
        """
        Get the lyrics for track based on title and artist

        :param lyrics:      The song title
        :type lyrics:       str
        :param artist:      The song artist
        :type artist:       str

        :return:            The lyrics based on title and artist
        """
        x = requests.get(
            f"{Endpoints.base_url}matcher.lyrics.get?apikey={self.api_key}&q_track={lyrics}&q_artist={artist}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        if x.json()["message"]["header"]["status_code"] == 402:
            return (
                "The usage limit has been reached, either you exceeded per day requests limits or your balance is "
                "insufficient. "
            )
        if x.json()["message"]["header"]["status_code"] == 403:
            return "You are not authorized to perform this operation."
        # print(x.json()["message"]["body"]["lyrics"]["lyrics_body"])
        return x.json()

    def match_song(self, track, artist, album=""):
        """
        Match your song against musixmatch database.

        :param track:       The song title
        :type track:        str
        :param artist:      The song artist
        :type artist:       str
        :param album:       The song album
        :type album:        str, Optional

        :return:            the details of the song
        """
        x = requests.get(
            f"{Endpoints.base_url}matcher.track.get?apikey={self.api_key}&q_track={track}&q_artist={artist}&q_album={album}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        if x.json()["message"]["header"]["status_code"] == 402:
            return (
                "The usage limit has been reached, either you exceeded per day requests limits or your balance is "
                "insufficient. "
            )
        if x.json()["message"]["header"]["status_code"] == 403:
            return "You are not authorized to perform this operation."
        return x.json()
