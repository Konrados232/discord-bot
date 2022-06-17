from discord.ext import commands
from Shared.Utils import Utils


class RandomCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="random")
    async def generate_random_number(self, ctx):
        await ctx.channel.send(str(Utils.randomize()) + "!")
