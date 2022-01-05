import os
import random
import discord

from clients.main_bot_client import MainBotClient

# Code for discord channel

#token = os.getenv("DISCORD_TOKEN")
#my_guild = os.getenv("DISCORD_GUILD")

def run_bot():
    token = "OTI4MDI0MjI2ODc3ODI1MTM0.YdSv6Q.VRTp6YN4tpwUOrR2vGzEtfeNNGQ"
    my_guild = "927996396823515206"    
    
    intents = discord.Intents.default()
    my_client = discord.Client(intents=intents)

    bot = MainBotClient(
        command_prefix='$'
    )

    bot.run(token)

if __name__ == "__main__":
    run_bot()