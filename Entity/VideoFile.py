from moviepy.editor import VideoFileClip, VideoClip
from Entity.Video import Video


class VideoFile(Video):
    def __init__(self, video: Video, path: str = None, video_file: VideoClip = None):
        if path is None:
            self.video = video_file
        else:
            self.path = path
            self.video: VideoFileClip = VideoFileClip(self.path)

        super().__init__(video.id, video.title, video.description, video.thumbnail, video.url)
        self.video_width: int = self.video.w
        self.video_height: int = self.video.h
        self.video_filename: str = self.video.filename.split('/')[-1].split('.')[0]
        self.video_duration: int = self.video.duration