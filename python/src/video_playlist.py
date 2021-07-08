"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        """The Playlist class is initialized."""
        self._playlists = {}

    @property
    def playlists(self) -> dict:
        """Returns dictionary of playlists."""
        return self._playlists

    def create_playlist(self, playlist_name):
        """Creates a new playlist."""
        self._playlists[playlist_name.lower()] = {"name": playlist_name, "videos": []}

    def add_to_playlist(self, playlist_name, video_id):
        """Add video id to an existing playlist."""
        self._playlists[playlist_name.lower()]['videos'].append(video_id)

    def remove_from_playlist(self, playlist_name, video_id):
        """Remove video id to an existing playlist."""
        self._playlists[playlist_name.lower()]['videos'].remove(video_id)

    def clear_playlist(self, playlist_name):
        """Clear list of video ids to an existing playlist."""
        self._playlists[playlist_name.lower()]['videos'].clear()

    def delete_playlist(self, playlist_name):
        """Delete an existing playlist."""
        self._playlists.pop(playlist_name, None)
