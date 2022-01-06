import asyncio
import requests

from discord.ext import commands, tasks

DISCORD_CHANNEL_ID = 928409579820290069


class TechNewsCog(commands.Cog, name="Tech News module"):
    """
    This class contains processes that obtain
    the latest news articles in tech and publishes them
    to the daily-tech-news channel.
    """

    def __init__(self, bot):
        self.bot = bot
        self.send_news_article_link.start()

    @tasks.loop(hours=24)
    async def send_news_article_link(self):
        channel = self.bot.get_channel(DISCORD_CHANNEL_ID)

        news_api_key = os.getenv("NEWS_API_TOKEN")
        url = (
            "https://newsapi.org/v2/top-headlines?"
            "sources=techcrunch&"
            "apiKey={apiKey}"
        ).format(apiKey=news_api_key)

        response = requests.get(url)
        articles = response.json()["articles"]
        for article in articles[0:2]:
            url = article["url"]
            await channel.send(url)

            await asyncio.sleep(5)

    @send_news_article_link.before_loop
    async def before_send_news_article_link(self):
        await self.bot.wait_until_ready()
