from moviepy.editor import VideoFileClip
from abc import ABC


class VideoEditor(ABC):
    def __init__(self, video_path: str):
        self.capture: VideoFileClip = VideoFileClip(video_path)

        self.capture_width: int = self.capture.w
        self.capture_height: int = self.capture.h
