import discord
from discord.ext import commands


def init(prefix):
    prefix = str(prefix)
    client = commands.Bot(command_prefix=prefix)
    return client


class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, colour = discord.Colour.red(), title = ":bookmark_tabs: | Help Menu")
            emby.set_thumbnail(url = " ")
            await destination.send(embed=emby)

client.help_command = NewHelpName()
