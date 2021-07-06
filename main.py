import discord
from discord.ext import commands


def init(prefix):
    prefix = str(prefix)
    client = commands.Bot(command_prefix=prefix)
    return client


