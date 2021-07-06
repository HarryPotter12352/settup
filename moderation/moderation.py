import discord
from discord.ext import commands 
import asyncio 
import datetime 



class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


        @commands.command()
        async def ban(ctx, member : discord.Member, *, reason : str):
            """
            Bans a member from a server
            Very used command
            """
            await member.ban(reason=reason)
            