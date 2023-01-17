import os

from Controller.Slicer import Slicer
from Controller.Cropper import Cropper
from Controller.Downloader import Downloader

if __name__ == '__main__':
    # Download video
    downloader = Downloader("https://www.youtube.com/watch?v=UqvqnL4IQ1g", './input')
    downloader.download()
    video_path: str = f'./input/{downloader.name}'

    # Crop video
    cropper = Cropper(video_path)
    temp_path: str = f'./temp/{cropper.capture_name}.mp4'
    cropper.save(cropper.crop(), temp_path)

    # Slice video
    slicer = Slicer(temp_path)
    print(slicer.capture.duration)
    slicer.slice()

    # Delete temp file
    os.unlink(temp_path)