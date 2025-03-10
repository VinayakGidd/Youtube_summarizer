# from flask import Flask, render_template, request
# from src.youtube_summary import summarize_youtube_video

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     summary = None
#     if request.method == "POST":
#         video_url = request.form["video_url"]
#         method = request.form["method"]
#         summary = summarize_youtube_video(video_url, method=method)
    
#     return render_template("index.html", summary=summary)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
from src.youtube_summary import summarize_youtube_video
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        video_url = request.form["video_url"]
        method = request.form["method"]
        summary = summarize_youtube_video(video_url, method=method)
    
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns a dynamic port
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0 for public access
