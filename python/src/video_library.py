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
        self._flagged = {}
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
    def flagged(self) -> dict:
        """Returns dictionary of flagged video_ids."""
        return self._flagged

    def flag_video(self, video_id, reason=""):
        """Add flagged status to video id with optional reason"""
        self._flagged[video_id] = reason

    def unflag_video(self, video_id):
        """Remove flagged status to video id"""
        self._flagged.pop(video_id)

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
