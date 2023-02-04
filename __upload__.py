import os

from Controller.Tiktok_uploader import uploadVideo
from dotenv import load_dotenv

load_dotenv()

session_id = str(os.getenv('TIKTOK_SESSION_ID'))

print(session_id)

file = "/Users/axelvion/Developer/Python/TikTokBot/input/test.mp4"
title =  "Test title"
tags = ["Funny", "Joke", "fyp"]

uploadVideo(session_id, file, title, tags, verbose=True)
