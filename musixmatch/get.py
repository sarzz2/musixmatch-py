import requests
from endpoints import Endpoints

API = "0c453b2cff6e1ee5fb0a6650681f9375"


class Get:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_top_artist(self, country, page=1, pagesize=10, format="json"):
        """
        Get the list of top artist for a given country
        :param country: A valid country code (default US)
        :param page:    Define the page number for paginated results (default 1)
        :param pagesize:    Define the page size for paginated results. Range is 1 to 100. (default 10)
        :param format:  Decide the output type (json or xml) (default json)

        :return:
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
        x = requests.get(
            f"{Endpoints.base_url}chart.tracks.get?apikey={self.api_key}&page={page}&page_size={pagesize}&country={country}&chart_name={chart_name}&f_has_lyrics={f_has_lyrics}"
        )
        return x.json()
