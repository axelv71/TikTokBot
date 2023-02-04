import os
import time
from dotenv import load_dotenv

from Controller.Downloader.Downloader import Downloader
from Controller.Editor.Slicer import Slicer
from Controller.Editor.Cropper import Cropper
from Controller.Tiktok_uploader import uploadVideo

from Controller.Scrapper import Scrapper
from Entity.Video import Video
from Entity.VideoFile import VideoFile
from database.Database import Database

if __name__ == '__main__':

    load_dotenv()
    session_id = str(os.getenv('TIKTOK_SESSION_ID'))

    print('Starting TikTokBot...')
    print('---------------------')

    # Initialize database
    db: Database = Database()

    # Scrapping
    scrapper: Scrapper = Scrapper(channel_url='https://www.youtube.com/@MontreuxComedy')
    video: Video = scrapper.get_random_video(videos=scrapper.scrap_all_videos())

    # If video is already in database, scrap another video
    while db.get_video(video) is not None:
        print(f'Video "{video.title}" already in database. Scraping another video...')
        video = scrapper.get_random_video(videos=scrapper.scrap_all_videos())

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

    # Save and upload slice video
    for i in range(len(video_parts)):
        os.makedirs(f'./output/{video_parts[i].video_filename}', exist_ok=True)
        slicer.save(video_parts[i].video, f'./output/{slicer.video.video_filename}/{slicer.video.video_filename}_{i}.mp4')

        time.sleep(30)
        uploadVideo(session_id=session_id, video=f'./output/{slicer.video.video_filename}/{slicer.video.video_filename}_{i}.mp4', title=str(f'{video_parts[i].title} - Part {i + 1}'), tags=["Funny", "Joke", "monteuxcomedy", "fyp", "montreux", "comedy"])

    # Insert video in database
    db.insert_video(video)

    # Delete temp file
    os.unlink(temp_path)
