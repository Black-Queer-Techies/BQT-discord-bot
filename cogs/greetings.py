from discord.ext import commands


class Greetings(commands.Cog, name="Greetings module"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(928000257973964810)
        await channel.send(f"Welcome to Black Queer Techies {member.mention}!")
