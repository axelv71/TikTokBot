import os

from moviepy.video.compositing.CompositeVideoClip import clips_array, CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

from Controller.Editor.Editor import Editor
from Entity.VideoFile import VideoFile


class Stacker(Editor):
    def __init__(self, video: VideoFile):
        super().__init__(video)

    def stack(self, background: VideoFile) -> VideoFile:
        video_clip = VideoFileClip(background.path, target_resolution=(background.video_height, background.video_width))
        overlay_clip = VideoFileClip(self.video.path, has_mask=True, target_resolution=(round(self.video.video_height / 2), round(self.video.video_width / 2)))
        overlay_clip.set_position((round((background.video_width / 2) - (self.video.video_width / 2)), round((background.video_height / 2) - (self.video.video_height / 2))))

        final_video = CompositeVideoClip([video_clip, overlay_clip])

        final_video.write_videofile(
            "output_stacked.mp4",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
            threads=6,
        )