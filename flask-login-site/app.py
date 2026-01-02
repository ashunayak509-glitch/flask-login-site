from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "mysecretkey123"

USERNAME = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("home"))

    error = None
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["user"] = USERNAME
            return redirect(url_for("home"))
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)


@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    channel_name = "Abhinam_Pixels"
    youtube_videos = [
        {"title": "Bournemouth Beach Day Out", "link": "https://www.youtube.com/watch?v=g82LuZl9pH0"},
        {"title": "10 mins Crispy cheese Sandwich Pizza Recipe", "link": "https://www.youtube.com/watch?v=0kYZFEK-K0E"},
        {"title": "Best thrilling view at Gandelbal", "link": "https://www.youtube.com/watch?v=mNaVBb_OK7s&pp=0gcJCU0KAYcqIYzv"}
    ]

    for video in youtube_videos:
        video_id = video["link"].split("v=")[-1].split("&")[0]
        video["thumbnail"] = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        video["embed"] = f"https://www.youtube.com/embed/{video_id}"

    return render_template("home.html", channel=channel_name, videos=youtube_videos)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
