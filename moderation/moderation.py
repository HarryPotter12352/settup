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
            await ctx.send(f"Successfully banned {member}!")


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
            await ctx.send(f"Successfully kicked {member}!")

        @kick.error 
        async def ban_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"You need the `kick_members` permissions required to run this command {ctx.author.mention}!")
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please provide all of the vaild parameters. They are `member` and `reason`")
            if isinstance(error, commands.BotMissingPermissions):
                await ctx.send("I do not have the needed permissions! They are `Kick members`")
            if isinstance(error, commands.MemberNotFound):
                await ctx.send("They're a :ghost: How do I interact with them?")


        @commands.command()
        @commands.has_permissions(manage_messages=True)
        @commands.bot_has_permissions(manage_roles=True)
        async def mute(ctx, member : discord.Member, *, reason : str):
            """
            Mutes a member from sending any messages
            """
            mutedRole = discord.utils.get(ctx.guild.roles, name = "Muted")
            if not mutedRole:
                channels = 0
                mutedRole = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(mutedRole, send_messages=False)
                    channels += 1 
                await ctx.send(f"Successfully applied overwrites for {channels} channels")
            await member.add_roles(mutedRole)
            embed = discord.Embed(title="Muted", description = f"You have been muted in **{ctx.guild.name}** by **{ctx.author}** **indefinetly** for reason **{reason}**", colour = ctx.author.color, timestamp = datetime.datetime.now())
            await member.send(embed=embed)


        @mute.error 
        async def mute_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"You need the `manage_messages` permissions required to run this command {ctx.author.mention}!")
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please provide all of the vaild parameters. They are `member` and `reason`")
            if isinstance(error, commands.BotMissingPermissions):
                await ctx.send("I do not have the needed permissions! They are `Manage roles`")
            if isinstance(error, commands.MemberNotFound):
                await ctx.send("They're a :ghost: How do I interact with them?")
