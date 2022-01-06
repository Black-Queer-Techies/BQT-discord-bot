import discord


class Greetings(discord.ext.commands.Cog, name="Greetings module"):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="hey")
    async def adhoc_play(self, client):
        await client.send(f"Hey {client.author.name}")

    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"A wild {member.mention} has appeared!")