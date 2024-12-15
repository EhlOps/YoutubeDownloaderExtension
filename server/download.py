import yt_dlp
from app import logger


def format_selector(ctx):
    formats = ctx.get("formats")[::-1]
    best_video = next(
        f for f in formats if f["vcodec"] != "none" and f["acodec"] == "none"
    )

    audio_ext = {"mp4": "m4a", "webm": "webm"}[best_video["ext"]]
    best_audio = next(
        f
        for f in formats
        if (f["acodec"] != "none" and f["vcodec"] == "none" and f["ext"] == audio_ext)
    )

    yield {
        "format_id": f'{best_video["format_id"]}+{best_audio["format_id"]}',
        "ext": best_video["ext"],
        "requested_formats": [best_video, best_audio],
        "protocol": f'{best_video["protocol"]}+{best_audio["protocol"]}',
    }


def my_hook(d):
    if d["status"] == "finished":
        logger.info("Done downloading...")


def download_video(url, output_path="/downloads"):
    ydl_opts = {
        "logger": logger,
        "format": format_selector,
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "progress_hooks": [my_hook],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        logger.error(e)
