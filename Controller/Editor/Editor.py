from moviepy.editor import VideoFileClip, VideoClip
from abc import ABC

from Entity.VideoFile import VideoFile


class Editor(ABC):
    def __init__(self, video: VideoFile):
        self.video: VideoFile = video


    # Play video
    def play(self) -> None:
        self.video.video.preview()

    # Save video
    @staticmethod
    def save(video: VideoFileClip, location: str) -> None:
        video.write_videofile(location, audio_codec='aac', codec='libx264')