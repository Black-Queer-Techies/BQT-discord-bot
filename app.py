import os
import random
import discord

from clients.main_bot_client import MainBotClient

def run_bot():
    token = os.getenv("DISCORD_TOKEN")
    my_guild = os.getenv("DISCORD_GUILD")
    
    intents = discord.Intents.default()
    my_client = discord.Client(intents=intents)

    bot = MainBotClient(
        command_prefix='$'
    )

    bot.run(token)

if __name__ == "__main__":
    run_bot()