import os
import random
import discord

from client.main_bot_client import MainBotClient
from cogs.tech_news_cog import TechNewsCog


def start():
    # token = os.getenv("DISCORD_TOKEN")
    token = "OTI4MDI0MjI2ODc3ODI1MTM0.YdSv6Q.AXuq6gtK7vWYT4hNdp8pDzfBQIM"

    intents = discord.Intents.default()
    intents.members = True

    bot = MainBotClient(command_prefix="$", intents=intents)

    # Adding cogs
    bot.add_cog(TechNewsCog(bot))

    bot.run(token)


if __name__ == "__main__":
    start()
