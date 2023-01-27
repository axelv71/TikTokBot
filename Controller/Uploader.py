import os
import time
from pathlib import Path

from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Entity.VideoFile import VideoFile


class Uploader:
    def __init__(self, video: VideoFile):
        #os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --remote-debugging-port=9999 --user-data-dir=/Users/axelvion/Library/\"Application Support\"/Google/Chrome/Default")
        #time.sleep(5)
        chrome_options = Options()
        # Récuperez l'instance de Chrome
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")

        # Téléchargez chromedriver exécutable depuis https://chromedriver.chromium.org/downloads et rensignez son
        # chemin absolu
        chrome_driver = Service("/Users/axelvion/Developer/Python/TikTokBot/chromedriver")  # A MODIFIER
        driver = webdriver.Chrome(service=chrome_driver, options=chrome_options)

        # Open TikTok upload page
        driver.get("https://www.tiktok.com/upload/?lang=fr")


        input("Login to your account and press enter to continue...")
        print("Starting upload...")

        # Switch to the upload iframe
        iframe = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/iframe')
        driver.switch_to.frame(iframe)

        # Upload video
        upload_video = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/input')
        upload_video.send_keys(video.path)
        print("Video uploaded")
        time.sleep(10)




