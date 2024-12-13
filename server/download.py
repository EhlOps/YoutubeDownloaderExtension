from pytube import YouTube
from app import logger


def download_video(url, output_path="/downloads"):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension="mp4").all()
        stream = stream[-1]
        stream.download(output_path)
    except Exception as e:
        logger.error(e)
