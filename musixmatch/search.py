import requests
from endpoints import Endpoints


API = "0c453b2cff6e1ee5fb0a6650681f9375"


class Search:
    def __init__(self, api):
        self.api = api

    def search_track(
        self,
        q_track,
        q_artist="",
        q_lyrics="",
        f_artist_id="",
        f_music_genre_id="",
        f_lyrics_language="",
        f_has_lyrics="",
        f_track_release_group_first_release_date_min="",
        f_track_release_group_first_release_date_max="",
        s_artist_rating="",
        s_track_rating="",
        page=1,
        page_size=5,
    ):
        """
        :param api:     Your musixmatch API key
        :param q_track: The song title
        :param q_artist:    The song artist
        :param q_lyrics:    The song lyric
        :param f_artist_id: When set, filter by this artist id
        :param f_music_genre_id:    When set, filter by this music category id
        :param f_lyrics_language:   Filter by the lyrics language (en,it,..)
        :param f_has_lyrics:    When set, filter only contents with lyrics
        :param f_track_release_group_first_release_date_min:    When set, filter the tracks with release date newer than value, format is YYYYMMDD
        :param f_track_release_group_first_release_date_max:    When set, filter the tracks with release date older than value, format is YYYYMMDD
        :param s_artist_rating: Sort by our popularity index for artists (asc|desc)
        :param s_track_rating:  Sort by our popularity index for tracks (asc|desc)
        :param page:    Define the page number for paginated results
        :param page_size:   Define the page size for paginated results. Range is 1 to 100.
        :return:
        """
        x = requests.get(
            f"{Endpoints.base_url}track.search?apikey={self.api}&q_track={q_track}&q_artist={q_artist}&q_lyrics={q_lyrics}&page_size={page_size}&page={page}&f_artist_id={f_artist_id}&f_music_genre_id={f_music_genre_id}&f_lyrics_language={f_lyrics_language}&f_has_lyrics={f_has_lyrics}&f_track_release_group_first_release_date_min={f_track_release_group_first_release_date_min}&f_track_release_group_first_release_date_max={f_track_release_group_first_release_date_max}&s_artist_rating={s_artist_rating}&s_track_rating{s_track_rating}"
        )
        return x.json()


# Search(API).search_track("just")
