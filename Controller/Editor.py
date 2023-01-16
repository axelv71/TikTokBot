from moviepy.editor import VideoFileClip, VideoClip
from abc import ABC


class Editor(ABC):
    def __init__(self, video_path: str):
        self.capture: VideoFileClip = VideoFileClip(video_path)

        self.capture_width: int = self.capture.w
        self.capture_height: int = self.capture.h
        self.capture_name: str = self.capture.filename.split('/')[-1].split('.')[0]

    # Play video
    def play(self) -> None:
        self.capture.preview()

    # Save video
    @staticmethod
    def save(video: VideoClip, location: str) -> None:
        video.write_videofile(location)