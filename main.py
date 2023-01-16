import os

from Controller.Slicer import Slicer
from Controller.Cropper import Cropper

if __name__ == '__main__':
    video_path = './input/input.mp4'

    cropper = Cropper(video_path)

    temp_path: str = f'./temp/{cropper.capture_name}.mp4'

    cropper.save(cropper.crop(), temp_path)

    slicer = Slicer(temp_path)

    print(slicer.capture.duration)

    slicer.slice()

    os.unlink(temp_path)