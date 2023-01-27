from pathlib import Path

from Controller.Scrapper import Scrapper
from Controller.Uploader import Uploader
from Entity.Video import Video
from Entity.VideoFile import VideoFile

scrapper: Scrapper = Scrapper(channel_url='https://www.youtube.com/@sciencetrash')
video: Video = scrapper.get_random_video(videos=scrapper.scrap_all_videos())

video_file = VideoFile(video=video, path=str(Path.cwd() / 'input' / 'test.mp4'))

uploader = Uploader(video_file)
