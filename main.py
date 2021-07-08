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
            emby.set_thumbnail(url = "https://cdn.discordapp.com/avatars/566193564502196235/b624ea7737776938c070f6693c91abc9?size=2048")
            emby.set_footer(text = "Check Bot Status at https://RKS.aryamansri.repl.co ")
            await destination.send(embed=emby)

client.help_command = NewHelpName()
