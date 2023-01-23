from Controller.Editor.Editor import Editor
import os

from Entity.VideoFile import VideoFile


class Slicer(Editor):
    MIN_DURATION: int = 1.5
    MAX_PARTS: int = 5

    def __init__(self, video: VideoFile):
        super().__init__(video)

    def slice(self) -> [VideoFile]:
        parts = round(self.video.video_duration / self.MIN_DURATION)

        if parts > self.MAX_PARTS:
            parts = self.MAX_PARTS

        part_duration = round(self.video.video_duration / parts)

        video_parts: [VideoFile] = []
        for i in range(parts):
            start = i * part_duration
            end = start + part_duration

            if end > self.video.video_duration:
                end = self.video.video_duration

            print("Part: " + str(i))
            print("------")
            print("Start: " + str(start))
            print("End: " + str(end))
            print("duration: " + str(part_duration))

            video_parts.append(VideoFile(video=self.video, video_file=self.video.video.subclip(start, end)))

        return video_parts

    def save_parts(self, video_parts: [VideoFile]) -> None:
        for i in range(len(video_parts)):
            os.makedirs(f'./output/{self.video.video_filename}', exist_ok=True)
            self.save(video_parts[i].video, f'./output/{self.video.video_filename}/{self.video.video_filename}_{i}.mp4')

