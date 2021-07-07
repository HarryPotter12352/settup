import discord
from discord.ext import commands
import datetime
import asyncio
import random


class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client 

        def convert(time):
            pos = ["s", "m", "h", "d"]

            time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24, "w" : 3600*24*7}

            unit = time[-1]

            if unit not in pos:
                return -1

            try:
                val = int(time[:-1])
            except:
                return -2


            return val * time_dict[unit]

        @commands.command()
        @commands.has_any_role("Owner", "Co-Owner", "Admin", "Moderator", "Giveaway Manager")
        async def giveaway(self, ctx, time, channel : discord.TextChannel = None,*, prize : str):
            await ctx.message.delete()
            if channel == None:
                channel = ctx.channel 
            converted_time = convert(time)
            if converted_time == -1 or -2:
                await ctx.send("Please provide vaild time!")
            else:
                embed = discord.Embed(title="Giveaway!", description = f'{prize}', colour = discord.Colour.random())
                end = datetime.datetime.utcnow() + datetime.timedelta(converted_time)
                embed.set_footer(f'Ends at {end} UTC')
                embed.add_field(name="Hosted by", value = f'{ctx.author}', inline = False)
                msg = await channel.send(embed=embed)
                await msg.add_reaction("🎉")
                await asyncio.sleep(converted_time)
                msg = await ctx.channel.fetch_message(msg.id)

                entries = msg.reactions[0].users().flatten()
                entries.pop(entries.index(self.client.user))

                winner = random.choice(entries)
                await channel.send(f'Congratulations, {winner}! You just won a giveaway of **{prize}**!')


            
        @giveaway.error 
        async def g_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("All the paramters needed are `time`, `channel` and `prize`")
            if isinstance(error, commands.MissingAnyRole):
                await ctx.send(f"You need the Owner, Co-Owner, Admin, Moderator, or Giveaway Manager role to execute this command!")
