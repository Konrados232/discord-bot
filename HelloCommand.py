from discord.ext import commands


class HelloCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")
