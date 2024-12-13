from flask import jsonify, request, make_response
from app import app, logger
from download import download_video


@app.route("/yt-dl", methods=["POST"])
def yt_dl():
    data = request.json
    logger.info(data)
    url = data["url"]
    try:
        download_video(url)
        return make_response(jsonify({"message": "Download complete"}), 200)

    except Exception as e:
        logger.error(e)
        return make_response(jsonify({"message": "Failed to download video"}), 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
