import requests
from endpoints import Endpoints


class Track:
    """
    Get the tracks based on various attributes
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def search_track(
        self,
        q_track,
        q_artist="",
        q_lyrics="",
        f_artist_id="",
        f_music_genre_id="",
        f_lyrics_language="",
        f_has_lyrics=1,
        f_track_release_group_first_release_date_min="",
        f_track_release_group_first_release_date_max="",
        s_artist_rating="",
        s_track_rating="",
        page=1,
        page_size=5,
    ):
        """
        Search for track in musixmatch database.

        :param q_track:                                         The song title
        :type q_track:                                          str
        :param q_artist:                                        The song artist
        :type q_artist:                                         str, Optional
        :param q_lyrics:                                        The song lyric
        :type q_lyrics:                                         str, Optional
        :param f_artist_id:                                     When set, filter by this artist id
        :type f_artist_id:                                      int, Optional
        :param f_music_genre_id:                                When set, filter by this music category id
        :type f_music_genre_id:                                 int, Optional
        :param f_lyrics_language:                               Filter by the lyrics language (en,it,..)
        :type f_lyrics_language:                                str, Optional
        :param f_has_lyrics:                                    When set, filter only contents with lyrics
        :type f_has_lyrics:                                     int, Optional
        :param f_track_release_group_first_release_date_min:    When set, filter the tracks with release date newer than value, format is YYYYMMDD
        :type f_track_release_group_first_release_date_min:     int, Optional
        :param f_track_release_group_first_release_date_max:    When set, filter the tracks with release date older than value, format is YYYYMMDD
        :type f_track_release_group_first_release_date_max:     int, Optional
        :param s_artist_rating:                                 Sort by our popularity index for artists (asc|desc)
        :type s_artist_rating:                                  int, Optional
        :param s_track_rating:                                  Sort by our popularity index for tracks (asc|desc)
        :type s_track_rating:                                   int, Optional
        :param page:                                            Define the page number for paginated results, defaults to 1
        :type page:                                             int, Optional
        :param page_size:                                       Define the page size for paginated results. Range is 1 to 100. defaults to 10
        :type page_size:                                        int, Optional

        :return:                                                    The track details
        """
        x = requests.get(
            f"{Endpoints.base_url}track.search?apikey={self.api_key}&q_track={q_track}&q_artist={q_artist}&q_lyrics={q_lyrics}&page_size={page_size}&page={page}&f_artist_id={f_artist_id}&f_music_genre_id={f_music_genre_id}&f_lyrics_language={f_lyrics_language}&f_has_lyrics={f_has_lyrics}&f_track_release_group_first_release_date_min={f_track_release_group_first_release_date_min}&f_track_release_group_first_release_date_max={f_track_release_group_first_release_date_max}&s_artist_rating={s_artist_rating}&s_track_rating{s_track_rating}"
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

    def track_by_id(self, id):
        """
        Get a track info

        :param id:  The Musixmatch commontrack id
        :type id:   int

        :return:    the track details
        """
        x = requests.get(
            f"{Endpoints.base_url}track.get?apikey={self.api_key}&commontrack_id={id}"
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

    def lyrics_by_id(self, id):
        """
        Get lyrics info by musixmatch track id

        :param id:  The Musixmatch track id
        :type id:   int

        :return:    the lyric details
        """
        x = requests.get(
            f"{Endpoints.base_url}track.lyrics.get?apikey={self.api_key}&track_id={id}"
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

    def lyrics_mood_by_id(self, id):
        """
        Get mood info of a track by it's musixmatch commontrack id

        :param id:  The Musixmatch commontrack id
        :type id:   int

        :return:    the lyric details
        """
        x = requests.get(
            f"{Endpoints.base_url}track.lyrics.mood.get?apikey={self.api_key}&commontrack_id={id}"
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

    # def track_snippet_by_id(self, id):
    #     x = requests.get(
    #         f"{Endpoints.base_url}track.snippet.get?apikey={self.api_key}&track_id={id}"
    #     )
    #     return x.json()

    def subtitle_track_by_id(
        self,
        id,
        subtitle_format="lrc",
        f_subtitle_length=20,
        f_subtitle_length_max_deviation=20,
    ):
        """
        Get the subtitles of track by their common track ID. Requires a commercial plan.
        You need a commercial plan to make this request

        :param id:                                  The Musixmatch commontrack id
        :type id:                                   int
        :param subtitle_format:                     The format of the subtitle (lrc,dfxp,stledu). Default to lrc
        :type subtitle_format:                      str, Optional
        :param f_subtitle_length:                   The desired length of the subtitle (seconds), defaults to 20
        :type f_subtitle_length:                    int, Optional
        :param f_subtitle_length_max_deviation:     The maximum deviation allowed from the f_subtitle_length (seconds), defaults to 20
        :type f_subtitle_length_max_deviation:      int, Optional

        :return:    the subitle details
        """
        x = requests.get(
            f"{Endpoints.base_url}track.subtitle.get?apikey={self.api_key}&commontrack_id={id}&subtitle_format={subtitle_format}&f_subtitle_length={f_subtitle_length}&f_subtitle_length_max_deviation{f_subtitle_length_max_deviation}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        if x.json()["message"]["header"]["status_code"] == 402:
            return (
                "The usage limit has been reached, either you exceeded per day requests limits or your balance is "
                "insufficient. "
            )
        if x.json()["message"]["header"]["status_code"] == 403:
            return "You are not authorized to perform this operation.You need a commercial plan for this request"
        return x.json()

    def rich_sync_by_id(
        self, id, f_richsync_length=20, f_richsync_length_max_deviation=20
    ):
        """
        Get the Rich sync for a track
        A rich sync is an enhanced version of the standard sync which allows:
        position offset by single characther
        endless formatting options at single char level
        multiple concurrent voices
        multiple scrolling direction
        You need a commercial plan to make this request

        :param id:                                  The Musixmatch ntrack id
        :type id:                                   int
        :param f_richsync_length:                   The desired length of the sync (seconds), defaults to 20
        :type f_richsync_length:                    int, Optional
        :param f_richsync_length_max_deviation:     The maximum deviation allowed from the f_sync_length (seconds), default to 20
        :type f_richsync_length_max_deviation:      int, Optional

        """
        x = requests.get(
            f"{Endpoints.base_url}track.richsync.get?apikey={self.api_key}&track_id={id}&f_richsync_length={f_richsync_length}&f_richsync_length_max_deviation={f_richsync_length_max_deviation}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        if x.json()["message"]["header"]["status_code"] == 402:
            return (
                "The usage limit has been reached, either you exceeded per day requests limits or your balance is "
                "insufficient. "
            )
        if x.json()["message"]["header"]["status_code"] == 403:
            return "You are not authorized to perform this operation. You need a commercial plan for this request."
        return x.json()

    def translate_lyrics(self, id, language, min_completed=1):
        """
        Get a translated lyrics for a given language.
        You need a commercial plan to make this request.

        :param id:                                  The Musixmatch ntrack id
        :type id:                                   int
        :param language:                            The language of the translated lyrics
        :type language:                             str
        :param min_completed:                       Teal from 0 to 1. If present, only the tracks with a translation ratio over this specific value, for a given language, are returned Set it to 1 for completed translation only, to 0.7 for a mimimum of 70% complete translation, defaults to 1
        :type min_completed:                        int, Optional
        """
        x = requests.get(
            f"{Endpoints.base_url}track.lyrics.translation.get?apikey={self.api_key}&commontrack_id={id}&selected_language={language}&min_completed={min_completed}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        if x.json()["message"]["header"]["status_code"] == 402:
            return (
                "The usage limit has been reached, either you exceeded per day requests limits or your balance is "
                "insufficient. "
            )
        if x.json()["message"]["header"]["status_code"] == 403:
            return "You are not authorized to perform this operation. You need a commercial plan for this request."
        return x.json()
