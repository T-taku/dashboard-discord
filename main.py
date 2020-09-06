from flask import Flask, redirect, url_for, Unauthorized
from flask_discord import DiscordOAuth2Session, Unauthorized
from flask import *



app = Flask(__name__)

app.secret_key = b"seacret_key_here"

app.config["DISCORD_CLIENT_ID"] = 0000#CLIENTID here
app.config["DISCORD_CLIENT_SECRET"] = "CLIENT"
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)


@app.route("/")
def index():
    try:
        user = discord.fetch_user()
        return render_template("login-index.html",name=user.name,img=user.avatar_url)
    except:
        return render_template("not-login.html")

@app.route("/login/")
def login():
   return discord.create_session(["identify", "guilds"])

@app.route("/callback/")
def callback():
    discord.callback()
    return redirect(url_for(".index"))

@app.route("/server/")
def server():
    server = discord.fetch_guilds()
    #...

@app.route("/logout/")
def logout():
    discord.revoke()
    return redirect(url_for(".index"))

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html")

@app.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for(".login"))

if __name__ == "__main__":
    app.run(debug=True)
