import discord
from discord.ext import commands
import datetime



class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.command()
        async def avatar(ctx, member : discord.Member = None):
            """
            Returns the member's avatar
            """
            if member == None:
                member = ctx.author 
            else:
                member = member 
            embed = discord.Embed(title=f"{member}'s avatar", description = " ", timeatamp = datetime.datetime.now())
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

        @commands.command()
        async def id(ctx, member : discord.Member = None):
            """
            Gives you your or anyone else's id"""
            if member == None:
                await ctx.send(f"{ctx.author}'s id is {ctx.author.id}!")
            else:
                await ctx.send(f"{member}'s id is {member.id}!")
        
        def setup(client):
            client.add_cog(Utility(client))