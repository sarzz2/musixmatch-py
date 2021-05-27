from .main import Musixmatch
from charts import Charts
from tracks import Track
from matcher import Matcher
from artist import Artist
from album import Album

"""
musixmatch API Wrapper
~~~~~~~~~~~~~~~~~~~~~
Basic wrapper for the undocumented musixmatch API.
"""

from typing import NamedTuple

VersionInfo = NamedTuple(
    "VersionInfo", major=int, minor=int, micro=int, releaselevel=str, serial=int
)

version_info = VersionInfo(major=0, minor=3, micro=5, releaselevel="", serial=0)

__all__ = [
    "Musixmatch",
    "Charts",
    "Track",
    "Matcher",
    "Artist",
    "Album"
]

