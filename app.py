import os
import random
import discord

from client.main_bot_client import MainBotClient


def run_bot():
    token = os.getenv("DISCORD_TOKEN")

    bot = MainBotClient(command_prefix="$")
    bot.run(token)


if __name__ == "__main__":
    run_bot()
