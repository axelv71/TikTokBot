from Controller.VideoSlicer import VideoSlicer
from Controller.VideoCropper import VideoCropper

if __name__ == '__main__':
    #video_path = './input/input.mp4'

    #video_cropper = VideoCropper(video_path)

    #video_cropper.save(video_cropper.crop(), "./output/cropped.mp4")


    video_slicer = VideoSlicer("./output/cropped.mp4")

    print(video_slicer.capture.duration)

    video_slicer.slice()