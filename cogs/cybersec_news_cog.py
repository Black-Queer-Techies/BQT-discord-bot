import asyncio
import requests
import os
import logging
import requests

from discord.ext import commands, tasks
from datetime import datetime

DISCORD_CHANNEL_ID = 932031078074572881


class CyberSecNews(commands.Cog, name="Cyber Security News Modules"):
    """
    This class contains processes that obtain
    the latest news articles in cybersecurity and publishes them
    to the cybersecurity-news channel.
    """

    def __init__(self, bot):
        self.bot = bot
        self.send_news_article_link.start()

    @tasks.loop(seconds=1)
    async def send_news_article_link(self):
        execution_time = "10:00:00"  # Setting time to 10AM
        now = datetime.now().strftime("%H:%M:%S")

        channel = self.bot.get_channel(DISCORD_CHANNEL_ID)

        if execution_time == now:
            news_api_key = os.getenv("NEWS_API_TOKEN")
            url = (
                "https://newsapi.org/v2/top-headlines?"
                "sources=hacker-news&"
                "apiKey={apiKey}"
            ).format(apiKey=news_api_key)

            response = requests.get(url)
            articles = response.json()["articles"]
            for article in articles[0:2]:
                logging.info(
                    "Sending this article to the discord server: ", str(article)
                )
                url = article["url"]
                await channel.send(url)
                await asyncio.sleep(5)

    @send_news_article_link.before_loop
    async def before_send_news_article_link(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(CyberSecNews(bot))
