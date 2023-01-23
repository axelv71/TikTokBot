import sqlite3
from pathlib import Path

from Entity.Video import Video


class Database:
    def __init__(self):
        self.path = Path('db.sqlite')
        if not self.path.exists():
            self.create_database()

        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS videos (id TEXT PRIMARY KEY, url TEXT, title TEXT, description TEXT, thumbnail TEXT);')
        self.connection.commit()

    def create_database(self):
        f = open(self.path, 'w')
        f.close()

    def insert_video(self, video: Video):
        self.cursor.execute('INSERT INTO videos VALUES (?, ?, ?, ?, ?);', (video.id, video.url, video.title, video.description, video.thumbnail))
        self.connection.commit()

    def get_all_videos(self) -> [Video]:
        self.cursor.execute('SELECT * FROM videos;')
        return self.cursor.fetchall()

    def get_video(self, video: Video) -> Video:
        self.cursor.execute('SELECT * FROM videos WHERE id=?;', (video.id,))
        return self.cursor.fetchone()
