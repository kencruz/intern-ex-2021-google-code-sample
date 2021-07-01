"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
        print("Here's a list of all available videos:" )
        videos = self._video_library.get_all_videos()
        # Sort by lexicographical order by title
        videos.sort(key=lambda x: x.title)
        for video in videos:
            print('{title} ({id}) [{tags}]'.format(title=video.title, id=video.video_id, tags=' '.join(video.tags)))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist" )
        else:
            if len(self._video_library.playing) > 0:
                prev_video_id = self._video_library.playing;
                prev_video = self._video_library.get_video(prev_video_id);
                print("Stopping video: " + prev_video.title)

            print('Playing video: {}'.format(video.title))
            self._video_library.now_playing(video.video_id)

    def stop_video(self):
        """Stops the current video."""
        prev_video_id = self._video_library.playing;
        prev_video = self._video_library.get_video(prev_video_id);

        if len(self._video_library.playing) == 0:
            print("Cannot stop video: No video is currently playing" )
        else:
            print("Stopping video: " + prev_video.title)
            self._video_library.stopping_video()

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = self._video_library.get_all_videos()
        num_videos = len(videos)
        random_video = videos[random.randint(0, num_videos - 1)]
        self.play_video(random_video.video_id)

    def pause_video(self):
        """Pauses the current video."""

        prev_video_id = self._video_library.playing;
        prev_video = self._video_library.get_video(prev_video_id);

        if self._video_library.is_paused:
            print('Video already paused: {}'.format(prev_video.title))
        elif not self._video_library.playing:
            print("Cannot pause video: No video is currently playing")
        else:
            print('Pausing video: {}'.format(prev_video.title))
            self._video_library.pause_video()

    def continue_video(self):
        """Resumes playing the current video."""

        if not self._video_library.playing:
            print("Cannot continue video: No video is currently playing")
        elif not self._video_library.is_paused:
            print("Cannot continue video: Video is not paused")
        else:
            prev_video_id = self._video_library.playing;
            prev_video = self._video_library.get_video(prev_video_id);
            print('Continuing video: {}'.format(prev_video.title))
            self._video_library.now_playing(prev_video_id)


    def show_playing(self):
        """Displays video currently playing."""

        video_id = self._video_library.playing;
        video = self._video_library.get_video(video_id);
        
        if video:
            out = 'Currently playing: {title} ({id}) [{tags}]'.format(title=video.title, id=video.video_id, tags=' '.join(video.tags))
            if self._video_library.is_paused:
                out = out + " - PAUSED"
            print(out)
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlists = self._video_library.playlists

        if playlist_name.lower() in playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._video_library.create_playlist(playlist_name)
            print("Successfully created new playlist: " + playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
