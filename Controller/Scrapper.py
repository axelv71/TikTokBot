import random
import scrapetube

from Entity.Video import Video


class Scrapper:
    def __init__(self, channel_url: str):
        self.channel_url: str = channel_url

    def scrap_all_videos(self) -> [Video]:
        videos: [Video] = []
        scrapped_videos: [] = scrapetube.get_channel(channel_url=self.channel_url)

        for video in scrapped_videos:
            videos.append(Video(video['videoId'], video['title']['runs'][0]['text'], video['descriptionSnippet']['runs'][0]['text'], video['thumbnail']['thumbnails'][3]['url'], "https://www.youtube.com/watch?v=" + video['videoId']))

        return videos

    def get_random_video(self, videos: [Video]) -> Video:
        return videos[random.randint(0, len(videos) - 1)]


