import requests
from endpoints import Endpoints


class Charts:
    """
    Get the list of top Charts
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def get_top_artist(self, country, page=1, pagesize=10, format="json"):
        """
        Get the list of top artist for a given country

        :param country:     A valid country code (default US)
        :type country:      str
        :param page:        Define the page number for paginated results (default 1)
        :type page:         int, Optional
        :param pagesize:    Define the page size for paginated results. Range is 1 to 100. (default 10)
        :type pagesize:     int, Optional
        :param format:      Decide the output type (json or xml) (default json)
        :type format:       str, Optional

        :return:    The request response
        """
        x = requests.get(
            f"{Endpoints.base_url}chart.artists.get?apikey={self.api_key}&page={page}&page_size={pagesize}&country={country}&format={format}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        return x.json()

    def get_top_song(
        self, country, page=1, pagesize=10, chart_name="top", f_has_lyrics=1
    ):
        """
        Get the top song of a country

        :param country:     Country name
        :type country:      str
        :param page:        Define the page number for paginated results (default 1)
        :type page:         int, Optional
        :param pagesize:    Define the page size for paginated results. Range is 1 to 100. (default 10)
        :type pagesize:     int, Optional
        :param chart_name:  Select among available charts:
                            top : editorial chart
                            hot : Most viewed lyrics in the last 2 hours
                            defaults to top
        :type chart_name:   str, Optional
        :param f_has_lyrics: When set, filter only contents with lyrics (0|1), defaults to 1
        :type f_has_lyrics: int, Optional

        :return:            The top song of a particular country
        """
        x = requests.get(
            f"{Endpoints.base_url}chart.tracks.get?apikey={self.api_key}&page={page}&page_size={pagesize}&country={country}&chart_name={chart_name}&f_has_lyrics={f_has_lyrics}"
        )
        if x.json()["message"]["header"]["status_code"] == 401:
            return "Invalid API key"
        return x.json()
