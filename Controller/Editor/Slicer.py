from Controller.Editor.Editor import Editor
import os


class Slicer(Editor):
    MIN_DURATION: int = 1.5
    MAX_PARTS: int = 5

    def __init__(self, input_video_path: str):
        super().__init__(input_video_path)

    def slice(self) -> None:
        parts = round(self.capture.duration / self.MIN_DURATION)

        if parts > self.MAX_PARTS:
            parts = self.MAX_PARTS

        part_duration = round(self.capture.duration / parts)

        for i in range(parts):
            start = i * part_duration
            end = start + part_duration

            if end > self.capture.duration:
                end = self.capture.duration

            print("Part: " + str(i))
            print("------")
            print("Start: " + str(start))
            print("End: " + str(end))
            print("duration: " + str(part_duration))

            os.makedirs(f'./output/{self.capture_name}', exist_ok=True)

            self.save(self.capture.subclip(start, end), f'./output/{self.capture_name}/{self.capture_name}_{i}.mp4')