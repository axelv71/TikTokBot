import os

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from pathlib import Path

from Controller.Downloader.Downloader import Downloader
from Controller.Editor.Slicer import Slicer
from Controller.Editor.Cropper import Cropper
from Controller.Editor.Stacker import Stacker

from Controller.Scrapper import Scrapper
from Entity.Video import Video
from Entity.VideoFile import VideoFile
from database.Database import Database

if __name__ == '__main__':
    # Initialize database
    db: Database = Database()

    # Scrapping
    scrapper: Scrapper = Scrapper(channel_url='https://www.youtube.com/@sciencetrash')
    video: Video = scrapper.get_random_video(videos=scrapper.scrap_all_videos())

    # If video is already in database, scrap another video
    while db.get_video(video) is not None:
        print(f'Video "{video.title}" already in database. Scraping another video...')
        video = scrapper.get_random_video(videos=scrapper.scrap_all_videos())

    # Download video
    #downloader = Downloader(url=video.url, path='./input')
    #downloader.download()
    video_file = VideoFile(video=video, path=str(Path.cwd() / 'input' / 'input.mp4'))

    # Crop video
    #cropper = Cropper(video=video_file)
    #temp_path: str = str(Path.cwd() / 'temp' / f'{cropper.video.video_filename}_cropped.mp4')
    #cropper.save(cropper.crop().video, temp_path)
    #video_file = VideoFile(video=video, path=temp_path)

    # Stack video
    background = VideoFile(video=video, path=str(Path.cwd() / 'assets' / 'background.mp4'))
    stacker = Stacker(video=video_file)
    stacker.stack(background=background)

    # Slice video
    #slicer = Slicer(video_file)
    #video_parts: [VideoFile] = slicer.slice()

    # Save slice video
    #for i in range(len(video_parts)):
    #    os.makedirs(f'./output/{video_parts[i].video_filename}', exist_ok=True)
    #    slicer.save(video_parts[i].video, f'./output/{slicer.video.video_filename}/{slicer.video.video_filename}_{i}.mp4')

    # Insert video in database
   # db.insert_video(video)

    # Delete temp file
   # os.unlink(temp_path)
