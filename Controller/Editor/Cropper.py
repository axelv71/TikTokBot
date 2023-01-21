from moviepy.editor import *
from moviepy.video.fx.crop import crop

from Controller.Editor.Editor import Editor
from Entity.VideoFile import VideoFile


class Cropper(Editor):
    # Ratio portrait 9/16
    RATIO_WIDTH: int = 9
    RATIO_HEIGHT: int = 16

    def __init__(self, video: VideoFile):
        super().__init__(video)

        self.crop_width = round((self.video.video_height / self.RATIO_HEIGHT) * self.RATIO_WIDTH)
        self.start_x = round((self.video.video_width - self.crop_width) / 2)

    # Crop video
    def crop(self) -> VideoClip:
        return crop(self.video.video, x1=self.start_x, y1=0, x2=self.start_x + self.crop_width, y2=self.video.video_height)

    # Play cropped video
    def play_crop(self) -> None:
        self.crop().preview()

