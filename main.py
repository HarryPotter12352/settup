from datetime import datetime
import discord
from discord.ext import commands



def init(prefix):
    prefix = str(prefix)
    client = commands.Bot(command_prefix=prefix)
    return client


def help(client : commands.Bot):
    commands = client.commands 
    embed = discord.Embed(title="List of all commands", colour = discord.Colour.random(), timestamp=datetime.now())
    for command in commands:
        embed.add_field(name=command.name, value = command.description)
        return embed
