import discord
from discord.ext import commands
import datetime
import random



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
               
        @commands.command()
        async def say(ctx, *, content : str):
            await ctx.message.delete()
            await ctx.send(content)

        
        @say.error 
        async def say_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please give me what I need to say!")

        
        @commands.command()
        async def poll(ctx,*, content : str):
            await ctx.message.delete()
            embed = discord.Embed(title=content, description = f"Question by {ctx.author.mention}", colour= ctx.author.colour)
            my_msg = await ctx.send(embed=embed)
            await my_msg.add_reaction("✅")
            await my_msg.add_reaction("❌")


        @poll.error 
        async def poll_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(f"What do you wanna ask the people?")

        
        @commands.command()
        async def add(ctx, no1 : float, no2 : float):
            await ctx.send(no1+no2)

        @add.error 
        async def add_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please give the first number and the second!")

        
        @commands.command()
        async def subtract(ctx, no1 : float, no2 : float):
            await ctx.send(no1-no2)

        @subtract.error 
        async def subtract_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please give the first number and the second!")

        
        @commands.command()
        async def multiply(ctx, no1 : float, no2 : float):
            await ctx.send(no1*no2)

        @multiply.error 
        async def multiply_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please give the first number and the second!")

        
        @commands.command()
        async def divide(ctx, no1 : float, no2 : float):
            await ctx.send(no1+no2)

        @divide.error 
        async def divide_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please give the first number and the second!")

        
        @commands.command()
        async def roll(ctx, no1, no2):
            await ctx.send(random.randint(no1, no2))
            
            
        def setup(client):
            client.add_cog(Utility(client))
