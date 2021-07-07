import discord
from discord.ext import commands
from flask import Flask
from threading import Thread





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