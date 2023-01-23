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
    cropper.save(cropper.crop().video, temp_path)
    video_file = VideoFile(video=video, path=temp_path)

    # Slice video
    slicer = Slicer(video_file)
    video_parts: [VideoFile] = slicer.slice()

    # Save slice text
    for i in range(len(video_parts)):
        os.makedirs(f'./output/{video_parts[i].video_filename}', exist_ok=True)
        slicer.save(video_parts[i].video, f'./output/{slicer.video.video_filename}/{slicer.video.video_filename}_{i}.mp4')

    # Delete temp file
    os.unlink(temp_path)
