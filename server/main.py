from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/yt-dl", methods=["GET"])
def yt_dl():
    data = request.data
    return jsonify({"message": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
