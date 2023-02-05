![made-with-python](https://img.shields.io/badge/Made%20with-Python3-brightgreen)

<br />
<div align="center">
  <div>
    <img src=".github/logo.png" alt="Logo" width="100" height="100">
  </div>

  <h3 align="center">TikTokBot</h3>

  <p align="center">
    Bot for downloads YouTube videos, crop them to TikTok format, and upload them to TikTok.
    <br />
    <br />
    <br />
  </p>
</div>

## Installation
Install the required packages using pip:
```sh
pip install -r requirements.txt
```

Rename the ```.env.example``` file to ```.env``` and fill in the required fields.

- ```TIKTOK_SESSION_ID``` - TikTok session ID. You can get it by logging in to TikTok and copying the value of the ```sessionid``` cookie. For more information, see [this](https://github.com/MiniGlome/Tiktok-uploader)
- ```CROP_RATIO_WIDTH``` - Width of the crop ratio. Example: 9
- ```CROP_RATIO_HEIGHT``` - Height of the crop ratio. Example: 16
- ```SLICE_MIN_DURATION``` - Minimum duration of the video slice. Example: 60 seconds
- ```SLICE_MAX_PARTS``` - Maximum number of parts to which the video will be divided. Example: 3
- ```TIKTOK_UPLOAD_DELAY``` - Delay between TikTok uploads. Recommended value: 30 seconds minimum

## Usage
Change the url of the YouTube channel in the ```main.py``` file:
```python
channel_url='https://www.youtube.com/@MontreuxComedy'
```

Run the ```main.py``` file:
```sh
python main.py
```

For cleaning the downloaded videos, run the ```clean.py``` file:
```sh
python clean.py
```
This will delete all videos.

## Sources
- [TikTok-uploader](https://github.com/MiniGlome/Tiktok-uploader)