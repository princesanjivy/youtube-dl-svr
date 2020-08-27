import youtube_dl as ytdl
from flask import Flask, request, jsonify

app = Flask(__name__)

def getVideoData(url):
    ydl_opts = {"forceip":"4"}
    ydl = ytdl.YoutubeDL(ydl_opts)
    with ydl:
        res = ydl.extract_info(url, download=False)
    return res["formats"][len(res["formats"])-1]["url"], res["title"]

@app.route("/geturl", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.json
        video_url, title = getVideoData(data["yt_url"])
        return jsonify({"video_url" : video_url, "title" : title})
    else:
        return "nothing here!"

##app.run()
