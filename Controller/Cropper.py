from moviepy.editor import *
from moviepy.video.fx.all import *
from moviepy.video.fx.crop import crop

from Controller.Editor import Editor


class Cropper(Editor):
    # Ratio portrait 9/16
    RATIO_WIDTH: int = 9
    RATIO_HEIGHT: int = 16

    def __init__(self, video_path: str):
        super().__init__(video_path)

        self.crop_width = round((self.capture_height / self.RATIO_HEIGHT) * self.RATIO_WIDTH)
        self.start_x = round((self.capture_width - self.crop_width) / 2)

    # Crop video
    def crop(self) -> VideoClip:
        return crop(self.capture, x1=self.start_x, y1=0, x2=self.start_x + self.crop_width, y2=self.capture_height)

    # Play cropped video
    def play_crop(self) -> None:
        self.crop().preview()

