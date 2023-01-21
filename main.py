import os

from Controller.Downloader.Downloader import Downloader
from Controller.Editor.Slicer import Slicer
from Controller.Editor.Cropper import Cropper

from Controller.Scrapper import Scrapper
from Entity.Video import Video
from Entity.VideoFile import VideoFile

if __name__ == '__main__':
    # Scrapping
    scrapper: Scrapper = Scrapper(channel_url='https://www.youtube.com/@sciencetrash')
    video: Video = scrapper.get_random_video(videos=scrapper.scrap_all_videos())

    # Download video
    downloader = Downloader(url=video.url, path='./input')
    downloader.download()
    video_file = VideoFile(video=video, path=f'./input/{downloader.name}')


    # Crop video
    cropper = Cropper(video=video_file)
    temp_path: str = f'./temp/{cropper.video.video_filename}.mp4'
    cropper.save(cropper.crop(), temp_path)
    video_file = VideoFile(video=video, path=temp_path)

    # Slice video
    slicer = Slicer(video_file)
    print(slicer.video.video_duration)
    slicer.slice()

    # Delete temp file
    os.unlink(temp_path)
