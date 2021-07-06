import discord
from discord.ext import commands
import datetime



class Avatar(commands.Cog):
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
        
        def setup(client):
            client.add_cog(Avatar(client))