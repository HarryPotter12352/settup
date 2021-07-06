import discord
from discord.ext import commands
import asyncio
import datetime
from dipytools import tools


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.command()
        @commands.has_permissions(ban_members=True)
        @commands.bot_has_permissions(ban_members=True)
        async def ban(ctx, member: discord.Member, *, reason: str):
            """
            Bans a member from a server
            Very used command
            """
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Banned", description=f"You have been banned from **{ctx.guild.name} by **{ctx.author}** for reason **{reason}**", colour=ctx.author.colour, timestamp = datetime.datetime.now())
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await member.send(embed=embed)


        @ban.error 
        async def ban_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"You need the `ban_members` permissions required to run this command {ctx.author.mention}!")
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please provide all of the vaild parameters. They are `member` and `reason`")
            if isinstance(error, commands.BotMissingPermissions):
                await ctx.send("I do not have the needed permissions! They are `Ban members`")
            if isinstance(error, commands.MemberNotFound):
                await ctx.send("They're a :ghost: How do I interact with them?")

        @commands.command()
        @commands.has_permissions(kick_members=True)
        @commands.bot_has_permissions(kick_members=True)
        async def kick(ctx, member : discord.Member, *, reason : str):
            """
            Kicks a member
            """
            await member.kick(reason=reason)
            embed = discord.Embed(title="Kicked", description=f'You have been kicked from **{ctx.guild.name}** by **{ctx.author}** for reason **{reason}**', timestamp = datetime.datetime.now(), colour = ctx.author.colour)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await member.send(embed=embed)
