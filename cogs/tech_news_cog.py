import discord

DISCORD_CHANNEL_ID = 928409579820290069


class TechNewsCog(discord.ext.commands.Cog, name="Tech News module"):
    """
    This class contains processes that obtain
    the latest news articles in tech and publishes them
    to the daily-tech-news channel.
    """

    def __init__(self, bot):
        self.bot = bot

    def get_news_article(self):
        return "Testing the works..."

    @discord.ext.commands.command()
    async def publish_news_article(self):
        channel = self.bot.get_channel(DISCORD_CHANNEL_ID)
        await channel.send(self.get_news_article())
