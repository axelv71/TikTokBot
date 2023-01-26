import sys

from pytube import YouTube
from cleantext import clean


class Downloader:
    def __init__(self, url, path):
        self.name = None
        self.url = url
        self.path = path

    def download(self):
        print(f'Downloading {self.url}...')
        youtube = YouTube(self.url, on_progress_callback=self.progress)
        youtube = youtube.streams.get_highest_resolution()
        self.name = self.format_name(youtube.default_filename)
        print(self.name)
        try:
            youtube.download(self.path, self.name)
            print(f'\nDownloaded {self.name} successfully!')
        except:
            print("Error downloading video")

    def format_name(self, name: str) -> str:
        formatted_name: str = clean(name, to_ascii=True, lower=True, no_line_breaks=True, no_urls=True, no_emoji=True)
        formatted_name = formatted_name.replace(' ', '_')
        return formatted_name

    def progress(self, stream, chunk, bytes_remaining):
        percent = int((stream.filesize - bytes_remaining) / stream.filesize * 100)
        sys.stdout.write(f'\rProgress: {percent}%')
        sys.stdout.flush()



