import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import requests
import datetime





def keep_alive():
    """
    This will host your bot for 1 hour
    To continue with the hosting, you have to link it up with an uptime service
    Note: This will work on on replit
    """
    app = Flask("")
    @app.route("/")
    def home():
        return "Your bot is now alive!"

    def run():
        app.run(host="0.0.0.0", port=8080)


    server = Thread(target=run)
    server.start()


def meme():
    """
    This function let's you easily access memes
    """
    a = requests.get("https://meme-api.herokuapp.com/gimme/memes")
    b = a.json()
    title = b["title"]
    upvote = b["ups"]
    img = b["url"]
    author = b["author"]

    embed = discord.Embed(title=title,description=f"By **{author}**", color=0xFF5733)
    embed.set_image(url=img)
    embed.set_footer(text = f"{upvote} upvotes")
    return embed


def getimg(topic):
    """
    This feature allows you to easily grab images from anywhere
    """
    topic = str(topic)
    embed = discord.Embed(title=f"Image on {topic}!", colour = discord.Colour.random(), timestamp = datetime.datetime.now())
    url = f"https://source.unsplash.com/900x/900/?{topic}"
    embed.set_image(url=url)
    return embed
