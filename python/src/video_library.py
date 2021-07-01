"""A video library class."""

from .video import Video
from pathlib import Path
import csv


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.
def _csv_reader_with_strip(reader):
    yield from ((item.strip() for item in line) for line in reader)


class VideoLibrary:
    """A class used to represent a Video Library."""

    def __init__(self):
        """The VideoLibrary class is initialized."""
        self._videos = {}
        self._playing_video = ""
        self._video_paused = False
        self._playlists = {}
        with open(Path(__file__).parent / "videos.txt") as video_file:
            reader = _csv_reader_with_strip(
                csv.reader(video_file, delimiter="|"))
            for video_info in reader:
                title, url, tags = video_info
                self._videos[url] = Video(
                    title,
                    url,
                    [tag.strip() for tag in tags.split(",")] if tags else [],
                )

    @property
    def playing(self) -> str:
        """Returns the id of the playing video."""
        return self._playing_video

    @property
    def is_paused(self) -> bool:
        """Returns boolean of if the video is paused."""
        return self._video_paused

    @property
    def playlists(self) -> dict:
        """Returns dictionary of playlists."""
        return self._playlists

    def create_playlist(self, playlist_name):
        """Creates a new playlist."""
        self._playlists[playlist_name.lower()] = {"name": playlist_name, "videos": set()}

    def add_to_playlist(self, playlist_name, video_id):
        """Add video id to an existing playlist."""
        self._playlists[playlist_name.lower()]['videos'].add(video_id)

    def remove_from_playlist(self, playlist_name, video_id):
        """Remove video id to an existing playlist."""
        self._playlists[playlist_name.lower()]['videos'].remove(video_id)

    def pause_video(self):
        """Pauses the current playing video."""
        self._video_paused = True

    def now_playing(self, video_id):
        """Modifies the id of the playing video."""
        self._playing_video = video_id
        self._video_paused = False
    
    def stopping_video(self):
        """Stops the current video"""
        self._playing_video = ""
        self._video_paused = False

    def get_all_videos(self):
        """Returns all available video information from the video library."""
        return list(self._videos.values())

    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the video library.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)
