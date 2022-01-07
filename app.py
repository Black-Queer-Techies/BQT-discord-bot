import os
import random
import discord

from client.main_bot_client import MainBotClient
from cogs.tech_news_cog import TechNewsCog
from cogs.greetings import Greetings


def start():
    token = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.members = True

    bot = MainBotClient(command_prefix=".", intents=intents)

    # Adding all cogs to BQTBot
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
        else:
            print("Unable to load ", filename[:3])

    bot.run(token)


if __name__ == "__main__":
    start()
