import json
import decimal
import discord
from discord.ext import commands
import aiohttp


class Quote(commands.Cog):
  def __init__(self,client):
    self.client = client

    @commands.command("quote")  
    async def q(self,ctx):
        async with aiohttp.ClientSession() as r:
            async with r.get("https://api.quotable.io/random") as r:
                data = await r.json()

                embed = discord.Embed(title = "Quote for you", description = f'{data["content"]}', colour = discord.Colour.blue()) 
                embed.set_thumbnail(url=' ')

                await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Quote(client))