from discord.ext import commands

class MainBotClient(commands.Bot):
    async def on_ready(self):
        print(
            f'{self.user.name} bot user is connected to the server.'
        )
    